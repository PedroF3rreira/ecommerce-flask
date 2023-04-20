from flask import abort, render_template
from flask.views import View
from my_app.blueprints.models.user import User
from my_app.ext.database import db


# Class de views listagem
class ViewsList(View):
	def __init__(self, model, template, columns):
		self.model = model
		self.template = template
		self.columns = columns


	def dispatch_request(self):
		items = self.model.query.all()
		return render_template(self.template, items=items, columns=self.columns)


def index():
	return render_template('admin/index.html')

