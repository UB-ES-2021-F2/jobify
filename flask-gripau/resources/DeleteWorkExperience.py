from flask import g
from flask_restful import Resource, Api, reqparse
from models import WorkExperiencesModel, JobSeekersModel
from models.job_seeker import auth
from db import db


class DeleteWorkExperience(Resource):

    @auth.login_required(role='user')
    def post(self, username):

        if username != g.user.username:
            return {'message': 'Access denied'}, 400

        parser = reqparse.RequestParser()

        parser.add_argument('id', type=int, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        user = JobSeekersModel.find_by_username(username)

        work_exp = user.delete_work_experience(data.id)

        if work_exp:
            work_exp.delete_from_db(db)
            return {'message': "Work experience with id [{}] deleted".format(data.id)}, 200

        return {'message': "Work experience with id [{}] don't exists".format(data.id)}, 400

