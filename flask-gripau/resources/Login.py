from flask_restful import Resource, reqparse

from models import JobSeekersModel, CompanyModel


class Login(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        for job_seeker in JobSeekersModel.query.all():
            if job_seeker.username == data['username']:
                if job_seeker.verify_password(data['password']):
                    return {'token': job_seeker.generate_auth_token().decode('ascii')}, 200
                else:
                    return {"message": "Invalid password"}, 400

        for company in CompanyModel.query.all():
            if company.company == data['username']:
                if company.verify_password(data['password']):
                    return {'token': company.generate_auth_token().decode('ascii')}, 200
                else:
                    return {"message": "Invalid password"}, 400

        return {"message": "User doesn't exist"}, 404
