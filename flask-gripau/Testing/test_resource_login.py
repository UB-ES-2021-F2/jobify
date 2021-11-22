import json
import unittest
from unittest import TestCase

from Testing import BaseTestCase
from db import db
from models import JobSeekersModel, CompanyModel


class TestLoginResource(BaseTestCase):

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

    def test_successful_job_seeker_login(self):
        self._add_data()

        response = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        self.assertEquals(response.status_code, 200)

    def test_invalid_password_job_seeker_login(self):
        self._add_data()

        response = self.client.post('/api/login', json={
            'username': 'test', 'password': 'wrong'
        })
        self.assertDictEqual(response.json, {"message": "Invalid password"})
        self.assertEquals(response.status_code, 400)

    def test_successful_company_login(self):
        self._add_data()

        response = self.client.post('/api/login', json={
            'username': 'username', 'password': 'Test1234'
        })
        self.assertEquals(response.status_code, 200)

    def test_invalid_password_company_login(self):
        self._add_data()

        response = self.client.post('/api/login', json={
            'username': 'username', 'password': 'wrong'
        })
        self.assertDictEqual(response.json, {"message": "Invalid password"})
        self.assertEquals(response.status_code, 400)

    def test_user_not_exists_login(self):
        response = self.client.post('/api/login', json={
            'username': 'not_exists', 'password': 'wrong'
        })
        self.assertDictEqual(response.json, {"message": "User doesn't exist"})
        self.assertEquals(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
