from app.carshop.carshopSchema import CarshopSchema
from app.carshop.carshopModel import CarshopModel
from app import api

from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from time import strftime

carshop_schema = CarshopSchema(many = True)

class CarshopResource(Resource):
    @jwt_required()
    def post(self):
        name = request.json.get('student_id')
        date = strftime('%T-%m-%d')
        courses = request.json.get('courses')
        print(name,courses,sep='\n')