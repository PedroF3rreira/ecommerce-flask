from my_app.ext.database import db
from flask_login import UserMixin


class Category(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(80), nullable=False)
	long_description = db.Column(db.Text())
	createdat = db.Column(db.DateTime())
	updatedat = db.Column(db.DateTime())
	products = db.relationship('Product', backref='category', lazy=True)