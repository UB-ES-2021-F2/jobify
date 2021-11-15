from flask import g
from flask_restful import Resource, Api, reqparse
from models import WorkExperiencesModel, JobSeekersModel, ApplicationModel, JobOfferModel
from models.job_seeker import auth
from db import db


class Applications(Resource):
    """
    Resource related to the Applications endpoint
    """

    def get(self, job_seeker_username):
        """
        HTTP GET method that gets the list of applications of a specific job seeker
        :param job_seeker_username: name of the job seeker
        :return: list of json objects with the job seeker's applications information
        """
        return [application.json() for application in
                ApplicationModel.find_by_job_seeker_username(job_seeker_username)], 200

    # @auth.login_required(role='user')
    def post(self, job_seeker_username):
        """
        HTTP POST method to create an application
        :param job_seeker_username: username of the job seeker that posts the application
        Request fields:
        - job_offer_id: id of the job offer (Required)
        - info: additional information the job seeker wants to give (Optional)
        :return:  json object with the created application information
        """
        # if job_seeker_username != g.user.username:
        #    return {'message': 'Access denied'}, 400

        parser = reqparse.RequestParser()

        parser.add_argument('job_offer_id', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('info', type=str, required=False)

        data = parser.parse_args()

        user = JobSeekersModel.find_by_username(job_seeker_username)
        job_offer = JobOfferModel.find_by_id(data.job_offer_id)

        if not user or not job_offer:
            return {"message": "The user or the job offer doesn't exist."}, 500

        new_application = ApplicationModel(data.info)
        new_application.job_seeker_username = user.username
        new_application.job_offer_id = job_offer.id
        user.applications.append(new_application)
        job_offer.applications.append(new_application)

        try:
            db.session.add(user)
            db.session.add(job_offer)
            db.session.commit()
            return {'application': new_application.json()}, 200
        except:
            db.session.rollback()
            return {"message": "An error occurred inserting the order."}, 500
