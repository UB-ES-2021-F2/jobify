import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config as config_decouple
from config import config
# import models here
from models import EducationsModel, WorkExperiencesModel, JobOfferModel, SkillsModel
from models.job_seeker import JobSeekersModel
from models.company import CompanyModel
from models.education import EducationsModel
from models.job_offer import JobOfferModel
import json

app = Flask(__name__)
environment = config['development']
if config_decouple('PRODUCTION', cast=bool, default=False):
    environment = config['production']
app.config.from_object(environment)
db = SQLAlchemy(app)
db.init_app(app)

with open('data.json', 'rt') as data_file:
    data = json.load(data_file)

for job_seeker in data['jobseekers']:
    new_job_seeker = JobSeekersModel(job_seeker['username'], job_seeker['first-name'], job_seeker['last-name'], job_seeker['email'], job_seeker['bio'])
    new_job_seeker.hash_password(job_seeker['password'])
    for ed in job_seeker['educations']:
        new_education = EducationsModel(ed['title'], ed['institution'], ed['start-date'], ed['end-date'], ed['currently'])
        new_job_seeker.educations.append(new_education)
    for sk in job_seeker['skills']:
        new_skill = SkillsModel(sk)
        new_job_seeker.skills.append(new_skill)
    for we in job_seeker['work-experiences']:
        new_workexperience = WorkExperiencesModel(we['job-name'], we['description'], we['company'], we['start-date'], we['end-date'], we['currently'])
        new_job_seeker.work_experiences.append(new_workexperience)
    db.session.add(new_job_seeker)

for company in data['companies']:
    new_company = CompanyModel(company['username'], company['name'], company['email'], company["description"])
    new_company.hash_password(company['password'])
    for jo in company['job-offers']:
        new_job_offer = JobOfferModel(jo['job-name'], jo['description'], datetime.datetime(jo['posted-year'], jo['posted-month'], jo['posted-day']), jo['location'], jo['salary'], jo['weekly-working-hours'], jo['contract-type'])
        new_company.job_offers.append(new_job_offer)
    db.session.add(new_company)

db.session.commit()
db.session.close()
