from datetime import datetime

from models.job_offer import JobOfferModel
from models.company import CompanyModel
from Testing import BaseTestCase
from db import db


class TestJobOffer(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def test_add_job_offer(self):
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        new_company = CompanyModel('test', 'test@test.com', 'test')
        new_company.hash_password('test')
        new_company.job_offers.append(new_job_offer)
        self._add_data_to_db(new_company)
        result = db.session.query(JobOfferModel).first()
        self.assertIsNotNone(result, 'Nothing in the database')
        self.assertTrue(result.json()['company'] == 'test')

    def test_json(self):
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        ret = {'id': None, 'company': None, 'job_name': 'test',
               'description': 'test', 'publication_date': datetime.strptime('2021-07-04', "%Y-%m-%d"),
               'salary': 0, 'vacancy_number': 0, 'location': 'test',
               'working_hours': 'FLEXIBLE', 'minimum_experience': 0}
        assert new_job_offer.json() == ret

    def test_delete_from_db(self):
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        new_company = CompanyModel('test', 'test@test.com', 'test')
        new_company.hash_password('test')
        new_company.job_offers.append(new_job_offer)
        self._add_data_to_db(new_company)
        new_job_offer.delete_from_db()
        result = db.session.query(JobOfferModel).first()
        self.assertIsNone(result, 'Nothing in the database')


if __name__ == '__main__':
    import unittest

    unittest.main()
