from app import app
from app.student.studentModel import Student
from app.student.studentController import StudentController

from flask import request
from flask_jwt_extended import create_access_token

@app.route('/login',methods=['POST'])
def login():
    return StudentController.login()

@app.route('/register',methods=['POST'])
def register():
    return StudentController.register()
