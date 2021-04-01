from app import ma
from app.student.studentModel import Student

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True