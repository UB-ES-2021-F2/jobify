from flask_restful import Resource, reqparse

from models import JobSeekersModel, CompanyModel


class Login(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()

        job_seeker = JobSeekersModel.find_by_username(data.username)
        if job_seeker:
            if job_seeker.verify_password(data['password']):
                return {'token': job_seeker.generate_auth_token().decode('ascii')}, 200
            else:
                return {"message": "Invalid password"}, 400

        company = CompanyModel.find_by_company(data.username)
        if company:
            if company.verify_password(data['password']):
                return {'token': company.generate_auth_token().decode('ascii')}, 200
            else:
                return {"message": "Invalid password"}, 400

        return {"message": "User doesn't exist"}, 404
