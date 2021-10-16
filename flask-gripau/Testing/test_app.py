from models.job_seeker import JobSeekersModel
from Testing import BaseTestCase
from db import db


class TestApp(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def test_add_jobseeker(self):
        new_job_seeker = JobSeekersModel('test', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)
        result = db.session.query(JobSeekersModel).first()
        self.assertIsNotNone(result, 'Nothing in the database')

    def test_find_by_username(self):
        new_job_seeker = JobSeekersModel('test', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)
        find = JobSeekersModel.find_by_username('test')
        assert find.json()['username'] == 'test'


if __name__ == '__main__':
    import unittest

    unittest.main()
