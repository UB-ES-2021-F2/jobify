import base64
import datetime
import unittest

from db import db
from Testing import BaseTestCase
from models import CompanyModel, JobOfferModel


class TestJobOffersResource(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def _add_data(self):
        new_company = CompanyModel('test', 'ub', 'ub@gmail.com', 'hola, som la UB')
        new_job_offer = JobOfferModel('professor', 'professor de EDS', datetime.datetime(2021, 4, 7), 'Barcelona', 5000,
                                      8, 'Temporal')
        new_company.hash_password('test')
        new_company.job_offers.append(new_job_offer)
        self._add_data_to_db(new_company)
        new_company2 = CompanyModel('test2', 'ub2', 'ub2@gmail.com', 'hola, som la UB')
        new_company2.hash_password('test')
        self._add_data_to_db(new_company2)

    def test_successful_get(self):
        new_company = CompanyModel('test', 'ub', 'ub@gmail.com', 'hola, som la UB')
        new_job_offer = JobOfferModel('professor', 'professor de EDS', datetime.datetime(2021, 4, 7), 'Barcelona', 5000,
                                      8, 'Temporal')
        new_company.hash_password('test')
        new_company.job_offers.append(new_job_offer)
        self._add_data_to_db(new_company)

        response = self.client.get('/api/job_offer/1')
        self.assertEquals(response.status_code, 200)
        self.assertDictEqual(response.json, {'offer': new_job_offer.json()})

    def test_failed_get(self):
        response = self.client.get('/api/job_offer/1')
        self.assertEquals(response.status_code, 404)
        self.assertDictEqual(response.json, {'offer': None})

    def test_access_denied_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.post('/api/job_offer/test2', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 401)
        self.assertDictEqual(response.json, {'message': 'Access denied'})

    def test_successful_post(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.post('/api/job_offer/test', headers={"Authorization": "Basic " + valid_credentials},
                                    json={'job_name': 'job', 'location': 'bcn'})
        self.assertEquals(response.status_code, 201)

    def test_access_denied_delete(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test2', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.delete('/api/job_offer/1', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 401)
        self.assertDictEqual(response.json, {'message': 'Access denied'})

    def test_offer_not_exists_delete(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.delete('/api/job_offer/2', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 404)
        self.assertDictEqual(response.json, {'message': "Offer with id [2] don't exists"})

    def test_successful_delete(self):
        self._add_data()

        login = self.client.post('/api/login', json={
            'username': 'test', 'password': 'test'
        })
        token = login.json['token']
        valid_credentials = base64.b64encode(bytes(token+":", 'utf-8')).decode()

        response = self.client.delete('/api/job_offer/1', headers={"Authorization": "Basic " + valid_credentials})
        self.assertEquals(response.status_code, 200)
        self.assertDictEqual(response.json, {'message': "Offer with id [1] deleted"})


if __name__ == '__main__':
    unittest.main()
