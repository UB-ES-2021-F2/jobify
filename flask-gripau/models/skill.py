from db import db


class SkillsModel(db.Model):
    """Model of a skill.
    Job Seeker 1 ---> * Skill

    Args:

    Returns:

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

    def skill_name(self):
        return self.name

    def json(self):
        """Function that returns the skill info as json
        :return: json object with the information

        Args:

        Returns:

        """
        return {'id': self.id, 'username': self.username, 'name': self.name}

    def delete_from_db(self, database=None):
        """Function that the deletes from the database the skill

        Args:
          database: database instance (Default value = None)

        Returns:

        """
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_by_username_and_name(cls, username, name):
        """Function that finds the skill by username and name

        Args:
          username: username of the job seeker
          name: name of the skill

        Returns:
          : the skill

        """
        return cls.query.filter_by(username=username, name=name).first()