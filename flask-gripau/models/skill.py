from db import db


class SkillsModel(db.Model):
    """
    Model of a skill.
    Job Seeker 1 ---> * Skill
    """
    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), db.ForeignKey('jobseekers.username'), nullable=False)
    name = db.Column(db.String(15), unique=False, nullable=False)

    def __init__(self, name):
        """
        Initializer of a skill
        :param name: name of the skill
        """
        self.name = name

    def json(self):
        """
        Function that returns the skill info as json
        :return: json object with the information
        """
        return {'id': self.id, 'username': self.username, 'name': self.name}

    def delete_from_db(self, database=None):
        """
        Function that the deletes from the database the skill
        :param database: database instance
        """
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_by_username_and_name(cls, username, name):
        """
        Function that finds the skill by username and name
        :param username: username of the job seeker
        :param name: name of the skill
        :return: the skill
        """
        return cls.query.filter_by(username=username, name=name).first()