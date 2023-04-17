from flask import Blueprint

from .views import index, user



bp = Blueprint("webui", __name__, template_folder="templates")

#views USER
bp.add_url_rule("/", view_func=index)
bp.add_url_rule(
    "/usuario/<id>", view_func=user, endpoint="userview")


#PRODUCS
bp.add_url_rule("/produtos", view_func=index)


def init_app(app):
    app.register_blueprint(bp)