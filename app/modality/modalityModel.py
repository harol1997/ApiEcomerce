from app import db

class Modality(db.Model):
    __tablename__='modality'
    id = db.Column(db.Integer,index=True,primary_key=True,unique=True,autoincrement=True)
    name = db.Column(db.Text,nullable=False)
    courses = db.relationship('Course',backref='course',lazy=True)