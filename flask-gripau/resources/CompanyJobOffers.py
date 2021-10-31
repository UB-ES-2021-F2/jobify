from flask import g
from flask_restful import Resource, Api, reqparse
from models import JobOfferModel
from db import db
from models.company import CompanyModel


class CompanyJobOffers(Resource):
    """
        Resource that lists all the job offers from one specific company in the database
    """

    def get(self, company):
        """
            HTTP method of the resource CompanyJobOffers
            :return: list of all the job offers from one the company
        """
        company = CompanyModel.find_by_company(company)
        if company:
            return [offer.json() for offer in company.job_offers], 200
        else:
            return {'Company': None}, 404
