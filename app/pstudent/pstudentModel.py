from app import db
from app.tables.tables import pstudentcourse

class PStudent(db.Model):
    __tablename__ = 'pstudent'
    name = db.Column(db.Integer)
    id = db.Column(db.Integer,index=True,primary_key=True,unique=True,autoincrement=True)
    name = db.Column(db.Text,nullable=False)
    email = db.Column(db.Text,index=True,unique=True,nullable=False)
    password = db.Column(db.Text,nullable=False)
    courses = db.relationship('Course',secondary=pstudentcourse,lazy='subquery',backref=db.backref('pstudents',lazy=True))