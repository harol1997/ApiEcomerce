from flask_restx import Resource
from flask import request

from app.student.studentController import StudentController
from app.student.studentSchema import StudentSchema

student_schema = StudentSchema()

class StudentRegisterResource(Resource):
    def post(self):
        return StudentController.register()
