from flask import g, current_app
from db import db
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context as pwd_context

auth = HTTPBasicAuth()


class JobSeekersModel(db.Model):
    """
    Model of a job seeker
    """
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
        """
        Initializer of a job seeker
        :param username: username of the job seeker
        :param name: real name of the job seeker
        :param surname: real surname of the job seeker
        :param email: email of the job seeker
        :param bio: biography/information that the job seeker would want to share
        :param is_admin: if the user is admin of the website, 1 (yes) / 0 (no)
        """
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.is_admin = is_admin
        self.bio = bio

    def json(self):
        """
        Function that returns the job seeker info as json
        :return: json object with the information'
        """
        return {'id': self.id, 'username': self.username, 'name': self.name, 'surname': self.surname,
                'email': self.email, 'is_admin': self.is_admin,
                'bio': self.bio, 'educations': [education.json() for education in self.educations],
                'work_experiences': [we.json() for we in self.work_experiences],
                'skills': [skill.json() for skill in self.skills]}

    def save_to_db(self, database=None):
        """
        Function that saves to the database the job seeker
        :param database: database instance
        """
        if database is None:
            database = db
        database.session.add(self)
        database.session.commit()

    def delete_from_db(self, database=None):
        """
        Function that the deletes from the database the job seeker
        :param database: database instance
        """
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    def hash_password(self, password):
        """
        Function that encrypts and sets the password of the user
        :param password: password of the job seeker
        """
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        """
        Function that verifies if the password is the user's one
        :param password: password to verify
        :return: boolean, True (correct password) / False (incorrect password)
        """
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration=600):
        """
        Function that generates an authentication token for the user
        :param expiration: expiration time of the token
        :return: token
        """
        s = Serializer(current_app.secret_key, expires_in=expiration)
        return s.dumps({'username': self.username})

    def delete_education(self, id):
        """
        Function that deletes an education from the education list of the job seeker
        :param id: id of the education
        :return: the education removed, None if the education does not exist
        """
        for e in self.educations:
            if e.id == id:
                self.educations.remove(e)
                return e
        return None

    def delete_work_experience(self, id):
        """
        Function that deletes a work experience from the work experience list of the job seeker
        :param id: id of the work experience
        :return: the work experience removed, None if the work experience does not exist
        """
        for w in self.work_experiences:
            if w.id == id:
                self.work_experiences.remove(w)
                return w
        return None

    @classmethod
    def verify_auth_token(cls, token):
        """
        Function that returns the user related to the token
        :param token: token of the user
        :return: user, None if the token is expired or invalid
        """
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
        """
        Function that returns a job seeker given the username
        :param username: username of the job seeker
        :return: job seeker
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        """
        Function that returns a job seeker given the email
        :param email: email of the job seeker
        :return: job seeker
        """
        return cls.query.filter_by(email=email).first()

    @classmethod
    def show_accounts(cls):
        """
        Function that shows all the job seekers in the database
        :return: list of the job seekers
        """
        return [user.json() for user in cls.query.all()]


@auth.verify_password
def verify_password(token, password):
    """
    Function that sets the actual user as the user related to the token
    :param token: token of the user
    :return: job seeker
    """
    account = JobSeekersModel.verify_auth_token(token)
    if account:
        g.user = account
        return account


@auth.get_user_roles
def get_user_roles(user):
    """
    Function that returns the roles of a job seeker
    :param user: job seeker
    :return: roles
    """
    if user.is_admin == 1:
        return ['admin']
    else:
        return ['user']
