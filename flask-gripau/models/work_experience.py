from db import db


class WorkExperiencesModel(db.Model):
    """Model of a work experience.
    Job Seeker 1 ---> * Work experiences

    Args:

    Returns:

    """
    __tablename__ = 'work_experiences'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), db.ForeignKey('jobseekers.username'), nullable=False)
    job_name = db.Column(db.String(128), unique=False, nullable=False)
    description = db.Column(db.String(5000), unique=False, nullable=False)
    company = db.Column(db.String(128), unique=False, nullable=False)
    start_date = db.Column(db.String(7), unique=False, nullable=False)
    end_date = db.Column(db.String(7), unique=False, nullable=True)
    currently = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, job_name, description, company, start_date, end_date, currently):
        """
        Initializer of a work experience
        :param job_name: name of the job
        :param description: description of the job
        :param company: company where the job was done
        :param start_date: start date of the work experience
        :param end_date: end date of the work experience
        :param currently: if the job seeker is currently working on this job
        """
        self.job_name = job_name
        self.description = description
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.currently = currently

    def json(self):
        """Function that returns the work experience info as json
        :return: json object with the information

        Args:

        Returns:

        """
        return {'id': self.id, 'username': self.username, 'job_name': self.job_name, 'description': self.description,
                'company': self.company,
                'start_date': self.start_date, 'end_date': self.end_date, 'currently': self.currently}

    def delete_from_db(self, database=None):
        """Function that the deletes from the database the work experience

        Args:
          database: database instance (Default value = None)

        Returns:

        """
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def show_work_experiences(cls):
        """Function that shows all the work experiences in the database
        :return: list of the work experiences

        Args:

        Returns:

        """
        return [work_experience.json() for work_experience in cls.query.all()]
