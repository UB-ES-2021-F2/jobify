import base64
import datetime
import unittest

from Testing import BaseTestCase
from db import db
from models import JobSeekersModel, CompanyModel, EducationsModel, WorkExperiencesModel, SkillsModel, ApplicationModel, \
    JobOfferModel


class TestCompanyListResource(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def _add_data(self):
        new_company = CompanyModel('universitat123', 'ub', 'ub@gmail.com', 'hola, som la UB')
        new_company.hash_password('Password12')
        self._add_data_to_db(new_company)

        new_company = CompanyModel('test123', 'company test', 'test@companytest.com', 'hola, som una empresa de test')
        new_company.hash_password('Password12')
        self._add_data_to_db(new_company)

        new_company = CompanyModel('123test', 'test segon', 'testdos@companytest.com', 'hola, som una altra empresa de test')
        new_company.hash_password('Password12')
        self._add_data_to_db(new_company)

    def test_successful_get(self):
        self._add_data()

        response = self.client.get('/api/companies')
        self.assertEquals(response.status_code, 200)

    def test_successful_get_empty(self):
        response = self.client.get('/api/companies')
        self.assertEquals(len(response.json), 0)
        self.assertEquals(response.status_code, 200)

    def test_successful_get_test(self):
        self._add_data()

        response = self.client.get('/api/companies', json={'keyword': 'test'})
        self.assertEquals(len(response.json), 2)
        self.assertEquals(response.status_code, 200)

    def test_successful_get_companytest(self):
        self._add_data()

        response = self.client.get('/api/companies', json={'keyword': 'company test'})
        self.assertEquals(len(response.json), 1)
        self.assertEquals(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
