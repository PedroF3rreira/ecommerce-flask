from my_app.ext.database import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	confirmed = db.Column(db.Boolean())
	ceatedat = db.Column(db.DateTime())
	updatedat = db.Column(db.DateTime())
