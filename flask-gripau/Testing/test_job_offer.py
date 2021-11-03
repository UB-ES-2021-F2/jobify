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
        new_company = CompanyModel('username','test', 'test@test.com', 'test')
        new_company.hash_password('test')
        new_company.job_offers.append(new_job_offer)
        self._add_data_to_db(new_company)
        result = db.session.query(JobOfferModel).first()
        self.assertIsNotNone(result, 'Nothing in the database')
        self.assertTrue(result.json()['company_name'] == 'test')

    def test_json(self):
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        ret = {'id': None, 'company_name': '', 'company': None, 'job_name': 'test',
               'description': 'test', 'publication_date': '2021-07-04',
               'salary': None, 'location': 'test', 'contract_type': None,
               'working_hours': None}
        assert new_job_offer.json() == ret

    def test_save_to_db_and_delete_from_db(self):
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        new_company = CompanyModel('username', 'test', 'test@test.com', 'test')
        new_company.hash_password('test')
        self._add_data_to_db(new_company)
        new_job_offer.company = new_company.company
        new_job_offer.save_to_db()
        self.assertTrue(new_job_offer in db.session)
        new_job_offer.delete_from_db()
        self.assertTrue(new_job_offer not in db.session)

    def test_find_by_id(self):
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        new_company = CompanyModel('username', 'test', 'test@test.com', 'test')
        new_company.hash_password('test')
        self._add_data_to_db(new_company)
        new_job_offer.company = new_company.company
        new_job_offer.save_to_db()
        find = JobOfferModel.find_by_id(1)
        assert find == new_job_offer

    def test_show_offers(self):
        self.assertEquals([], JobOfferModel.show_job_offers())
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        new_company = CompanyModel('username','test', 'test@test.com', 'test')
        new_company.hash_password('test')
        self._add_data_to_db(new_company)
        new_job_offer.company = new_company.company
        new_job_offer.save_to_db()
        self.assertEquals([new_job_offer.json()], JobOfferModel.show_job_offers())


if __name__ == '__main__':
    import unittest

    unittest.main()
