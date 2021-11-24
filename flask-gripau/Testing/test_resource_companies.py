import base64
import datetime
import unittest

from Testing import BaseTestCase
from db import db
from models import JobSeekersModel, CompanyModel, EducationsModel, WorkExperiencesModel, SkillsModel, ApplicationModel, \
    JobOfferModel


class TestCompaniesResource(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def _add_data(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_education = EducationsModel('Maths phd', 'UB', '2021-09', '2022-10', True)
        new_workexperience = WorkExperiencesModel('professor', 'professor de EDS', 'ub', '2020-03', '2020-06', False)
        new_skill = SkillsModel('python')
        new_company = CompanyModel('universitat123', 'ub', 'ub@gmail.com', 'hola, som la UB')
        new_job_offer = JobOfferModel('professor', 'professor de EDS', datetime.datetime(2021, 4, 7), 'Barcelona', 5000,
                                      8, 'Temporal')
        new_company.hash_password('test')
        new_company.job_offers.append(new_job_offer)
        self._add_data_to_db(new_company)
        new_job_seeker.work_experiences.append(new_workexperience)
        new_job_seeker.educations.append(new_education)
        new_job_seeker.skills.append(new_skill)
        self._add_data_to_db(new_job_seeker)
        new_company2 = CompanyModel('universitat1234', 'ub2', 'ub2@gmail.com', 'hola, som la UB')
        new_company2.hash_password('test')
        self._add_data_to_db(new_company2)

    def test_successful_get(self):
        new_company = CompanyModel('universitat123', 'ub', 'ub@gmail.com', 'hola, som la UB')
        new_company.hash_password('test')
        self._add_data_to_db(new_company)

        response = self.client.get('/api/company/universitat123')
        self.assertEquals(response.status_code, 200)
        self.assertDictEqual(response.json, {'account': new_company.json()})

    def test_failed_get(self):
        response = self.client.get('/api/company/wrong')
        self.assertEquals(response.status_code, 404)
        self.assertDictEqual(response.json, {'account': None})

    def test_access_denied_delete(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'universitat123', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.delete('/api/company/universitat1234', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 401)
        self.assertDictEqual(response.json, {'message': 'Access denied'})

    def test_successful_delete(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'universitat123', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.delete('/api/company/universitat123', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 200)
        self.assertDictEqual(response.json, {'message': 'Account deleted'})

    def test_access_denied_put(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'universitat123', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.put('/api/company/universitat1234', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 401)
        self.assertDictEqual(response.json, {'message': 'Access denied'})

    def test_successful_put(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'universitat123', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.put('/api/company/universitat123',
                                   headers={"Authorization": "Basic " + valid_credentials},
                                   json={
                                       'password': 'Password1234', 'email': 'good@gmail.com', 'description': 'desc',
                                       'sector': 'sector', 'location': 'ub'
                                   })
        self.assertEquals(response.status_code, 200)

    def test_successful_empty_values_put(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'universitat123', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.put('/api/company/universitat123',
                                   headers={"Authorization": "Basic " + valid_credentials},
                                   json={
                                       'password': 'Password1234', 'email': 'good@gmail.com', 'description': 'desc',
                                       'sector': '', 'location': ''
                                   })
        self.assertEquals(response.status_code, 200)

    def test_invalid_password_put(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'universitat123', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.put('/api/company/universitat123',
                                   headers={"Authorization": "Basic " + valid_credentials},
                                   json={
                                       'password': 'invalid'
                                   })
        self.assertEquals(response.status_code, 406)
        self.assertDictEqual(response.json, {'message': "Password invalid! Does not meet requirements"})

    def test_invalid_email_put(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'universitat123', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.put('/api/company/universitat123',
                                   headers={"Authorization": "Basic " + valid_credentials},
                                   json={
                                       'email': 'invalid'
                                   })
        self.assertEquals(response.status_code, 402)
        self.assertDictEqual(response.json, {'message': "Email wrong format!"})

        response = self.client.put('/api/company/universitat123',
                                   headers={"Authorization": "Basic " + valid_credentials},
                                   json={
                                       'email': 'test@hotmail.com'
                                   })
        self.assertEquals(response.status_code, 409)
        self.assertDictEqual(response.json, {'message': "Email already exists"})

        response = self.client.put('/api/company/universitat123',
                                   headers={"Authorization": "Basic " + valid_credentials},
                                   json={
                                       'email': 'ub2@gmail.com'
                                   })
        self.assertEquals(response.status_code, 409)
        self.assertDictEqual(response.json, {'message': "Email already exists"})


if __name__ == '__main__':
    unittest.main()
