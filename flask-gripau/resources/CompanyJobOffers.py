from flask import g
from flask_restful import Resource, Api, reqparse
from models import JobOfferModel
from db import db
from models.company import CompanyModel


class CompanyJobOffers(Resource):
    """Resource related to the relation between the tables Company and JobOffer"""
    def get(self, company):
        """HTTP GET method that gets the list of job offers of a specific company

        Args:
          company: username of the company

        Returns:
          list of json objects with the company's job offers information

        """
        company = CompanyModel.find_by_username(company)
        if company:
            return [offer.json() for offer in company.job_offers], 200
        else:
            return {'Company': None}, 404
