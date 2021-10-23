from flask import g
from flask_restful import Resource, Api, reqparse
from models import JobOfferModel
from db import db
from models.company import CompanyModel
from datetime import datetime


class JobOffers(Resource):

    def get(self, id):

        offer = JobOfferModel.find_by_id(id)

        if offer:
            return {'offer': offer.json()}, 200
        else:
            return {'offer': None}, 404

    def post(self, company):
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('job_name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('publication_date', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('salary', type=float, required=False, help="This field cannot be left blank")
        parser.add_argument('vacancy_number', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('location', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('minimum_experience', type=int, required=True, help="This field cannot be left blank")

        # parser.add_argument('working_hours', type=working_hours_types, choices=list(working_hours_types))

        data = parser.parse_args()

        date_time_obj = datetime.strptime(data.publication_date, '%d-%m-%Y')

        company = CompanyModel.find_by_company(company)

        if not company:
            return {"message": "This company is not registered yet."}, 500

        offer = JobOfferModel(data.job_name, data.description, date_time_obj, data.salary, data.vacancy_number, data.location, data.minimum_experience)
        company.job_offers.append(offer)
        try:
            db.session.add(company)
            db.session.add(offer)
            db.session.commit()
        except:
            return {"message": "An error occurred inserting the offer."}, 500

        return offer.json(), 201

    def delete(self, id):
        offer = JobOfferModel.find_by_id(id)
        if offer:
            offer.delete_from_db(db)
            return {'message': "Offer with id [{}] deleted".format(id)}, 200

        return {'message': "Offer with id [{}] don't exists".format(id)}, 400
