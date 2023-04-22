from flask import abort, render_template, request, redirect
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


# Class de views cadastro
class ViewsCreate(View):
	def __init__(self, model, template, fields):
		self.model = model
		self.template = template
		self.fields = fields


	def dispatch_request(self):
		if request.method == 'POST':
			model = self.model()
			error = None

			for field in self.fields.values():
				setattr(model, field['name'], request.form[field['name']])
			
			db.session.add(model)
			db.session.commit()		
			
			return "Cadastro realizado com exito"
			
		else:
			
			for item in self.fields.values():
				if type(item['name']) == 'flask_sqlalchemy.model.DefaultMeta':
					m = item['name']()
					print(dir(m))

			return render_template(self.template, fields=self.fields)


def index():
	return render_template('admin/index.html')

