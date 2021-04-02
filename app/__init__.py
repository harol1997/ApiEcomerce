from config import Config

from flask import Flask
from flask_restx import Api,Resource
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config.from_object(Config)

jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
ma = Marshmallow(app)

auth = {
        'Bearer Auth':{
                'type':'apiKey',
                'in':'header',
                'name':'Authorization'
        }
}

api = Api(  app,
        title="Pachaqtec",
        version="0.1",
        description="RESTAPI",
        prefix="/api/",
        doc="/docs/",
        contact="Harol Alvarado Valdivieso",
        contact_url="http://www.google.com",
        security='Bearer Auth',
        authorizations = auth
        )

from app.student import studentModel
from app.modality import modalityModel
from app.course import courseModel
from app.pstudent import pstudentModel
from app.teacher import teacherModel
from app.tables import tables

from app.course import courseSpace

from app.student import studentRouter