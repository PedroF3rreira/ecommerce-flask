from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from my_app.ext.database import db
from my_app.models.user import User

admin = Admin()

class UserView(ModelView):
    column_searchable_list = ['name', 'email']
    column_editable_list = ['name']
    create_modal = True
    edit_modal = True
    can_export = True
    page_size = 2



def init_app(app):
	admin.name = app.config.TITLE
	admin.init_app(app)
	admin.add_view(UserView(User, db.session, category='users'))
