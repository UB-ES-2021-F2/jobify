import base64
import datetime
import unittest

from Testing import BaseTestCase
from db import db
from models import JobSeekersModel, CompanyModel, EducationsModel, WorkExperiencesModel, SkillsModel, ApplicationModel, \
    JobOfferModel


class TestJobOfferApplicantsResource(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def _add_data(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_company = CompanyModel('universitat123', 'ub', 'ub@gmail.com', 'hola, som la UB')
        new_company.hash_password('Password12')
        new_job_offer = JobOfferModel('professor', 'professor de EDS', datetime.datetime(2021, 4, 7), 'Barcelona', 5000,
                                              8, 'Temporal')
        new_company.job_offers.append(new_job_offer)
        new_job_offer_2 = JobOfferModel('teacher', 'test de EDS', datetime.datetime(2021, 4, 7), 'Barcelona', 5000,
                                              8, 'Temporal')
        new_company.job_offers.append(new_job_offer_2)
        new_application = ApplicationModel()
        new_job_seeker.applications.append(new_application)
        new_job_offer.applications.append(new_application)
        self._add_data_to_db(new_company)
        self._add_data_to_db(new_job_seeker)
        new_job_seeker2 = JobSeekersModel('test2', 'Sergi', 'Bech', 'test2@hotmail.com', 'hola, soc un test')
        new_job_seeker2.hash_password('test')
        self._add_data_to_db(new_job_seeker2)

    def test_successful_get(self):
        self._add_data()
        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.get('/api/applications/test', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 200)

    def test_failed_get(self):
        self._add_data()
        login = self.client.post('/api/login', json={
            'username': 'test2', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()
        response = self.client.get('/api/applications/test2', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 404)
        self.assertDictEqual(response.json, {'message': "There are no applications of the user [test2]"})

    def test_access_denied(self):
        self._add_data()
        login = self.client.post('/api/login', json={
            'username': 'test2', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()
        response = self.client.get('/api/applications/test', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 401)
        self.assertDictEqual(response.json, {'message': "Access denied"})

if __name__ == '__main__':
    unittest.main()
