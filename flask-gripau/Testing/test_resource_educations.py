import base64
import datetime
import unittest

from Testing import BaseTestCase
from db import db
from models import JobSeekersModel, CompanyModel, EducationsModel, WorkExperiencesModel, SkillsModel, ApplicationModel, \
    JobOfferModel


class TestEducationsResource(BaseTestCase):

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

    def test_successful_get(self):
        self._add_data()

        response = self.client.get('/api/education/test')
        self.assertEquals(response.status_code, 200)

    def test_failed_get(self):
        self._add_data()

        response = self.client.get('/api/education/test2')
        self.assertEquals(response.status_code, 404)
        self.assertDictEqual(response.json, {"education": None})

    def test_access_denied_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.post('/api/education/test2', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 401)
        self.assertDictEqual(response.json, {'message': 'Access denied'})

    def test_title_space_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': ' ',
                                          'institution': 'ub',
                                          'start_date': '2000-1',
                                          'end_date': '2000-2',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Title cannot be blank"})

    def test_end_date_required_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2000-1',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "End date is required if \"currently\" is false"})

    def test_dates_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '20001',
                                          'end_date': '39',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Date format is wrong, try (yyyy-mm)"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2000-a1',
                                          'end_date': '39',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Date format is wrong, try (yyyy-mm)"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2200-01',
                                          'end_date': '39',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Dates need to be between years 1900 and 2100"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2000-13',
                                          'end_date': '39',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Dates need to be between months 1 and 12"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2030-01',
                                          'end_date': '39',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Start date cannot be posterior to current date"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2010-01',
                                          'end_date': '39',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Date format is wrong, try (yyyy-mm)"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2010-01',
                                          'end_date': '39-a',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Date format is wrong, try (yyyy-mm)"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2010-01',
                                          'end_date': '1800-02',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Dates need to be between years 1900 and 2100"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2010-01',
                                          'end_date': '1901-20',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Dates need to be between months 1 and 12"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2010-01',
                                          'end_date': '2009-04',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Start date cannot be posterior than end date"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2010-02',
                                          'end_date': '2010-01',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "Start date cannot be posterior than end date"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2010-02',
                                          'end_date': '2010-03',
                                          'currently': True})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "End date cannot be previous to current date if \"currently\" "
                                                        "is true"})

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2010-02',
                                          'end_date': '2099-12',
                                          'currently': False})

        self.assertEquals(response.status_code, 400)
        self.assertDictEqual(response.json, {"message": "End date cannot be posterior to current date if \"currently\" "
                                                        "is false"})

    def test_successful_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token + ":", 'utf-8')).decode()

        response = self.client.post('/api/education/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'title': 'title',
                                          'institution': 'ub',
                                          'start_date': '2000-01',
                                          'end_date': '2000-02',
                                          'currently': False})

        self.assertEquals(response.status_code, 200)
        self.assertDictEqual(response.json, {"education": {'id': 2, 'username': 'test', 'title': 'title',
                                                           'institution': 'ub', 'start_date': '2000-01',
                                                           'end_date': '2000-02', 'currently': False}})


if __name__ == '__main__':
    unittest.main()
