from flask import g
from flask_restful import Resource, Api, reqparse
from models import JobOfferModel
from db import db
from models.company import CompanyModel

class JobOfferList(Resource):

    def get(self):
        offers = []
        for company in CompanyModel.query.all():
            for offer in company.job_offers:
                offers.append(offer.json())
        return {'OfferList': offers}, 200
