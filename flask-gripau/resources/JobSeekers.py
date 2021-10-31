from flask import g
from flask_restful import Resource, Api, reqparse
from models import JobSeekersModel, CompanyModel
from db import db
from models.job_seeker import auth
from models.skill import SkillsModel


class JobSeekers(Resource):
    """
    Resource related to the table Jobseeker
    """
    def get(self, username):
        """
        HTTP GET method that gets a specific job seeker
        :param username: username of the job seeker to return
        :return: json object with the job seeker information
        """
        account = JobSeekersModel.find_by_username(username)
        if account:
            return {'account': account.json()}, 200
        else:
            return {'account': None}, 404

    def post(self):
        """
        HTTP POST method to create a job seeker
        :return: json object with the created job seeker information
        """
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('username', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('surname', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('bio', type=str, required=False)

        data = parser.parse_args()

        if JobSeekersModel.find_by_username(data.username):
            return {'message': "Username already exists"}, 400

        if CompanyModel.find_by_company(data.username):
            return {'message': "Username already exists"}, 400

        account = JobSeekersModel(data.username, data.name, data.surname, data.email, data.bio)

        account.hash_password(data.password)

        try:
            account.save_to_db(db)
        except:
            return {"message": "An error occurred inserting the account."}, 500

        return account.json(), 201

    @auth.login_required(role='user')
    def delete(self, username):
        """
        HTTP DELETE method to delete a specific job seeker
        :param username: username of the job seeker to delete
        :return: status message
        """
        if username != g.user.username:
            return {'message': 'Access denied'}, 400

        account = JobSeekersModel.find_by_username(username)
        if account:
            account.delete_from_db(db)
            return {'message': "Account deleted"}, 200

        return {'message': "Account doesn't exist"}, 400

    @auth.login_required(role='user')
    def put(self, username):
        """
        HTTP PUT method to update a specific job seeker
        :param username: name of the job seeker to update
        :return: json object with the updated job seeker information
        """

        if username != g.user.username:
            return {'message': 'Access denied'}, 400

        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('password', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('bio', type=str)
        parser.add_argument('name', type=str)
        parser.add_argument('surname', type=str)
        parser.add_argument('skills', type=str,
                            action="append")
        parser.add_argument('remove_skills', type=str,
                            action="append")

        account = JobSeekersModel.find_by_username(username)
        if account:
            data = parser.parse_args()
            if data.password:
                account.hash_password(data.password)
            if data.email:
                account.email = data.email
            if data.bio:
                account.bio = data.bio
            if data.name:
                account.name = data.name
            if data.surname:
                account.surname = data.surname
            if data.skills:
                for skill in data.skills:
                    if SkillsModel.find_by_username_and_name(username, skill) is None:
                        new_skill = SkillsModel(skill)
                        account.skills.append(new_skill)
            if data.remove_skills:
                for skill in data.remove_skills:
                    remove_skill = SkillsModel.find_by_username_and_name(username, skill)
                    remove_skill.delete_from_db()
                    #account.skills.remove(remove_skill)

            try:
                account.save_to_db(db)
            except Exception as err:
                print(Exception, err)
                return {"message": "An error occurred modifying the account."}, 500
            return account.json(), 202

        return {'message': "Company doesn't exist"}, 400
