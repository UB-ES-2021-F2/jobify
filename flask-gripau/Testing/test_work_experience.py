from datetime import datetime

from models import JobSeekersModel, WorkExperiencesModel
from models.skill import SkillsModel
from models.job_seeker import JobSeekersModel
from Testing import BaseTestCase
from db import db


class TestWorkExperience(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def test_add_work_experience(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_work_experience = WorkExperiencesModel('QA Tester', 'test', 'Jobify', '10-2020', '10-2021', True)
        new_job_seeker.work_experiences.append(new_work_experience)
        self._add_data_to_db(new_job_seeker)
        result = db.session.query(WorkExperiencesModel).first()
        self.assertIsNotNone(result, 'Nothing in the database')
        self.assertTrue(result.json()['username'] == 'test')

    def test_json(self):
        new_work_experience = WorkExperiencesModel('QA Tester', 'test', 'Jobify', '10-2020', '10-2021', True)
        ret = {'id': None, 'username': None, 'job_name': 'QA Tester', 'description': 'test',
               'company': 'Jobify',
               'start_date': '10-2020', 'end_date': '10-2021', 'currently': True}
        assert new_work_experience.json() == ret

    def test_delete_from_db(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_work_experience = WorkExperiencesModel('QA Tester', 'test', 'Jobify', '10-2020', '10-2021', True)
        new_job_seeker.work_experiences.append(new_work_experience)
        self._add_data_to_db(new_job_seeker)
        new_work_experience.delete_from_db()
        result = db.session.query(WorkExperiencesModel).first()
        self.assertIsNone(result, 'Nothing in the database')

    def test_show_work_experiences(self):
        self.assertEquals([], WorkExperiencesModel.show_work_experiences())
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_work_experience = WorkExperiencesModel('QA Tester', 'test', 'Jobify', '10-2020', '10-2021', True)
        new_job_seeker.work_experiences.append(new_work_experience)
        self._add_data_to_db(new_job_seeker)
        self.assertEquals([new_work_experience.json()], WorkExperiencesModel.show_work_experiences())


if __name__ == '__main__':
    import unittest

    unittest.main()
