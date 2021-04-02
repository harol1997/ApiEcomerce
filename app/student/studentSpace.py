from app.student.studentResource import StudentRegisterResource

from app import api

student_namespace = api.namespace(
                                'student',
                                description="APIT TO STUDENT"
                                )

student_namespace.add_resource(StudentRegisterResource,'/register')

api.add_namespace(student_namespace)
