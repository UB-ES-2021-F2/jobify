from flask import g, current_app
from db import db
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context as pwd_context

auth = HTTPBasicAuth()


class JobSeekersModel(db.Model):
    __tablename__ = 'jobseekers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    bio = db.Column(db.String(1024), unique=False, nullable=True)
    password = db.Column(db.String(128), nullable=False)
    # 0 not admin/ 1 is admin
    is_admin = db.Column(db.Integer, nullable=False, default=False)
    educations = db.relationship('EducationsModel', backref='educations', lazy=True)
    work_experiences = db.relationship('WorkExperiencesModel', backref='work_experiences', lazy=True)
    skills = db.relationship('SkillsModel', backref='skills', lazy=True)

    def __init__(self, username, name, surname, email, bio, is_admin=0):
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.is_admin = is_admin
        self.bio = bio

    def json(self):
        return {'id': self.id, 'username': self.username, 'name': self.name, 'surname': self.surname,
                'email': self.email, 'is_admin': self.is_admin,
                'bio': self.bio, 'educations': [education.json() for education in self.educations],
                'work_experiences': [we.json() for we in self.work_experiences],
                'skills': [skill.skill_name() for skill in self.skills]}

    def save_to_db(self, database=None):
        if database is None:
            database = db
        database.session.add(self)
        database.session.commit()

    def delete_from_db(self, database=None):
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(current_app.secret_key, expires_in=expiration)
        return s.dumps({'username': self.username})

    def delete_education(self, id):
        for e in self.educations:
            if e.id == id:
                self.educations.remove(e)
                return e
        return None

    def delete_work_experience(self, id):
        for w in self.work_experiences:
            if w.id == id:
                self.work_experiences.remove(w)
                return w
        return None

    @classmethod
    def verify_auth_token(cls, token):
        s = Serializer(current_app.secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token

        user = cls.query.filter_by(username=data['username']).first()

        return user

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def show_accounts(cls):
        return [user.json() for user in cls.query.all()]


@auth.verify_password
def verify_password(token, password):
    account = JobSeekersModel.verify_auth_token(token)
    if account:
        g.user = account
        return account


@auth.get_user_roles
def get_user_roles(user):
    if user.is_admin == 1:
        return ['admin']
    else:
        return ['user']
