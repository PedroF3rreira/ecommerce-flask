from flask_migrate import Migrate
from my_app.ext.database import db

migrate = Migrate()

def init_app(app):
	migrate.init_app(app, db)