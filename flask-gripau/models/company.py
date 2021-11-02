from flask import g, current_app
from db import db
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context as pwd_context

auth = HTTPBasicAuth()


class CompanyModel(db.Model):
    """
    Model of a company
    """
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    company = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.String(256), unique=False, nullable=True)
    password = db.Column(db.String(128), nullable=False)
    # 0 not admin/ 1 is admin
    is_admin = db.Column(db.Integer, nullable=False, default=False)
    job_offers = db.relationship('JobOfferModel', backref='job_offer', lazy=True)
    sector = db.Column(db.String(30))
    location = db.Column(db.String(30))

    def __init__(self, username, company, email, description, is_admin=0, sector="Unknown", location="Unknown"):    
        """
        Initializer of a company
        :param company: company name
        :param email: email of the company
        :param description: description of the company
        :param is_admin: if the user is admin of the website, 1 (yes) / 0 (no)
        :param sector: sector of the company
        :param location: location of the company
        """
        self.username = username
        self.company = company
        self.email = email
        self.is_admin = is_admin
        self.description = description
        self.sector = sector
        self.location = location

    def json(self):
        """
        Function that returns the company info as json
        :return: json object with the information'
        """
        return {'id': self.id, 'username': self.username, 'company': self.company, 'email': self.email, 'is_admin': self.is_admin,
                'description': self.description, 'sector': self.sector, 'location': self.location}

    def save_to_db(self, database=None):
        """
        Function that saves to the database the company
        :param database: database instance
        """
        if database is None:
            database = db
        database.session.add(self)
        database.session.commit()

    def delete_from_db(self, database=None):
        """
        Function that the deletes from the database the company
        :param database: database instance
        """
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    def hash_password(self, password):
        """
        Function that encrypts and sets the password of the company
        :param password: password of the company
        """
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        """
        Function that verifies if the password is the company's one
        :param password: password to verify
        :return: boolean, True (correct password) / False (incorrect password)
        """
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration=4000):
        """
        Function that generates an authentication token for the company
        :param expiration: expiration time of the token
        :return: token
        """
        s = Serializer(current_app.secret_key, expires_in=expiration)
        return s.dumps({'company': self.company})

    @classmethod
    def verify_auth_token(cls, token):
        """
        Function that returns the company related to the token
        :param token: token of the company
        :return: company, None if the token is expired or invalid
        """
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
    def find_by_username(cls, username):
        """
        Function that returns a company given the name
        :param username: username of the company
        :return: company
        """
        if not username:
            return None
        return cls.query.filter_by(username=username.lower()).first()

    @classmethod
    def find_by_company(cls, company):
        """
        Function that returns a company given the name
        :param company: name of the company
        :return: company
        """
        return cls.query.filter_by(company=company).first()

    @classmethod
    def find_by_email(cls, email):
        """
        Function that returns a company given the email
        :param email: email of the company
        :return: company
        """
        return cls.query.filter_by(email=email).first()

    @classmethod
    def show_accounts(cls):
        """
        Function that shows all the companies in the database
        :return: list of the companies
        """
        return [user.json() for user in cls.query.all()]


@auth.verify_password
def verify_password(token, password):
    """
    Function that sets the actual user as the company related to the token
    :param token: token of the company
    :return: company
    """
    account = CompanyModel.verify_auth_token(token)
    if account:
        g.user = account
        return account


@auth.get_user_roles
def get_user_roles(user):
    """
    Function that returns the roles of a company
    :param user: company
    :return: roles
    """
    if user.is_admin == 1:
        return ['admin']
    else:
        return ['user']
