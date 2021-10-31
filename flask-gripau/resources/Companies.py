from flask import g
from flask_restful import Resource, Api, reqparse
from models import CompanyModel, JobSeekersModel
from db import db
from models.company import auth


class Companies(Resource):
    """
    Resource related to the table Company
    """
    def get(self, company):
        """
        HTTP GET method that gets a specific company
        :param company: name of the company to return
        :return: json object with the company information
        """
        account = CompanyModel.find_by_company(company)
        if account:
            return {'account': account.json()}, 200
        else:
            return {'account': None}, 404

    @auth.login_required(role='user')
    def delete(self, company):
        """
        HTTP DELETE method to delete a specific company
        :param company: name of the company to delete
        :return: status message
        """
        if company != g.user.company:
            return {'message': 'Access denied'}, 400

        account = CompanyModel.find_by_company(company)
        if account:
            account.delete_from_db(db)
            return {'message': "Account deleted"}, 200

        return {'message': "Account doesn't exist"}, 400

    @auth.login_required(role='user')
    def put(self, company):
        """
        HTTP PUT method to update a specific company
        :param company: name of the company to update
        :return: json object with the updated company information
        """

        if company != g.user.company:
            return {'message': 'Access denied'}, 400

        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('password', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('sector', type=str)
        parser.add_argument('location', type=str)

        account = CompanyModel.find_by_company(company)
        if account:
            data = parser.parse_args()
            if data.password:
                account.hash_password(data.password)
            if data.email:
                account.email = data.email
            if data.description:
                account.description = data.description
            if data.sector:
                account.sector = data.sector
            if data.location:
                account.location = data.location

            account.save_to_db()
            try:
                account.save_to_db(db)
            except:
                return {"message": "An error occurred modifying the account."}, 500
            return account.json(), 202

        return {'message': "Company doesn't exist"}, 400
