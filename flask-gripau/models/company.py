from flask import g, current_app
from db import db
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context as pwd_context

auth = HTTPBasicAuth()


class CompanyModel(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.String(256), unique=False, nullable=True)
    password = db.Column(db.String(128), nullable=False)
    # 0 not admin/ 1 is admin
    is_admin = db.Column(db.Integer, nullable=False, default=False)
    job_offers = db.relationship('JobOfferModel', backref='job_offer', lazy=True)

    def __init__(self, company, email, description, is_admin=0):
        self.company = company
        self.email = email
        self.is_admin = is_admin
        self.description = description

    def json(self):
        return {'id': self.id, 'company': self.company, 'email': self.email, 'is_admin': self.is_admin,
                'description': self.description}

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
        return s.dumps({'company': self.company})

    @classmethod
    def verify_auth_token(cls, token):
        s = Serializer(current_app.secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token

        user = cls.query.filter_by(company=data['company']).first()

        return user

    @classmethod
    def find_by_company(cls, company):
        return cls.query.filter_by(company=company).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def show_accounts(cls):
        return [user.json() for user in cls.query.all()]

@auth.verify_password
def verify_password(token, password):
    account = CompanyModel.verify_auth_token(token)
    if account:
        g.user = account
        return account

@auth.get_user_roles
def get_user_roles(user):
    if user.is_admin == 1:
        return ['admin']
    else:
        return ['user']
