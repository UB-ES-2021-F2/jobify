from models.company import CompanyModel, get_user_roles
from models.job_seeker import JobSeekersModel
from models.education import EducationsModel
from models.work_experience import WorkExperiencesModel
from Testing import BaseTestCase
from db import db


class TestJobSeeker(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def test_add_company(self):
        new_company = CompanyModel('test', 'test@test.com', 'test')
        new_company.hash_password('test')
        self._add_data_to_db(new_company)
        result = db.session.query(CompanyModel).first()
        self.assertIsNotNone(result, 'Nothing in the database')

    def test_find_by_company(self):
        new_company = CompanyModel('test', 'test@test.com', 'test')
        new_company.hash_password('test')
        self._add_data_to_db(new_company)
        find = CompanyModel.find_by_company('test')
        assert find.json()['company'] == 'test'

    def test_json(self):
        new_company = CompanyModel('test', 'test@test.com', 'test')
        new_company.hash_password('test')
        ret = {'id': None, 'company': 'test', 'email': 'test@test.com', 'is_admin': 0,
               'description': 'test', 'sector': 'Unknown', 'location': 'Unknown'}
        assert new_company.json() == ret

    def test_save_to_db_and_delete_from_db(self):
        new_company = CompanyModel('test', 'test@test.com', 'test')
        new_company.hash_password('test')
        new_company.save_to_db()
        self.assertTrue(new_company in db.session)
        new_company.delete_from_db()
        self.assertTrue(new_company not in db.session)

    def test_hash_password_and_verify_password(self):
        new_company = CompanyModel('test', 'test@test.com', 'test')
        new_company.hash_password('test')
        self.assertTrue(new_company.verify_password('test'))

    def test_find_by_email(self):
        new_company = CompanyModel('test', 'test@test.com', 'test')
        new_company.hash_password('test')
        self._add_data_to_db(new_company)
        find = CompanyModel.find_by_email('test@test.com')
        assert find.json()['email'] == 'test@test.com'

    def test_show_accounts(self):
        self.assertEquals([], CompanyModel.show_accounts())
        new_company = CompanyModel('test', 'test@test.com', 'test')
        new_company.hash_password('test')
        self._add_data_to_db(new_company)
        self.assertEquals([new_company.json()], CompanyModel.show_accounts())

    def test_get_user_roles(self):
        new_company = CompanyModel('test', 'test@test.com', 'test')
        assert get_user_roles(new_company) == ['user']
        new_company.is_admin = 1
        assert get_user_roles(new_company) == ['admin']


if __name__ == '__main__':
    import unittest

    unittest.main()
