from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import models here
from models.job_seeker import JobSeekersModel
from models.company import CompanyModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

new_job_seeker = JobSeekersModel('sergi','sergi@gmail.com', 'hola, soc estudiant')
db.session.add(new_job_seeker)

new_company = CompanyModel('UB','ub@gmail.com', 'hola, som la UB')
db.session.add(new_company)

db.session.commit()
db.session.close()