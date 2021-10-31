from flask import g
from flask_restful import Resource, Api, reqparse
from models import JobOfferModel
from db import db
from models.company import CompanyModel
from datetime import datetime


class JobOffers(Resource):
    """
    Resource related to the table JobOffer
    """
    def get(self, id):
        """
        HTTP GET method that gets a specific job offer
        :param id: id of the job offer to return
        :return: json object with the job offer information
        """
        offer = JobOfferModel.find_by_id(id)

        if offer:
            return {'offer': offer.json()}, 200
        else:
            return {'offer': None}, 404

    def post(self, company):
        """
        HTTP POST method to create a job offer
        :param company: company that posts the job offer
        Request fields:
        - job_name: name of the job offer (Required)
        - description: description of the job offer (Optional)
        - salary: salary of the worker (Optional)
        - vacancy_number: number of vacancies that are available (Optional)
        - location: job location (Required)
        - contract_type: contract type (Optional)
        - working_hours: working hours (Optional)
        - minimum_experience: minimum experience required (Optional)
        :return: json object with the created job offer information
        """
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('job_name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument('salary', type=float, required=False, help="This field cannot be left blank")
        parser.add_argument('vacancy_number', type=int, required=False, help="This field cannot be left blank")
        parser.add_argument('location', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('contract_type', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument('working_hours', type=int, required=False, help="This field cannot be left blank")
        parser.add_argument('minimum_experience', type=int, required=False, help="This field cannot be left blank")

        data = parser.parse_args()

        date_time_obj = datetime.today()

        company = CompanyModel.find_by_company(company)

        if not company:
            return {"message": "This company is not registered yet."}, 500

        offer = JobOfferModel(data.job_name, data.description, date_time_obj, data.salary, data.vacancy_number,
                              data.location, data.working_hours, data.minimum_experience, data.contract_type)
        company.job_offers.append(offer)
        try:
            db.session.add(company)
            db.session.add(offer)
            db.session.commit()
        except:
            return {"message": "An error occurred inserting the offer."}, 500

        return offer.json(), 201

    def delete(self, id):
        """
        HTTP DELETE method to delete a specific job offer
        :param id: id of the job offer to delete
        :return: status message
        """
        offer = JobOfferModel.find_by_id(id)
        if offer:
            offer.delete_from_db(db)
            return {'message': "Offer with id [{}] deleted".format(id)}, 200

        return {'message': "Offer with id [{}] don't exists".format(id)}, 400
