from app import db


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.Text,nullable=False)
    description = db.Column(db.Text,nullable=False)
    module = db.Column(db.Integer,nullable=False)
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.id'),nullable=False)
    modality_id = db.Column(db.Integer,db.ForeignKey('modality.id'),nullable=False)

