from db import db


class WorkExperiencesModel(db.Model):
    __tablename__ = 'work_experiences'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), db.ForeignKey('jobseekers.username'), nullable=False)
    job_name = db.Column(db.String(128), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=False)
    company = db.Column(db.String(128), unique=False, nullable=False)
    start_date = db.Column(db.String(7), unique=False, nullable=False)
    end_date = db.Column(db.String(7), unique=False, nullable=False)
    currently = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, job_name, description, company, start_date,end_date, currently):
        self.job_name = job_name
        self.description = description
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.currently = currently

    def json(self):
        return {'id': self.id, 'username': self.username, 'job_name': self.job_name, 'description': self.description,
                'company': self.company,
                'start_date': self.start_date, 'end_date': self.end_date,'currently': self.currently}

    def delete_from_db(self, database=None):
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def show_work_experiences(cls):
        return {'work_experiences': [work_experience.json() for work_experience in cls.query.all()]}