from flask_restful import Resource

from models import ApplicationModel, JobSeekersModel


class JobOfferApplicants(Resource):
    """
    Resource that lists all the applicants to a given offer
    """
    @auth.login_required(role='user')
    def get(self, job_offer_id):
        """
        HTTP method of the resource JobOfferApplicants
        :return: list of all the applicants of an offer
        """
        # check if this job offer is made by the company logged
        offer = JobOfferModel.find_by_id(id)
        if offer:
            if offer.company != g.user.username:
                return {'message': 'Access denied'}, 401
                
            applications = [x for x in ApplicationModel.find_by_job_offer_id(job_offer_id)]
            applicants = []
            for a in applications:
                applicants.append(JobSeekersModel.find_by_username(a.job_seeker_username).json())
            if len(applicants) > 0:
                return applicants, 200
            else:
                return {'message': "There are no applicants to the offer [{}]".format(job_offer_id)}, 404
        return {'message': "There is no job offer with id [{}]".format(job_offer_id)}, 404
