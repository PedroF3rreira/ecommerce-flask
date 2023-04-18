from flask import abort, render_template
from my_app.blueprints.models.user import User
from my_app.ext.database import db


def index():
	return render_template('admin/index.html')


def user():
	users = User.query.all()
	columns = {
		'id': 'Id',
		'name': 'Nome completo',
		'email': 'Email',
	}
	return render_template('admin/list.html', items=users, columns=columns)