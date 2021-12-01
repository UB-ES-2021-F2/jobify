from datetime import datetime
from models import JobSeekersModel, ApplicationModel, CompanyModel, JobOfferModel
from Testing import BaseTestCase
from db import db


class TestApplication(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def test_add_application(self):
        new_application = ApplicationModel()
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_job_seeker.applications.append(new_application)
        new_company = CompanyModel('username', 'test', 'test@test.com', 'test')
        new_company.hash_password('test')
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        new_company.job_offers.append(new_job_offer)
        new_job_offer.applications.append(new_application)
        self._add_data_to_db(new_job_seeker)
        self._add_data_to_db(new_company)
        result = db.session.query(ApplicationModel).first()
        self.assertIsNotNone(result, 'Nothing in the database')
        self.assertTrue(result.json()['job_seeker_username'] == 'test')
        self.assertTrue(result.json()['job_offer_name'] == 'test')

    def test_json(self):
        new_application = ApplicationModel('test')
        ret = {'id': None, 'job_seeker_username': None, 'job_offer_id': None,
               'job_offer_name': None, 'job_offer_company': None, 'info': 'test'}
        assert new_application.json() == ret

    def test_delete_from_db(self):
        new_application = ApplicationModel()
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_job_seeker.applications.append(new_application)
        new_company = CompanyModel('username', 'test', 'test@test.com', 'test')
        new_company.hash_password('test')
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        new_company.job_offers.append(new_job_offer)
        new_job_offer.applications.append(new_application)
        self._add_data_to_db(new_job_seeker)
        self._add_data_to_db(new_company)
        new_application.delete_from_db()
        result = db.session.query(ApplicationModel).first()
        self.assertIsNone(result, 'Nothing in the database')

    def test_find_by_job_seeker_username(self):
        new_application = ApplicationModel()
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_job_seeker.applications.append(new_application)
        new_company = CompanyModel('username', 'test', 'test@test.com', 'test')
        new_company.hash_password('test')
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        new_company.job_offers.append(new_job_offer)
        new_job_offer.applications.append(new_application)
        self._add_data_to_db(new_job_seeker)
        self._add_data_to_db(new_company)
        result = ApplicationModel.find_by_job_seeker_username('test')
        assert result == [new_application]

    def test_find_by_job_offer_id(self):
        new_application = ApplicationModel()
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_job_seeker.applications.append(new_application)
        new_company = CompanyModel('username', 'test', 'test@test.com', 'test')
        new_company.hash_password('test')
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        new_company.job_offers.append(new_job_offer)
        new_job_offer.applications.append(new_application)
        self._add_data_to_db(new_job_seeker)
        self._add_data_to_db(new_company)
        result = ApplicationModel.find_by_job_offer_id(new_job_offer.id)
        assert result == [new_application]

    def test_show_applications(self):
        new_application = ApplicationModel()
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_job_seeker.applications.append(new_application)
        new_company = CompanyModel('username', 'test', 'test@test.com', 'test')
        new_company.hash_password('test')
        new_job_offer = JobOfferModel('test', 'test', datetime.strptime('2021-07-04', "%Y-%m-%d"), 'test')
        new_company.job_offers.append(new_job_offer)
        new_job_offer.applications.append(new_application)
        self._add_data_to_db(new_job_seeker)
        self._add_data_to_db(new_company)
        result = ApplicationModel.show_applications()
        assert result == [new_application.json()]


if __name__ == '__main__':
    import unittest

    unittest.main()
