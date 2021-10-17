from db import db

working_hours_types = ('FULL_TIME', 'MORNING', 'AFTERNOON', 'NIGHT', 'FLEXIBLE')
contract_types = ('INDEFINITE', 'DETERMINED_DURATION', 'STAND_ALONE', 'PART_TIME', 'TRAINING')


class JobOfferModel(db.Model):
    __tablename__ = 'job_offer'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(30), db.ForeignKey('companies.company'), nullable=False)
    job_name = db.Column(db.String(128), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=False)
    publication_date = db.Column(db.DateTime, unique=False, nullable=False)
    salary = db.Column(db.Float, unique=False)
    vacancy_number = db.Column(db.Integer, unique=False)
    location = db.Column(db.String(30))
    working_hours = db.Column(db.Enum(*working_hours_types, name='working_hours_types'))
    minimum_experience = db.Column(db.Integer)

    def __init__(self, job_name, description, publication_date, salary, vacancy_number, location,
                 working_hours, minimum_experience):
        self.job_name = job_name
        self.description = description
        self.publication_date = publication_date
        self.salary = salary
        self.vacancy_number = vacancy_number
        self.location = location
        self.working_hours = working_hours
        self.minimum_experience = minimum_experience

    def json(self):
        return {'id': self.id, 'company': self.company, 'job_name': self.job_name,
                'description': self.description, 'publication_date': self.publication_date,
                'salary': self.salary, 'vacanc_number': self.vacancy_number, 'location': self.location,
                'working_hours': self.working_hours, 'minimum_experience': self.minimum_experience}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self, database=None):
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def show_job_offers(cls):
        return {'job_offers': [job_offer.json() for job_offer in cls.query.all()]}
