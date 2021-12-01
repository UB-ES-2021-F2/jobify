from flask_restful import Resource, Api, reqparse
from fuzzywuzzy import fuzz

from models.company import CompanyModel


class CompanyList(Resource):
    """Resource that lists all the companies in the database"""
    def get(self):
        """HTTP method of the resource CompanyList
        :return: list of all the companies in the database

        Args:

        Returns:

        """

        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('keyword', type=str, required=False)

        data = parser.parse_args()

        company_list = []
        if data.keyword is None or data.keyword == '':
            company_list = [x.json() for x in CompanyModel.query.all()]
        else:
            for company in CompanyModel.query.all():
                to_append = True
                for word in data.keyword.split(" "):
                    if fuzz.partial_ratio(word.lower(), company.company.lower()) < 80:
                        to_append = False
                        break
                if to_append:
                    company_list.append(company.json())

        return company_list, 200
