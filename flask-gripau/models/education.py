from db import db


class EducationsModel(db.Model):
    """
    Model of a education.
    Job Seeker 1 ---> * Educations
    """
    __tablename__ = 'educations'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), db.ForeignKey('jobseekers.username'), nullable=False)
    title = db.Column(db.String(128), unique=False, nullable=False)
    institution = db.Column(db.String(128), unique=False, nullable=False)
    start_date = db.Column(db.String(7), unique=False, nullable=False)
    end_date = db.Column(db.String(7), unique=False, nullable=False)
    currently = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, title, institution, start_date, end_date, currently):
        """
        Initializer of a education
        :param title: title of the education
        :param institution: institution where the education was studied
        :param start_date: start date of the education
        :param end_date: end date of the education
        :param currently: if the job seeker is currently studying the education, 1 (yes) / 0 (no)
        """
        self.title = title
        self.institution = institution
        self.start_date = start_date
        self.end_date = end_date
        self.currently = currently

    def json(self):
        """
        Function that returns the education info as json
        :return: json object with the information
        """
        return {'id': self.id, 'username': self.username, 'title': self.title, 'institution': self.institution,
                'start_date': self.start_date, 'end_date': self.end_date,'currently': self.currently}

    def delete_from_db(self, database=None):
        """
        Function that the deletes from the database the education
        :param database: database instance
        """
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def show_educations(cls):
        """
        Function that shows all the educations in the database
        :return: list of the educations
        """
        return [education.json() for education in cls.query.all()]

