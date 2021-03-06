from datetime import date

from flask import g
from flask_restful import Resource, Api, reqparse
from models import WorkExperiencesModel, JobSeekersModel
from models.job_seeker import auth
from db import db


class WorkExperiences(Resource):
    """Resource related to the WorkExperiences endpoint"""
    def get(self, username):
        """HTTP GET method that gets the list of work experiences of a specific job seeker

        Args:
          username: name of the job seeker

        Returns:
          list of json objects with the job seeker's work experiences information

        """
        account = JobSeekersModel.find_by_username(username)
        if not account:
            return {'work_experience': None}, 404
        return [work_experience.json() for work_experience in account.work_experiences], 200

    @auth.login_required(role='user')
    def post(self, username):
        """HTTP POST method to create a work experience

        Args:
          username: username of the job seeker that posts the work experience
        Request fields:
        - job_name: name of the job (Required)
        - description: description of the job (Required)
        - company: company where the job was done (Required)
        - start_date: start date of the work experience (Required)
        - end_date: end date of the work experience (Required)
        - currently: if the job seeker is currently working on this job (Required)

        Returns:
          json object with the created work experience information

        """
        if username != g.user.username:
            return {'message': 'Access denied'}, 401

        parser = reqparse.RequestParser()

        parser.add_argument('job_name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('description', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('company', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('start_date', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('end_date', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument('currently', type=bool, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        user = JobSeekersModel.find_by_username(username)

        if data.job_name.isspace():
            return {"message": "Job name cannot be blank"}, 400

        if not user:
            return {'user': None}, 404

        # Date validations
        if not data.end_date and not data.currently:
            return {"message": "End date is required if \"currently\" is false"}, 400

        today = date.today()
        try:
            start_year, start_month = data.start_date.split('-')
        except ValueError:
            return {"message": "Date format is wrong, try (yyyy-mm)"}, 400

        if not start_year.isnumeric() or not start_month.isnumeric():
            return {"message": "Date format is wrong, try (yyyy-mm)"}, 400
        elif int(start_year) < 1900 or int(start_year) > 2100:
            return {"message": "Dates need to be between years 1900 and 2100"}, 400
        elif int(start_month) < 1 or int(start_month) > 12:
            return {"message": "Dates need to be between months 1 and 12"}, 400
        elif int(start_year) > today.year or (int(start_year) == today.year and int(start_month) > today.month):
            return {"message": "Start date cannot be posterior to current date"}, 400

        if data.end_date:
            try:
                end_year, end_month = data.end_date.split('-')
            except ValueError:
                return {"message": "Date format is wrong, try (yyyy-mm)"}, 400

            if not end_year.isnumeric() or not end_month.isnumeric():
                return {"message": "Date format is wrong, try (yyyy-mm)"}, 400
            elif int(end_year) < 1900 or int(end_year) > 2100:
                return {"message": "Dates need to be between years 1900 and 2100"}, 400
            elif int(end_month) < 1 or int(end_month) > 12:
                return {"message": "Dates need to be between months 1 and 12"}, 400
            elif int(start_year) > int(end_year):
                return {"message": "Start date cannot be posterior than end date"}, 400
            elif int(start_year) == int(end_year):
                if int(start_month) > int(end_month):
                    return {"message": "Start date cannot be posterior than end date"}, 400

            if data.currently:
                if int(end_year) < today.year or (int(end_year) == today.year and int(end_month) < today.month):
                    return {"message": "End date cannot be previous to current date if \"currently\" is true"}, 400
            else:
                if int(end_year) > today.year or (int(end_year) == today.year and int(end_month) > today.month):
                    return {
                               "message": "End date cannot be posterior to current date if \"currently\" is false"}, 400

        if data.job_name and len(data.job_name) > 128:
            return {"message": "The job name field can't be larger than 128 characters."}, 431

        if data.description and len(data.description) > 5000:
            return {"message": "The description field can't be larger than 5000 characters."}, 431

        if data.company and len(data.company) > 128:
            return {"message": "The company field can't be larger than 128 characters."}, 431

        new_work_experience = WorkExperiencesModel(data.job_name, data.description, data.company, data.start_date, data.end_date, data.currently)
        user.work_experiences.append(new_work_experience)

        try:
            db.session.add(user)
            db.session.add(new_work_experience)
            db.session.commit()
            return {'work_experience': new_work_experience.json()}, 200
        except:
            db.session.rollback()
            return {"message": "An error occurred inserting the order."}, 500

