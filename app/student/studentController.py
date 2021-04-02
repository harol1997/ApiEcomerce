from app.student.studentModel import Student
from app import db

from flask import request
from flask_jwt_extended import create_access_token

class StudentController:

    @staticmethod
    def login():
        username = request.json.get('email')
        password = request.json.get('password')

        student:Student = Student.query.filter_by(email=username).first()

        if student:
            if student.check_password(password):
                access_token = create_access_token(identity=username)
                return{
                    'state' : 'pass',
                    'access_token' : access_token
                }
            else:
                return {
                    'state':'error',
                    'message':'incorrect password'
                }
        else:
            return {
                'state':'error',
                'message':'user not exist'
            }        

    @staticmethod
    def register():
        name = request.json.get('name').strip()
        email = request.json.get('email').strip()
        password = request.json.get('password').strip()

        student = Student.query.filter_by(email=email).first()
        if student:
            return {
                'status':'error',
                'message':'the student already exist with exit'
            }
        new_student = Student(
                             name=name,
                             email = email,
                             password = password
                            )

        new_student.generate_password()

        db.session.add(new_student)
        db.session.commit()

        return {
            'status':'pass',
            'message':'the student has been registered'
        }
