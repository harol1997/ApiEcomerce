from app import db
from app.tables.tables import carshopcourse

class CarshopModel(db.Model):
    __tablename__ = "carshop"
    id = db.Column(db.Integer,index=True,primary_key=True,unique=True,autoincrement=True)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'),nullable=False)
    date = db.Column(db.DateTime,nullable=False)
    courses = db.relationship('Course',secondary=carshopcourse,lazy='subquery',backref=db.backref('carshops',lazy=True))
    