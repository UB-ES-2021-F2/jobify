from flask import g
from flask_restful import Resource, Api, reqparse
from models import JobOfferModel
from db import db
from models.company import CompanyModel
from datetime import datetime
from models.company import auth


class JobOffers(Resource):
    """Resource related to the table JobOffer"""

    def get(self, id):
        """HTTP GET method that gets a specific job offer

        Args:
          id: id of the job offer to return

        Returns:
          json object with the job offer information

        """
        offer = JobOfferModel.find_by_id(id)

        if offer:
            return {'offer': offer.json()}, 200
        else:
            return {'offer': None}, 404

    @auth.login_required(role='user')
    def post(self, company):
        """HTTP POST method to create a job offer

        Args:
          company: username of the company that posts the job offer
        Request fields:
        - job_name: name of the job offer (Required)
        - contract_type: contract type (Optional)
        - salary: salary of the worker (Optional)
        - location: job location (Required)
        - working_hours: weekly working hours (Optional)
        - description: description of the job offer (Optional)

        Returns:
          json object with the created job offer information

        """
        if company != g.user.username:
            print(g.user.username)
            return {'message': 'Access denied'}, 401

        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('job_name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument('salary', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument('location', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('contract_type', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument('working_hours', type=int, required=False, help="This field cannot be left blank")

        data = parser.parse_args()

        date_time_obj = datetime.today()

        company = CompanyModel.find_by_username(company)

        if not company:
            return {"message": "This company is not registered yet."}, 500

        if data.job_name and len(data.job_name) > 128:
            return {"message": "The job_name field can't be larger than 128 characters."}, 431
        if data.contract_type and len(data.contract_type) > 30:
            return {"message": "The contract_type field can't be larger than 30 characters."}, 431
        if data.salary and len(data.salary) > 30:
            return {"message": "The salary field can't be larger than 30 characters."}, 431
        if data.location and len(data.location) > 30:
            return {"message": "The location field can't be larger than 5000 characters."}, 431
        if data.description and len(data.description) > 5000:
            return {"message": "The description field can't be larger than 5000 characters."}, 431
        if data.working_hours is not None and data.working_hours > 168:
            return {"message": "The working hours can't exceed 168 hours/week."}, 406
        offer = JobOfferModel(data.job_name, data.description, date_time_obj, data.location, data.salary,
                              data.working_hours, data.contract_type)

        company.job_offers.append(offer)
        try:
            db.session.add(company)
            db.session.add(offer)
            db.session.commit()
        except:
            return {"message": "An error occurred inserting the offer."}, 500

        return offer.json(), 201

    @auth.login_required(role='user')
    def delete(self, id):
        """HTTP DELETE method to delete a specific job offer

        Args:
          id: id of the job offer to delete

        Returns:
          status message

        """

        offer = JobOfferModel.find_by_id(id)

        if offer:
            if offer.company != g.user.username:
                print(g.user.username)
                return {'message': 'Access denied'}, 401
            for application in offer.applications:
                db.session.delete(application)
            offer.delete_from_db(db)
            return {'message': "Offer with id [{}] deleted".format(id)}, 200

        return {'message': "Offer with id [{}] don't exists".format(id)}, 404
