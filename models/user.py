from app import db

class User(db.Model):
    # ID (int), username (text), password (test)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80)), nullable=False, unique=True
    password = db.Column(db.String(80), nullable=False)