from flask import g
from flask_restful import Resource, Api, reqparse
from models import JobSeekersModel
from db import db
from models.job_seeker import auth


class JobSeekers(Resource):

    def get(self, username):

        account = JobSeekersModel.find_by_username(username)
        if account:
            return {'account': account.json()}, 200
        else:
            return {'account': None}, 404

    def post(self):
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('username', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('bio', type=str, required=False)

        data = parser.parse_args()

        if JobSeekersModel.find_by_username(data.username):
            return {'message': "User already exists"}, 400

        account = JobSeekersModel(data.username, data.email, data.bio)

        account.hash_password(data.password)

        try:
            account.save_to_db(db)
        except:
            return {"message": "An error occurred inserting the account."}, 500

        return account.json(), 201

    @auth.login_required(role='admin')
    def delete(self, username):

        if g.user.is_admin == 0:
            return {'message': 'Access denied'}, 400

        account = JobSeekersModel.find_by_username(username)
        if account:
            account.delete_from_db(db)
            return {'message': "Account deleted"}, 200

        return {'message': "Account doesn't exist"}, 400
