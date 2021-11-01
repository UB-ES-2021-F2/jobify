from flask_restful import Resource, reqparse

from models import JobSeekersModel, CompanyModel
from db import db
import re

reg = "^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z]).{8,20}$"


class Register(Resource):
    """
    Resource that manages the registration to the app
    """
    def post(self):
        """
        HTTP POST method to register in the application
        Request fields:
        - username: username of the job seeker  or company (Required)
        - name: name of the job seeker (Optional)
        - surname: surname of the job seeker (Optional)
        - password: password of the user (Required)
        - is_job_seeker: if the user is a job seeker, 1 (yes) / 0 (no, is a company) (Required)
        - email: email of the user (Required)
        - description: bio/description of the user (Optional)
        :return: json object with the information of the registered user
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('surname', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")
        # 1 -> JobSeeker / 0 -> Company
        parser.add_argument('is_job_seeker', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=False)

        data = parser.parse_args()

        # Check if username is alphanumeric
        if not data.username.isalnum():
            return {'message': "Username must contain only alphanumeric characters"}, 400
        elif not all(x.isalpha() or x.isspace() for x in data.name):
            return {'message': "Name must contain only alphanumeric characters or spaces"}, 401
        if data.surname:
            if not data.surname.isalpha():
                return {'message': "Surname must contain only alphanumeric characters"}, 402

        # Convert username to lowercase
        data.username = data.username.lower()

        # Validate password
        if not validate_password(data.password):
            return {'message': "Password invalid! Does not meet requirements"}, 405

        # Check user doesn't exist
        if JobSeekersModel.find_by_username(data.username):
            return {'message': "User already exists"}, 406
        if CompanyModel.find_by_company(data.username):
            return {'message': "User already exists"}, 407

        # Check email doesn't exist
        if JobSeekersModel.find_by_email(data.email):
            return {'message': "Email already exists"}, 408
        if CompanyModel.find_by_email(data.email):
            return {'message': "Email already exists"}, 409

        # Create account
        if data.is_job_seeker:
            account = JobSeekersModel(data.username, data.name, data.surname, data.email, data.description)
        else:
            account = CompanyModel(data.username, data.name, data.email, data.description)
        account.hash_password(data.password)

        try:
            account.save_to_db(db)
        except Exception as err:
            print(Exception, err)
            return {"message": "An error occurred inserting the account."}, 500

        return account.json(), 201


def validate_password(password):
    """
    Function that validates that the password matches the requirements
    :param password: password to check
    :return: boolean, indicating the validation result
    """
    # compiling regex
    pat = re.compile(reg)
    # searching regex
    mat = re.search(pat, password)
    return mat
