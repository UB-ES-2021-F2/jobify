from db import db
from models import CompanyModel


# contract_types = ('INDEFINITE', 'DETERMINED_DURATION', 'STAND_ALONE', 'PART_TIME', 'TRAINING')


class JobOfferModel(db.Model):
    """Model of a job offer.
    Company 1 ---> * Job Offer

    Args:

    Returns:

    """
    __tablename__ = 'job_offer'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(30), db.ForeignKey('companies.username'), nullable=False)
    job_name = db.Column(db.String(128), unique=False, nullable=False)
    description = db.Column(db.String(5000), unique=False)
    publication_date = db.Column(db.DateTime, unique=False, nullable=False)
    salary = db.Column(db.String(30), unique=False)
    location = db.Column(db.String(30), unique=False, nullable=False)
    working_hours = db.Column(db.Integer, unique=False)
    contract_type = db.Column(db.String(30), unique=False)
    applications = db.relationship('ApplicationModel', backref='job_offer_applications', lazy=True)

    def __init__(self, job_name, description, publication_date, location, salary=None,
                 working_hours=None, contract_type=None):
        """
        Initializer of a job offer
        :param job_name: name of the job offer
        :param description: description of the job offer
        :param publication_date: date when the job offer was published
        :param location: job location
        :param salary: salary of the worker
        :param working_hours: weekly working hours
        :param contract_type: contract type
        """
        self.job_name = job_name
        self.description = description
        self.publication_date = publication_date
        self.salary = salary
        self.location = location
        self.working_hours = working_hours
        self.contract_type = contract_type

    def json(self):
        """Function that returns the job offer info as json
        :return: json object with the information'

        Args:

        Returns:

        """
        company_name = ''
        if CompanyModel.find_by_username(self.company):
            company_name = CompanyModel.find_by_username(self.company).company

        return {'id': self.id, 'company': self.company, 'company_name': company_name,
                'job_name': self.job_name, 'description': self.description, 'publication_date':
                    self.publication_date.strftime("%Y-%m-%d"), 'salary': self.salary, 'location': self.location,
                'working_hours': self.working_hours, 'contract_type': self.contract_type,
                'applications': [application.json() for application in self.applications]}

    def save_to_db(self, database=None):
        """Function that saves to the database the job offer

        Args:
          database: database instance (Default value = None)

        Returns:

        """
        if database is None:
            database = db
        database.session.add(self)
        database.session.commit()

    def delete_from_db(self, database=None):
        """Function that the deletes from the database the job offer

        Args:
          database: database instance (Default value = None)

        Returns:

        """
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    def delete_application(self, id):
        """Function that deletes an application from the applications list of the job offer

        Args:
          id: id of the application

        Returns:
          : the application removed, None if the application does not exist

        """
        for a in self.applications:
            if a.id == id:
                self.applications.remove(a)
                return a
        return None

    @classmethod
    def find_by_id(cls, _id):
        """Function that finds by id the job offer

        Args:
          _id: id of the job offer

        Returns:
          : the job offer

        """
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def show_job_offers(cls):
        """Function that returns a json with all the job offers in the database
        :return: json object with all the job offers

        Args:

        Returns:

        """
        return [job_offer.json() for job_offer in cls.query.all()]
