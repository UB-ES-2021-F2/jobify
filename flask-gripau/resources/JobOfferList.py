from flask import g
from flask_restful import Resource, Api, reqparse
from models import JobOfferModel
from db import db
from models.company import CompanyModel
from fuzzywuzzy import fuzz

class JobOfferList(Resource):
    """Resource that lists all the job offers in the database"""
    def get(self):
        """HTTP method of the resource JobOfferList
        :return: list of all the job offers in the database

        Args:

        Returns:

        """

        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('keyword', type=str, required=False)

        data = parser.parse_args()


        offers = []
        if data.keyword is None:
            for company in CompanyModel.query.all():
                for offer in company.job_offers:
                    offers.append(offer.json())
        else:
            for company in CompanyModel.query.all():
                to_append = False
                for word in company.company.split(" "):
                    if fuzz.ratio(word, data.keyword) > 80:
                        to_append = True
                        break
                for offer in company.job_offers:
                    if to_append:
                        offers.append(offer.json())
                    else:
                        offer_name = offer.job_name
                        appended=False
                        for word in offer_name.split(" "):
                            if fuzz.ratio(word, data.keyword) > 80:
                                offers.append(offer.json())
                                appended = True
                                break
        return {'OfferList': offers}, 200
