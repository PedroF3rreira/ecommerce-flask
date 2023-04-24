from my_app.ext.database import db
from flask_login import UserMixin


class Provider(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(80),nullable=False)
	corporate_name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100))
	phone = db.Column(db.String(14))
	products = db.relationship('Product', backref='product', lazy=True)

	def __repr__(self):
		return self.name
