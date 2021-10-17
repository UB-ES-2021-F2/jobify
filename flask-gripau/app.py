from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_migrate import Migrate
from db import db
from flask_cors import CORS

# Imports de resources
from resources import JobSeekers
from resources import Companies
from resources import Login
from resources import Register
from resources import Educations
from resources import WorkExperiences

# Imports de models
from models.job_seeker import JobSeekersModel
from models.company import CompanyModel
from models.education import EducationsModel
from models.work_experience import WorkExperiencesModel

from flask import g, current_app
from decouple import config as config_decouple
from config import config


def create_app():
    app = Flask(__name__)
    return app


app = create_app()
environment = config['development']
if config_decouple('PRODUCTION', cast=bool, default=False):
    environment = config['production']

app.static_folder = environment.STATIC_FOLDER
app.template_folder = environment.TEMPLATE_FOLDER

app.config.from_object(environment)

CORS(app, resources={r'/*': {'origins': '*'}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# with app.app_context():
#    app.config['SECRET_KEY'] = current_app.secret_key

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

# api.add_resource(Artist, '/artist/<int:id>', '/artist')
api.add_resource(JobSeekers, '/jobseeker/<string:username>', '/jobseeker')
api.add_resource(Companies, '/company/<string:company>', '/company')
api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(Educations, '/education/<string:username>')
api.add_resource(WorkExperiences, '/work_experience/<string:username>')


@app.route('/')
def render_vue():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
