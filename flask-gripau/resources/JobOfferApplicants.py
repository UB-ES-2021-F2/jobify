from flask_restful import Resource

from models import ApplicationModel, JobSeekersModel


class JobOfferApplicants(Resource):
    """
    Resource that lists all the applicants to a given offer
    """

    def get(self, job_offer_id):
        """
        HTTP method of the resource JobOfferApplicants
        :return: list of all the applicants of an offer
        """
        applications = [x for x in ApplicationModel.find_by_job_offer_id(job_offer_id)]
        applicants = []
        for a in applications:
            applicants.append(JobSeekersModel.find_by_username(a.job_seeker_username).json())
        if len(applicants) > 0:
            return applicants, 200
        else:
            return {'message': "There are no applicants to the offer [{}]".format(job_offer_id)}, 404
