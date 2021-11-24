from models import ApplicationModel
from models.job_seeker import JobSeekersModel, get_user_roles, verify_password
from models.education import EducationsModel
from models.work_experience import WorkExperiencesModel
from Testing import BaseTestCase
from db import db


class TestJobSeeker(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def test_add_jobseeker(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)
        result = db.session.query(JobSeekersModel).first()
        self.assertIsNotNone(result, 'Nothing in the database')

    def test_find_by_username(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)
        find = JobSeekersModel.find_by_username('test')
        assert find.json()['username'] == 'test'
        find = JobSeekersModel.find_by_username('')
        assert find is None

    def test_json(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        ret = {'id': None, 'username': 'test', "name": "Sergi", "surname": "Bech", 'email': 'test@hotmail.com',
               'is_admin': 0,
               'bio': 'hola, soc un test', "educations": [], "work_experiences": [], "skills": [],
               'applications': []}
        assert new_job_seeker.json() == ret

    def test_delete_from_db(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)
        new_job_seeker.delete_from_db(db)
        result = db.session.query(JobSeekersModel).first()
        self.assertIsNone(result, 'Nothing in the database')

    def test_delete_education(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_education = EducationsModel('Maths phd', 'UB', '09-2021', '10-2022', True)
        new_job_seeker.educations.append(new_education)
        new_job_seeker.delete_education(None)
        assert new_job_seeker.educations == []
        self.assertIsNone(new_job_seeker.delete_education(1233))

    def test_delete_work_experience(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_work_experience = WorkExperiencesModel('QA Tester', 'test', 'Jobify', '10-2020', '10-2021', True)
        new_job_seeker.work_experiences.append(new_work_experience)
        new_job_seeker.delete_work_experience(None)
        assert new_job_seeker.work_experiences == []
        self.assertIsNone(new_job_seeker.delete_work_experience(1233))

    def test_delete_application(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_application = ApplicationModel()
        new_job_seeker.applications.append(new_application)
        assert len(new_job_seeker.applications) == 1
        new_job_seeker.delete_application(None)
        assert new_job_seeker.applications == []
        self.assertIsNone(new_job_seeker.delete_application(1233))

    def test_save_to_db_and_delete_from_db(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_job_seeker.save_to_db()
        self.assertTrue(new_job_seeker in db.session)
        new_job_seeker.delete_from_db()
        self.assertTrue(new_job_seeker not in db.session)

    def test_hash_password_and_verify_password(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self.assertTrue(new_job_seeker.verify_password('test'))

    def test_find_by_email(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)
        find = JobSeekersModel.find_by_email('test@hotmail.com')
        assert find.json()['email'] == 'test@hotmail.com'

    def test_show_accounts(self):
        self.assertEquals([], JobSeekersModel.show_accounts())
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)
        self.assertEquals([new_job_seeker.json()], JobSeekersModel.show_accounts())

    def test_get_user_roles(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        assert get_user_roles(new_job_seeker) == ['user']
        new_job_seeker.is_admin = 1
        assert get_user_roles(new_job_seeker) == ['admin']

    def test_generate_auth_token_valid(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)
        token = new_job_seeker.generate_auth_token().decode('ascii')
        self.assertTrue(JobSeekersModel.verify_auth_token(token))

    def test_generate_auth_token_expired(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)
        token = new_job_seeker.generate_auth_token(expiration=-1).decode('ascii')
        self.assertIsNone(JobSeekersModel.verify_auth_token(token))

    def test_verify_auth_token_bad_signature(self):
        self.assertIsNone(JobSeekersModel.verify_auth_token('illegal_token'))

    def test_auth_verify_password(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        self._add_data_to_db(new_job_seeker)
        token = new_job_seeker.generate_auth_token().decode('ascii')
        self.assertEquals(new_job_seeker, verify_password(token, None))


if __name__ == '__main__':
    import unittest

    unittest.main()
