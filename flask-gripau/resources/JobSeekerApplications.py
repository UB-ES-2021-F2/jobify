from flask_restful import Resource
from flask import g

from models import ApplicationModel, JobSeekersModel, JobOfferModel
from models.job_seeker import auth


class JobSeekerApplications(Resource):
    """
    Resource that lists all the applicants a user have done
    """
    @auth.login_required(role='user')
    def get(self, username):
        """
        HTTP method of the resource JobOfferApplicants
        :return: list all the applications of one user
        """
        if username != g.user.username:
            return {'message': 'Access denied'}, 401

        applications = [x.json() for x in ApplicationModel.find_by_job_seeker_username(username)]
        if len(applications) > 0:
            return applications, 200
        else:
            return {'message': "There are no applications of the user [{}]".format(username)}, 404
