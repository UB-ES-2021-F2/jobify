import base64
import datetime
import unittest

from Testing import BaseTestCase
from db import db
from models import JobSeekersModel, CompanyModel, EducationsModel, WorkExperiencesModel, SkillsModel, ApplicationModel, \
    JobOfferModel


class TestCompanyJobOffersResource(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def _add_data(self):
        new_company = CompanyModel('universitat123', 'ub', 'ub@gmail.com', 'hola, som la UB')
        new_company.hash_password('Password12')
        self._add_data_to_db(new_company)

    def test_successful_get(self):
        self._add_data()

        response = self.client.get('/api/offers/universitat123')
        self.assertEquals(response.status_code, 200)

    def test_failed_get(self):
        response = self.client.get('/api/offers/universitat123')
        self.assertEquals(response.status_code, 404)
        self.assertDictEqual(response.json, {'Company': None})


if __name__ == '__main__':
    unittest.main()
