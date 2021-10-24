from datetime import datetime

from models import JobSeekersModel
from models.skill import SkillsModel
from models.job_seeker import JobSeekersModel
from Testing import BaseTestCase
from db import db


class TestSkill(BaseTestCase):

    def _add_data_to_db(self, data):
        db.session.add(data)
        db.session.commit()
        self.assertTrue(data in db.session)

    def test_add_skill(self):
        new_skill = SkillsModel('test')
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech','test@test.com', 'test')
        new_job_seeker.hash_password('test')
        new_job_seeker.skills.append(new_skill)
        self._add_data_to_db(new_job_seeker)
        result = db.session.query(SkillsModel).first()
        self.assertIsNotNone(result, 'Nothing in the database')
        self.assertTrue(result.json()['username'] == 'test')

    def test_json(self):
        new_skill = SkillsModel('test')
        ret = {'id': None, 'username': None, 'name': 'test'}
        assert new_skill.json() == ret

    def test_delete_from_db(self):
        new_skill = SkillsModel('test')
        new_job_seeker = JobSeekersModel('test', 'Sergi', 'Bech', 'sergi@gmail.com', 'hola, soc un test')
        new_job_seeker.hash_password('test')
        new_job_seeker.skills.append(new_skill)
        self._add_data_to_db(new_job_seeker)
        new_skill.delete_from_db()
        result = db.session.query(SkillsModel).first()
        self.assertIsNone(result, 'Nothing in the database')


if __name__ == '__main__':
    import unittest

    unittest.main()
