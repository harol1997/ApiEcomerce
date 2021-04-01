from app.course.courseResource import CourseResource,CourseResourceAll

from app import api

course_namespace = api.namespace(
                                'course',
                                description="API TO COURSES"
                                )

course_namespace.add_resource(CourseResource,'/<int:id>')
course_namespace.add_resource(CourseResourceAll,'/getall')

api.add_namespace(course_namespace)