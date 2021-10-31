from flask import current_app
from flask_testing import TestCase

from app import create_app
from db import db
from config import config


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config.update({
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'SQLALCHEMY_TRACK_MODIFICATIONS': False,
            'TESTING': True
        })
        with app.app_context():
            app.config['SECRET_KEY'] = "1q2s3f5g7jggujbffrhnbcdgh78jbhd"
        db.init_app(app)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
