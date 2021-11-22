from flask import g
from flask_restful import Resource, Api, reqparse
from models import CompanyModel, JobSeekersModel
from resources.Register import validate_password, validate_email
from db import db
from models.company import auth


class Companies(Resource):
    """Resource related to the table Company"""
    def get(self, company):
        """HTTP GET method that gets a specific company

        Args:
          company: username of the company to return

        Returns:
          json object with the company information

        @api {get} /company/<string:username> Get company information
        @apiName GetCompany
        @apiGroup Company

        @apiParam {String} oompany Name of the company
        @apiSuccess {Object} company Data of the Company with matching name
        @apiError (Error 404) NotFound Company with <code>name</code> was not found
        """
        account = CompanyModel.find_by_username(company)
        if account:
            return {'account': account.json()}, 200
        else:
            return {'account': None}, 404
          
    @auth.login_required(role='user')
    def delete(self, company):
        """HTTP DELETE method to delete a specific company

        Args:
          company:  username of the company to delete

        Returns:
          status message

        @api {delete} /company/<string:username> Delete Company information
        @apiName DeleteCompany
        @apiGroup Company
        @apiPermission user

        @apiParam {String} username Username of the company
        @apiSuccess {String} message Company deleted
        @apiError (Error 404) NotFound Company with <code>username</code> was not found
        @apiError (Error 401) AccesDenied Acces denied (no valid authentication or authenticated user doesn't match username)
        @apiError (Error 500) IternalError Backend error when updating the database
        """
        if company != g.user.username:
            return {'message': 'Access denied'}, 401

        account = CompanyModel.find_by_username(company)

        if account:
            try:
                for offer in account.job_offers:
                    db.session.delete(offer)
                account.delete_from_db(db)
                return {'message': "Account deleted"}, 200
            except Exception:
                db.session.rollback()
                return {'message': 'An error occurred deleting the account'}, 500
        return {'message': "Account doesn't exist"}, 404

    @auth.login_required(role='user')
    def put(self, company):
        """HTTP PUT method to update a specific company

        Args:
          company: username of the company to update
        Request fields:
        - password: password of the account (Required)
        - email: email of the company (Required)
        - description: description of the company (Optional)
        - sector: sector of the company (Optional)
        - location: location of the company (Optional)

        Returns:
          json object with the updated company information

        @api {put} /company/<string:username> Update Company information
        @apiName PutCompany
        @apiGroup Company
        @apiPermission user

        @apiParam {String} username Username of the job seeker
        @apiParam {String} [name] First name of the job seeker
        @apiParam {String} [surname] Last name of the job seeker
        @apiParam {String} [password] Password of the account
        @apiParam {String} [email] Email of the job seeker
        @apiParam {String} [bio] Biography/information that the job seeker would want to share
        @apiParam {Object[]} [skills] List of skills to add to the skills list of the job seeker
        @apiParam {Object[]} [remove_skills] List of skills to remove from the skills list of the job seeker

        @apiSuccess {Object} company Data of the Company matching username
        @apiError (Error 400) NotFound Company with <code>username</code> was not found
        @apiError (Error 401) AccesDenied Acces denied (no valid authentication or authenticated user doesn't match username)
        @apiError (Error 405) InvalidPasswordFormat Password invalid! Does not meet requirements
        @apiError (Error 402) InvalidEmailFormat Incorrect email format
        @apiError (Error 408/409) EmailAlreadyExists This email is in use by another account
        @apiError (Error 500) IternalError Backend error when updating the database
        """

        if company != g.user.username:
            print(g.user.username)
            print(company)
            return {'message': 'Access denied'}, 401

        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('password', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('sector', type=str)
        parser.add_argument('location', type=str)

        account = CompanyModel.find_by_username(company)
        if account:
            data = parser.parse_args()
            if data.password:
                # Validate password
                if not validate_password(data.password):
                    return {'message': "Password invalid! Does not meet requirements"}, 406
                account.hash_password(data.password)
            if data.email and data.email != account.email:
                if not validate_email(data.email):
                    return {'message': 'Email wrong format!'}, 402
                # Check email doesn't exist
                if JobSeekersModel.find_by_email(data.email):
                    return {'message': "Email already exists"}, 409
                if CompanyModel.find_by_email(data.email):
                    return {'message': "Email already exists"}, 409
                account.email = data.email
            if data.description or data.description == '':
                account.description = data.description
            if data.sector:
                account.sector = data.sector
            if data.sector == '':
                account.sector = 'Unknown'
            if data.location:
                account.location = data.location
            if data.location == '':
                account.location = 'Unknown'

            account.save_to_db()
            try:
                account.save_to_db(db)
            except:
                return {"message": "An error occurred modifying the account."}, 500
            return account.json(), 200

        return {'message': "Company doesn't exist"}, 404


