from app import db
from app.tables.tables import room

from werkzeug.security import generate_password_hash,check_password_hash

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,index=True,primary_key=True,unique=True,autoincrement=True)
    name = db.Column(db.Text,nullable=False)
    email = db.Column(db.Text,index=True,unique=True,nullable=False)
    password = db.Column(db.Text,nullable=False)
    courses = db.relationship('Course',secondary=room,lazy='subquery',backref=db.backref('students',lazy=True))

    def generate_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self,password):
        return check_password_hash(self.password,password)
