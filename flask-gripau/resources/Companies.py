from flask import g
from flask_restful import Resource, Api, reqparse
from models import CompanyModel
from db import db
from models.company import auth


class Companies(Resource):

    def get(self, company):

        account = CompanyModel.find_by_company(company)
        if account:
            return {'account': account.json()}, 200
        else:
            return {'account': None}, 404

    def post(self):
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('company', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=False)

        data = parser.parse_args()

        if CompanyModel.find_by_company(data.company):
            return {'message': "User already exists"}, 400

        account = CompanyModel(data.company, data.email, data.description)

        account.hash_password(data.password)

        try:
            account.save_to_db(db)
        except:
            return {"message": "An error occurred inserting the account."}, 500

        return account.json(), 201

    @auth.login_required(role='admin')
    def delete(self, company):

        if g.user.is_admin == 0:
            return {'message': 'Access denied'}, 400

        account = CompanyModel.find_by_company(company)
        if account:
            account.delete_from_db(db)
            return {'message': "Account deleted"}, 200

        return {'message': "Account don't exists"}, 400
