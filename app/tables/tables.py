from app import db

room = db.Table(
                'course_room',
                db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
                db.Column('course_id',db.Integer,db.ForeignKey('course.id'))
                )

pstudentcourse = db.Table(
                        'pstudent_course',
                        db.Column('pstudent_id',db.Integer,db.ForeignKey('pstudent.id')),
                        db.Column('course_id',db.Integer,db.ForeignKey('course.id'))
                        )
