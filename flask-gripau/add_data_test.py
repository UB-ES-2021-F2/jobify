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
from models.application import ApplicationModel

app = Flask(__name__)
environment = config['development']
if config_decouple('PRODUCTION', cast=bool, default=False):
    environment = config['production']
app.config.from_object(environment)
db = SQLAlchemy(app)
db.init_app(app)

new_job_seeker = JobSeekersModel('lordsergi', 'Sergi', 'Bech', 'sergi@gmail.com', 'hola, soc estudiant')
new_job_seeker.hash_password('Password12')

new_education = EducationsModel('Maths phd', 'UB', '2021-09', '2022-10', True)
new_workexperience = WorkExperiencesModel('professor', 'professor de EDS', 'ub', '2020-03', '2020-06', False)
new_skill = SkillsModel('python')
new_job_seeker.work_experiences.append(new_workexperience)
new_job_seeker.educations.append(new_education)
new_job_seeker.skills.append(new_skill)
db.session.add(new_job_seeker)

new_job_seeker_2 = JobSeekersModel('gripau', 'Gripau', 'Babau', 'gripau@gmail.com', 'hola, soc un gripau')
new_job_seeker_2.hash_password('Password12')
new_application = ApplicationModel()
new_job_seeker_2.applications.append(new_application)
db.session.add(new_job_seeker_2)

new_company = CompanyModel('universitat123', 'ub', 'ub@gmail.com', 'hola, som la UB')
new_job_offer = JobOfferModel('professor', 'professor de EDS', datetime.datetime(2021, 4, 7), 'Barcelona', 5000, 8, 'Full-time')
new_job_offer.applications.append(new_application)
new_company.hash_password('Password12')
new_company.job_offers.append(new_job_offer)
db.session.add(new_company)

db.session.commit()
db.session.close()
