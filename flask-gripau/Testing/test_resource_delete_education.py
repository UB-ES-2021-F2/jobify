import base64
import unittest

from Testing import BaseTestCase
from db import db
from models import JobSeekersModel, EducationsModel


class TestDeleteEducationResource(BaseTestCase):
    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def _add_data(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_education = EducationsModel('Maths phd', 'UB', '2021-09', '2022-10', True)
        new_job_seeker.educations.append(new_education)
        self._add_data_to_db(new_job_seeker)

    def test_access_denied_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.post('/api/delete_education/test2',
                                    headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 401)
        self.assertDictEqual(response.json, {'message': 'Access denied'})

    def test_successful_delete_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.post('/api/delete_education/test',
                                    headers={"Authorization": "Basic " + valid_credentials},
                                    json={'id': 1})
        self.assertEquals(response.status_code, 200)
        self.assertDictEqual(response.json, {'message': "Education with id [1] deleted"})

    def test_education_not_exist_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.post('/api/delete_education/test',
                                    headers={"Authorization": "Basic " + valid_credentials},
                                    json={'id': 2})
        self.assertEquals(response.status_code, 404)
        self.assertDictEqual(response.json, {'message': "Education with id [2] doesn't exist"})


if __name__ == '__main__':
    unittest.main()
