from flask import abort, render_template
from my_app.blueprints.models.user import User
from my_app.blueprints.models.provider import Provider
from my_app.blueprints.models.category import Category
from my_app.ext.database import db


def index():
	return render_template('admin/index.html')

# List Users
def user():
	users = User.query.all()
	columns = {
		'id': 'Id',
		'name': 'Nome completo',
		'email': 'Email',
	}
	return render_template('admin/list.html', items=users, columns=columns)

# List Providers
def provider():
	providers = Provider.query.all()
	columns = {
		'id': 'Id',
		'name': 'Nome fantasia',
		'corporate_name': 'Razão social',
		'email': 'Email',
		'phone': 'Contato',
	}
	return render_template('admin/list.html', items=providers, columns=columns)


# List Category
def category():
	categories = Category.query.all()
	columns = {
		'id': 'Id',
		'description': 'Nome',
		'long_description': 'Observações',
		
	}
	return render_template('admin/list.html', items=categories, columns=columns)