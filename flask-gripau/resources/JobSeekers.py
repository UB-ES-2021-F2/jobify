from flask import g
from flask_restful import Resource, Api, reqparse
from models import JobSeekersModel, CompanyModel
from db import db
from models.job_seeker import auth
from models.skill import SkillsModel
from resources.Register import validate_password, validate_email


class JobSeekers(Resource):
    """Resource related to the table Jobseeker"""
    def get(self, username):
        """
        HTTP GET method that gets a specific job seeker
        
        Args:
          username: username of the job seeker to return

        Returns:
          json object with the job seeker information

        @api {get} /jobseeker/<string:username> Get JobSeeker information
        @apiName GetJobSeeker
        @apiGroup JobSeeker

        @apiParam {String} username Username of the JobSeeker
        @apiSuccess {Object} jobseeker Data of the JobSeeker matching username
        @apiError (Error 404) NotFound Jobseeker with <code>username</code> was not found
        """
        account = JobSeekersModel.find_by_username(username)
        if account:
            return {'account': account.json()}, 200
        else:
            return {'account': None}, 404

    @auth.login_required(role='user')
    def delete(self, username):
        """HTTP DELETE method to delete a specific job seeker

        Args:
          username: username of the job seeker to delete

        Returns:
          status message

        @api {delete} /jobseeker/<string:username> Delete JobSeeker information
        @apiName DeleteJobSeeker
        @apiGroup JobSeeker
        @apiPermission user

        @apiParam {String} username Username of the JobSeeker
        @apiSuccess {String} message Account deleted
        @apiError (Error 404) NotFound Jobseeker with <code>username</code> was not found
        @apiError (Error 401) AccesDenied Acces denied (no valid authentication or authenticated user doesn't match username)
        @apiError (Error 400) IternalError Backend error when updating the database
        """
        if username != g.user.username:
            return {'message': 'Access denied'}, 401

        account = JobSeekersModel.find_by_username(username)
        if account:
            try:
                for education in account.educations:
                    db.session.delete(education)
                for work_experience in account.work_experiences:
                    db.session.delete(work_experience)
                for skill in account.skills:
                    db.session.delete(skill)
                for application in account.applications:
                    db.session.delete(application)
                account.delete_from_db(db)
                return {'message': "Account deleted"}, 200
            except Exception:
                db.session.rollback()
                return {'message': 'An error occurred deleting the account'}, 400

        return {'message': "Account doesn't exist"}, 404

    @auth.login_required(role='user')
    def put(self, username):
        """HTTP PUT method to update a specific job seeker

        Args:
          username: name of the job seeker to update
        Request fields:
        - name: real name of the job seeker (Optional)
        - surname: real surname of the job seeker (Optional)
        - password: password of the account (Optional)
        - email: email of the job seeker (Optional)
        - bio: biography/information that the job seeker would want to share (Optional)
        - skills: list of skills to add to the skills list of the job seeker (Optional)
        - remove_skills: list of skills to remove from the skills list of the job seeker (Optional)

        Returns:
          json object with the updated job seeker information

        @api {put} /jobseeker/<string:username> Update JobSeeker information
        @apiName PutJobSeeker
        @apiGroup JobSeeker
        @apiPermission user

        @apiParam {String} username Username of the job seeker
        @apiParam {String} [name] First name of the job seeker
        @apiParam {String} [surname] Last name of the job seeker
        @apiParam {String} [password] Password of the account
        @apiParam {String} [email] Email of the job seeker
        @apiParam {String} [bio] Biography/information that the job seeker would want to share
        @apiParam {Object[]} [skills] List of skills to add to the skills list of the job seeker
        @apiParam {Object[]} [remove_skills] List of skills to remove from the skills list of the job seeker

        @apiSuccess {Object} jobseeker Data of the JobSeeker matching username
        @apiError (Error 400) NotFound Jobseeker with <code>username</code> was not found
        @apiError (Error 405) InvalidPasswordFormat Password invalid! Does not meet requirements
        @apiError (Error 402) InvalidEmailFormat Incorrect email format
        @apiError (Error 408/409) EmailAlreadyExists This email is in use by another account
        @apiError (Error 500) IternalError Backend error when updating the database
        """

        if username != g.user.username:
            return {'message': 'Access denied'}, 401

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
                # Validate password
                if not validate_password(data.password):
                    return {'message': "Password invalid! Does not meet requirements"}, 405
                account.hash_password(data.password)
            if data.email and data.email != account.email:
                # Validate email
                if not validate_email(data.email):
                    return {'message': 'Email wrong format!'}, 402
                # Check email doesn't exist
                if JobSeekersModel.find_by_email(data.email):
                    return {'message': "Email already exists"}, 408
                if CompanyModel.find_by_email(data.email):
                    return {'message': "Email already exists"}, 409
                account.email = data.email
            if data.bio or data.bio == '':
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
                    if remove_skill:
                        remove_skill.delete_from_db()
                    #account.skills.remove(remove_skill)

            try:
                account.save_to_db(db)
            except Exception as err:
                print(Exception, err)
                return {"message": "An error occurred modifying the account."}, 500
            return account.json(), 202

        return {'message': "Company doesn't exist"}, 400
