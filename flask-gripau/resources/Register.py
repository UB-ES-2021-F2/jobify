from flask_restful import Resource, reqparse

from models import JobSeekersModel, CompanyModel
from db import db


class Register(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('name', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument('surname', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")
        #1 -> JobSeeker / 0 -> Company
        parser.add_argument('is_job_seeker', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=False)

        data = parser.parse_args()

        #Check if username is alphanumeric

        # Check user doesn't exist
        if JobSeekersModel.find_by_username(data.username):
            return {'message': "User already exists"}, 400
        if CompanyModel.find_by_company(data.username):
            return {'message': "User already exists"}, 400

        # Check email doesn't exist
        if JobSeekersModel.find_by_email(data.email):
            return {'message': "Email already exists"}, 400
        if CompanyModel.find_by_email(data.email):
            return {'message': "Email already exists"}, 400

        # Create account
        if data.is_job_seeker:
            account = JobSeekersModel(data.username, data.name, data.surname, data.email, data.description)
        else:
            account = CompanyModel(data.username, data.email, data.description)
        account.hash_password(data.password)

        try:
            account.save_to_db(db)
        except Exception as err:
            print(Exception, err)
            return {"message": "An error occurred inserting the account."}, 500

        return account.json(), 201
