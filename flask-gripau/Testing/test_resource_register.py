import json
import unittest
from unittest import TestCase

from Testing import BaseTestCase
from db import db
from models import JobSeekersModel, CompanyModel
from resources.Register import validate_password, validate_email


class TestRegisterResource(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def _add_data(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)

        new_company = CompanyModel('username', 'test', 'test@test.com', 'test')
        new_company.hash_password('Test1234')
        self._add_data_to_db(new_company)

    def test_validate_email(self):
        self.assertTrue(validate_email("mail@good.com"))
        self.assertFalse(validate_email("bad_mail."))

    def test_validate_password(self):
        self.assertTrue(validate_password("GoodP4assword"))
        self.assertFalse(validate_password("bad"))

    def test_alphanumeric_username(self):
        self._add_data()

        response = self.client.post('/api/register', json={
            'username': 'test_user', 'name': 'test', 'surname': 'test', 'password': 'Password123', 'is_job_seeker': 1,
            'email': 'ub@test.com', 'description': 'desc'
        })

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {'message': "Username must contain only alphanumeric characters"})

    def test_alpha_name(self):
        self._add_data()

        response = self.client.post('/api/register', json={
            'username': 'user', 'name': 'test4', 'surname': 'test', 'password': 'Password123', 'is_job_seeker': 1,
            'email': 'ub@test.com', 'description': 'desc'
        })

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {'message': "Name must contain only alphabetic characters or spaces"})

    def test_alpha_surname(self):
        self._add_data()

        response = self.client.post('/api/register', json={
            'username': 'user', 'name': 'test', 'surname': 'test4', 'password': 'Password123', 'is_job_seeker': 1,
            'email': 'ub@test.com', 'description': 'desc'
        })

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {'message': "Surname must contain only alphabetic characters"})

    def test_password_invalid(self):
        self._add_data()

        response = self.client.post('/api/register', json={
            'username': 'user', 'name': 'test', 'surname': 'test', 'password': 'a', 'is_job_seeker': 1,
            'email': 'ub@test.com', 'description': 'desc'
        })

        self.assertEquals(response.status_code, 406)
        self.assertDictEqual(response.json, {'message': "Password invalid! Does not meet requirements"})

    def test_job_seeker_exists(self):
        self._add_data()

        response = self.client.post('/api/register', json={
            'username': 'test', 'name': 'test', 'surname': 'test', 'password': 'Password123', 'is_job_seeker': 1,
            'email': 'ub@test.com', 'description': 'desc'
        })

        self.assertEquals(response.status_code, 409)
        self.assertDictEqual(response.json, {'message': "User already exists"})

    def test_company_exists(self):
        self._add_data()

        response = self.client.post('/api/register', json={
            'username': 'username', 'name': 'test', 'surname': 'test', 'password': 'Password123', 'is_job_seeker': 1,
            'email': 'ub@test.com', 'description': 'desc'
        })

        self.assertEquals(response.status_code, 409)
        self.assertDictEqual(response.json, {'message': "User already exists"})

    def test_invalid_email(self):
        self._add_data()

        response = self.client.post('/api/register',
                                    json={
                                        'username': 'user', 'name': 'test', 'surname': 'test', 'password':
                                            'Password123', 'is_job_seeker': 1,
                                        'email': 'invalid', 'description': 'desc'
                                    })
        self.assertEquals(response.status_code, 402)
        self.assertDictEqual(response.json, {'message': "Email wrong format!"})

        response = self.client.post('/api/register',
                                    json={
                                        'username': 'user', 'name': 'test', 'surname': 'test', 'password':
                                            'Password123', 'is_job_seeker': 1,
                                        'email': 'test@hotmail.com', 'description': 'desc'
                                    })
        self.assertEquals(response.status_code, 409)
        self.assertDictEqual(response.json, {'message': "Email already exists"})

        response = self.client.post('/api/register',
                                    json={
                                        'username': 'user', 'name': 'test', 'surname': 'test',
                                        'password': 'Password123', 'is_job_seeker': 1,
                                        'email': 'test@test.com', 'description': 'desc'
                                    })
        self.assertEquals(response.status_code, 409)
        self.assertDictEqual(response.json, {'message': "Email already exists"})

    def test_successful_job_seeker_register(self):
        self._add_data()

        response = self.client.post('/api/register', json={
            'username': 'user', 'name': 'test', 'surname': 'test', 'password': 'Password123', 'is_job_seeker': 1,
            'email': 'email@test.com', 'description': 'desc'
        })

        self.assertEquals(response.status_code, 201)

    def test_successful_company_register(self):
        self._add_data()

        response = self.client.post('/api/register', json={
            'username': 'user', 'name': 'ub', 'surname': 'test', 'password': 'Password123', 'is_job_seeker': 0,
            'email': 'email@test.com', 'description': 'desc'
        })

        self.assertEquals(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
