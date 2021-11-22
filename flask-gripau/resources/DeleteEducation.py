from flask import g
from flask_restful import Resource, Api, reqparse
from models import EducationsModel, JobSeekersModel
from models.job_seeker import auth
from db import db


class DeleteEducation(Resource):

    @auth.login_required(role='user')
    def post(self, username):

        if username != g.user.username:
            return {'message': 'Access denied'}, 401

        parser = reqparse.RequestParser()

        parser.add_argument('id', type=int, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        user = JobSeekersModel.find_by_username(username)

        education = user.delete_education(data.id)

        if education:
            education.delete_from_db(db)
            return {'message': "Education with id [{}] deleted".format(data.id)}, 200

        return {'message': "Education with id [{}] doesn't exist".format(data.id)}, 404



