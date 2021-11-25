from db import db
from models import JobOfferModel


class ApplicationModel(db.Model):
    """Model of an application
    Job Offer 1 ---> * Applications
    Job Seeker 1 ---> * Applications

    Args:

    Returns:

    """
    __tablename__ = 'applications'
    __table_args__ = (db.UniqueConstraint('job_seeker_username', 'job_offer_id'),)

    id = db.Column(db.Integer, primary_key=True)
    job_seeker_username = db.Column(db.String(30), db.ForeignKey('jobseekers.username'), nullable=False)
    job_offer_id = db.Column(db.Integer, db.ForeignKey('job_offer.id'), nullable=False)
    info = db.Column(db.String(500), unique=False, nullable=True)

    def __init__(self, info=None):
        """
        Initializer of an application.
        :param info: the additional information the job seeker wants to give
        """
        self.info = info

    def json(self):
        """Function that returns the application info as json
        :return: json object with the information

        Args:

        Returns:

        """

        job_offer_name = None
        if JobOfferModel.find_by_id(self.job_offer_id):
            job_offer_name = JobOfferModel.find_by_id(self.job_offer_id).job_name

        return {'id': self.id, 'job_seeker_username': self.job_seeker_username, 'job_offer_id': self.job_offer_id,
                'job_offer_name': job_offer_name, 'info': self.info}

    def delete_from_db(self, database=None):
        """Function that the deletes from the database the application

        Args:
          database: database instance (Default value = None)

        Returns:

        """
        if database is None:
            database = db
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_by_job_seeker_username(cls, job_seeker_username):
        """Function that returns a list of applications given the job seeker username

        Args:
          job_seeker_username: username of the job seeker

        Returns:
          : list of applications

        """
        return cls.query.filter_by(job_seeker_username=job_seeker_username).all()

    @classmethod
    def find_by_job_offer_id(cls, job_offer_id):
        """Function that returns a list of applications given the job offer id

        Args:
          job_offer_id: id of the job offer

        Returns:
          : list of applications

        """
        return cls.query.filter_by(job_offer_id=job_offer_id).all()

    @classmethod
    def show_applications(cls):
        """Function that shows all the applications in the database
        :return: list of the applications

        Args:

        Returns:

        """
        return [application.json() for application in cls.query.all()]
