import base64
import datetime
import unittest

from Testing import BaseTestCase
from db import db
from models import JobSeekersModel, CompanyModel, EducationsModel, WorkExperiencesModel, SkillsModel, ApplicationModel, \
    JobOfferModel


class TestApplicationsResource(BaseTestCase):

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
        new_application = ApplicationModel()
        new_application.job_offer_id = 1
        new_application.job_seeker_username = 'test'
        new_company = CompanyModel('universitat123', 'ub', 'ub@gmail.com', 'hola, som la UB')
        new_job_offer = JobOfferModel('professor', 'professor de EDS', datetime.datetime(2021, 4, 7), 'Barcelona', 5000,
                                      8, 'Temporal')
        new_company.hash_password('Password12')
        new_company.job_offers.append(new_job_offer)
        self._add_data_to_db(new_company)
        new_job_offer.applications.append(new_application)
        new_job_seeker.work_experiences.append(new_workexperience)
        new_job_seeker.educations.append(new_education)
        new_job_seeker.skills.append(new_skill)
        new_job_seeker.applications.append(new_application)
        self._add_data_to_db(new_job_seeker)
        self._add_data_to_db(new_application)
        new_job_seeker2 = JobSeekersModel('test2', 'Sergi', 'Bech', 'test@gmail.com', 'hola, soc un test')
        new_job_seeker2.hash_password('test')
        self._add_data_to_db(new_job_seeker2)

    def test_successful_get(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.get('/api/application/test/1', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 200)

    def test_failed_get(self):
        self._add_data()
        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.get('/api/application/test/7', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 404)
        self.assertDictEqual(response.json, {"application": None})

    def test_access_denied_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.post('/api/application/test2', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {'message': 'Access denied'})

    def test_job_offer_not_exist_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.post('/api/application/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'job_offer_id': 7})

        self.assertEquals(response.status_code, 404)
        self.assertDictEqual(response.json, {"message": "The user or the job offer doesn't exist."})

    def test_successful_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test2', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.post('/api/application/test2', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'job_offer_id': 1, 'info': 'info'})

        self.assertEquals(response.status_code, 200)




if __name__ == '__main__':
    unittest.main()
