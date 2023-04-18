from my_app.ext.database import db
from flask_login import UserMixin


class Product(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	description = db.Column(db.String(100), nullable=False)
	long_description = db.Column(db.Text())
	price = db.Column(db.Float(), nullable=False)
	createdat = db.Column(db.DateTime())
	updatedat = db.Column(db.DateTime())
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
	provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)