from flask import Blueprint
from my_app.blueprints.models.user import User
from my_app.blueprints.models.provider import Provider
from my_app.blueprints.models.category import Category
from my_app.blueprints.models.product import Product

from .admin import *

bp = Blueprint("webui", __name__, template_folder="templates")


# ADMIN VIEWS
bp.add_url_rule("/admin", view_func=index, )


# ADMIN USERS
bp.add_url_rule("/admin/usuario", 
    view_func=ViewsList.as_view('user', User,'admin/list.html', 
    columns={
            'id': 'Id',
            'name': 'Nome completo',
            'email': 'Email'
            }
        ))


# ADMIN PROVIDERS
bp.add_url_rule("/admin/fornecedor", 
    view_func=ViewsList.as_view('provider', Provider, 'admin/list.html', 
        columns={
            'id': 'Id',
            'name': 'Nome fantasia',
            'corporate_name': 'Razão social',
            'email': 'Email',
            'phone': 'Contato',
        }
    ))


# ADMIN CATEGORIES
bp.add_url_rule("/admin/categoria", 
    view_func=ViewsList.as_view('category', Category, 'admin/list.html', 
        columns={
            'id': 'Id',
            'description': 'Nome',
            'long_description': 'Observações',
        }
    ))



# ADMIN PRODUCTS
bp.add_url_rule("/admin/produto", 
    view_func=ViewsList.as_view('product', Product, 'admin/list.html', 
        columns={
            'id': 'Id',
            'description': 'Descrição',
            'long_description': 'Detalhes',
            'price': 'Preço',
            'category': 'Categoria'
        }
    ))

def create():
    return render_template('admin/create.html')

bp.add_url_rule("/admin/create", view_func=create)

def init_app(app):
    app.register_blueprint(bp)