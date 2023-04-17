from flask_login import LoginManager
from my_app.blueprints.models.user import User

login_manage = LoginManager()

@login_manage.user_loader
def load_user(user_id):
	return User.query.filter_by(id=user_id).first()

def init_app(app):
	login_manage.init_app(app)