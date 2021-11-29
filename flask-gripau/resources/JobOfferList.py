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
        parser.add_argument('job_type', type=str, required=False)

        data = parser.parse_args()

        offers = []
        if data.keyword is None or data.keyword == '':
            for company in CompanyModel.query.all():
                for offer in company.job_offers:
                    offers.append(offer.json())
        else:
            for company in CompanyModel.query.all():
                to_append = True
                for word in data.keyword.split(" "):
                    if fuzz.partial_ratio(word.lower(), company.company.lower()) < 60:
                        to_append = False
                        break
                for offer in company.job_offers:
                    if to_append:
                        offers.append(offer.json())
                    else:
                        append = True
                        for word in data.keyword.split(" "):
                            if fuzz.partial_ratio(word.lower(), offer.job_name.lower()) < 60:
                                append = False
                                break
                        if append:
                            offers.append(offer.json())

        if data.job_type is not None and data.job_type != '':
            job_types = data.job_type.split(',')
            filtered_offers = [o for o in offers if o['contract_type'] in job_types]
            offers = filtered_offers

        return {'OfferList': offers}, 200
