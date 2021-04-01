from app import db

class Teacher(db.Model):
    id = db.Column(db.Integer,index=True,primary_key=True,unique=True,autoincrement=True)
    name = db.Column(db.Text,nullable=False)
    courses = db.relationship('Course',backref="teacher",lazy=True)
    