from flask import g
from flask_restful import Resource, Api, reqparse
from models import WorkExperiencesModel, JobSeekersModel
from models.job_seeker import auth
from db import db


class DeleteApplication(Resource):
    """
    Resource related to the deletion of an Application
    """

    @auth.login_required(role='user')
    def post(self, job_seeker_username):
        """
        HTTP POST method to delete an application
        :param job_seeker_username: username of the job seeker that deletes the application
        Request fields:
        - id: id of the application (Required)
        :return: status message
        """
        if job_seeker_username != g.user.username:
            return {'message': 'Access denied'}, 400

        parser = reqparse.RequestParser()

        parser.add_argument('id', type=int, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        user = JobSeekersModel.find_by_username(job_seeker_username)
        application = user.delete_application(data.id)

        if application:
            application.delete_from_db(db)
            return {'message': "Application with id [{}] deleted".format(data.id)}, 200

        return {'message': "Application with id [{}] don't exists".format(data.id)}, 400
