from flask_restful import Resource

from models.company import CompanyModel


class CompanyList(Resource):

    def get(self):
        companyList = [x.json() for x in CompanyModel.query.all()]
        if len(companyList) > 0:
            return companyList, 200
        else:
            return {'message': "There are no companies"}, 404