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

        new_company_2 = CompanyModel('test24', 'test test', 'testing@gmail.com', 'hola, som tests')
        new_company_2.hash_password('Password12')
        new_job_offer_2 = JobOfferModel('professor adjunt', 'professor adjunt de EDS', datetime.datetime(2021, 4, 7), 'Barcelona', 5000,
                                              8, 'Temporal')
        new_job_offer_3 = JobOfferModel('professora de musica', 'professor de musica de violi', datetime.datetime(2021, 4, 7), 'Barcelona', 5000,
                                            8, 'Temporal')
        new_company_2.job_offers.append(new_job_offer_2)
        new_company_2.job_offers.append(new_job_offer_3)
        self._add_data_to_db(new_company_2)

    def test_successful_get_without_name(self):
        self._add_data()

        response = self.client.get('/api/offers')
        self.assertEquals(response.status_code, 200)

    def test_successful_get_with_keyword_professor(self):
        self._add_data()

        response = self.client.get('/api/offers',json={'keyword': 'professor'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.json['OfferList']), 3)

    def test_successful_get_with_keyword_adjunt(self):
        self._add_data()

        response = self.client.get('/api/offers',json={'keyword': 'adjunt'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.json['OfferList']), 1)

    def test_successful_get_with_keyword_test(self):
        self._add_data()

        response = self.client.get('/api/offers',json={'keyword': 'test'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.json['OfferList']), 2)
    def test_successful_get_with_two_keywords(self):
            self._add_data()

            response = self.client.get('/api/offers',json={'keyword': 'professor musica'})
            self.assertEquals(response.status_code, 200)
            self.assertEquals(len(response.json['OfferList']), 1)
if __name__ == '__main__':
    unittest.main()
