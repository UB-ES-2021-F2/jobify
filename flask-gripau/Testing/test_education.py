from datetime import datetime

from models import JobSeekersModel, WorkExperiencesModel, EducationsModel
from models.skill import SkillsModel
from models.job_seeker import JobSeekersModel
from Testing import BaseTestCase
from db import db


class TestEducation(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def test_add_education(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_education = EducationsModel('Maths phd', 'UB', '09-2021', '10-2022', True)
        new_job_seeker.educations.append(new_education)
        self._add_data_to_db(new_job_seeker)
        result = db.session.query(EducationsModel).first()
        self.assertIsNotNone(result, 'Nothing in the database')
        self.assertTrue(result.json()['username'] == 'test')

    def test_json(self):
        new_education = EducationsModel('Maths phd', 'UB', '09-2021', '10-2022', True)
        ret = {'id': None, 'username': None, 'title': 'Maths phd', 'institution': 'UB',
               'start_date': '09-2021', 'end_date': '10-2022', 'currently': True}
        assert new_education.json() == ret

    def test_delete_from_db(self):
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_education = EducationsModel('Maths phd', 'UB', '09-2021', '10-2022', True)
        new_job_seeker.educations.append(new_education)
        self._add_data_to_db(new_job_seeker)
        new_education.delete_from_db()
        result = db.session.query(EducationsModel).first()
        self.assertIsNone(result, 'Nothing in the database')

    def test_show_educations(self):
        self.assertEquals([], EducationsModel.show_educations())
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'test@hotmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_education = EducationsModel('Maths phd', 'UB', '09-2021', '10-2022', True)
        new_job_seeker.educations.append(new_education)
        self._add_data_to_db(new_job_seeker)
        self.assertEquals([new_education.json()], EducationsModel.show_educations())


if __name__ == '__main__':
    import unittest

    unittest.main()
