from flask import Blueprint

from .admin import *

bp = Blueprint("webui", __name__, template_folder="templates")

# ADMIN VIEWS
bp.add_url_rule("/admin", view_func=index, )
bp.add_url_rule("/admin/usuario", view_func=user, )
bp.add_url_rule("/admin/fornecedor", view_func=provider, )
bp.add_url_rule("/admin/categoria", view_func=category, )
bp.add_url_rule("/admin/produto", view_func=product, )



def init_app(app):
    app.register_blueprint(bp)