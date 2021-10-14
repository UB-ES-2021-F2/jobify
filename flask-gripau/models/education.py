from db import db


class EducationModel(db.Model):
    __tablename__ = 'educations'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), db.ForeignKey('jobseekers.username'), nullable=False)
    title = db.Column(db.String(128), unique=False, nullable=False)
    institution = db.Column(db.String(128), unique=False, nullable=False)
    start_date = db.Column(db.String(7), unique=False, nullable=False)
    end_date = db.Column(db.String(7), unique=False, nullable=False)
    currently = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, username, title, institution, start_date, end_date, currently):
        self.username = username
        self.title = title
        self.institution = institution
        self.start_date = start_date
        self.end_date = end_date
        self.currently = currently

    def json(self):
        return {'username': self.username, 'title': self.title, 'insitution': self.institution,
                'start_date': self.start_date, 'end_date': self.end_date,'currently': self.currently}

    def delete_from_db(self, database=None):
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def show_educations(cls):
        return {'educations': [education.json() for education in cls.query.all()]}
