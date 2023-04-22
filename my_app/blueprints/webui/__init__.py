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

# ADMIN CREATE PROVIDERS
bp.add_url_rule("/admin/fornecedor/cadastro", 
    view_func=ViewsCreate.as_view('create_provider', Provider, 'admin/create.html', 
    fields={
        1:{
            'name': 'name',
            'label': 'Nome fantasia:',
            'required': True,
        },
        2:{
            'name': 'corporate_name',
            'label': 'Razão Social:'
        },
        3: {
            'name': 'email',
            'type': 'email',
            'label': 'Email da empresa:'
        },
        4:{
            'name': 'phone',
            'label': 'Telefone ou Celular:'   
        }
    }), methods=('GET', 'POST'))


# ADMIN CATEGORIES
bp.add_url_rule("/admin/categoria", 
    view_func=ViewsList.as_view('category', Category, 'admin/list.html', 
        columns={
            'id': 'Id',
            'description': 'Nome',
            'long_description': 'Observações',
        }
    ))


# ADMIN CREATE CATEGORIES
bp.add_url_rule("/admin/categoria/cadastro", 
    view_func=ViewsCreate.as_view('create_category', Category, 'admin/create.html', 
    fields={
        1:{
            'name': 'description',
            'label': 'Nome da categoria:',
            'required': True,
        },
        2:{
            'name': 'long_description',
            'label': 'Observaçoes da catagoria:',
            'type': 'text'
        }
    }), methods=('GET', 'POST'))



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


# ADMIN CREATE CATEGORIES
bp.add_url_rule("/admin/produto/cadastro", 
    view_func=ViewsCreate.as_view('create_product', Product, 'admin/create.html', 
    fields={
        1:{
            'name': 'description',
            'label': 'Nome da categoria:',
            'required': True,
        },
        2:{
            'name': Provider,
            'label': 'Observaçoes da catagoria:',
            'type': 'text'
        }
    }), methods=('GET', 'POST'))





def init_app(app):
    app.register_blueprint(bp)