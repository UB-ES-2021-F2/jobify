import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import models here
from models import EducationsModel, JobOfferModel
from models.job_seeker import JobSeekersModel
from models.company import CompanyModel
from models.education import EducationsModel
from models.job_offer import JobOfferModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

new_job_seeker = JobSeekersModel('LordSergi', 'Sergi', 'Bech', 'sergi@gmail.com', 'hola, soc estudiant')
new_job_seeker.hash_password('password')
new_education = EducationsModel('Maths phd', 'UB', '09-2021', '10-2022', True)
new_job_seeker.educations.append(new_education)
db.session.add(new_job_seeker)

new_company = CompanyModel('UB', 'ub@gmail.com', 'hola, som la UB')
new_job_offer = JobOfferModel('professor', 'professor de EDS', datetime.datetime(2021, 4, 7), 5000, 5, 'Barcelona', 1)
new_company.hash_password('password')
new_company.job_offers.append(new_job_offer)
db.session.add(new_company)

db.session.commit()
db.session.close()
