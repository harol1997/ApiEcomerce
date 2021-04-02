from app.course.courseSchema import CourseSchema
from app.course.courseModel import Course
from app import api

from flask_restx import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

class CourseResource(Resource):#class to obtain only one course
    @jwt_required()
    def get(self,id):
        course = Course.query.filter_by(id=id).first()
        return course_schema.dump(course)

class CourseResourceAll(Resource):#class to obtain all courses
    @jwt_required()
    def get(self):        
        courses = Course.query.all()
        return courses_schema.dump(courses)
