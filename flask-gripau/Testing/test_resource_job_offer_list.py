import base64
import datetime
import unittest

from Testing import BaseTestCase
from db import db
from models import JobSeekersModel, CompanyModel, EducationsModel, WorkExperiencesModel, SkillsModel, ApplicationModel, \
    JobOfferModel


class TestJobOfferListResource(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def _add_data(self):
        new_company = CompanyModel('universitat123', 'ub', 'ub@gmail.com', 'hola, som la UB')
        new_company.hash_password('Password12')
        new_job_offer = JobOfferModel('professor', 'professor de EDS', datetime.datetime(2021, 4, 7), 'Barcelona', 5000,
                                      8, 'Temporal')
        new_company.job_offers.append(new_job_offer)
        self._add_data_to_db(new_company)

    def test_successful_get(self):
        self._add_data()

        response = self.client.get('/api/offers')
        self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
