from models.job_seeker import JobSeekersModel
from models.education import EducationsModel
from Testing import BaseTestCase
from db import db


class TestJobSeeker(BaseTestCase):

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

    def test_json(self):
        new_job_seeker = JobSeekersModel('test', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        ret = {'id': None, 'username': 'test', 'email': 'test@hotmail.com', 'is_admin': 0,
               'bio': 'hola, soc un test'}
        assert new_job_seeker.json() == ret

    def test_delete_from_db(self):
        new_job_seeker = JobSeekersModel('test', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)
        new_job_seeker.delete_from_db(db)
        result = db.session.query(JobSeekersModel).first()
        self.assertIsNone(result, 'Nothing in the database')

    def test_delete_education(self):
        new_job_seeker = JobSeekersModel('test', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_education = EducationsModel('Maths phd', 'UB', '09-2021', '10-2022', True)
        new_job_seeker.educations.append(new_education)
        new_job_seeker.delete_education(None)
        assert new_job_seeker.educations == []


if __name__ == '__main__':
    import unittest

    unittest.main()