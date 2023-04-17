from flask import abort, render_template
from my_app.blueprints.models.user import User
from my_app.ext.database import db


def index():
	users = db.session.execute(db.select(User).order_by(User.name)).scalars()
	return render_template('index.html', users=users)



def user(id):
	user = db.session.execute(db.select(User).where(User.id == id)).scalar()
	return render_template('user.html', user=user)
