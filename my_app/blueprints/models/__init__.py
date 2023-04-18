from flask import Blueprint

from .user import User
from .category import Category
from .provider import Provider
from .product import Product


bp = Blueprint("models", __name__)


def init_app(app):
    app.register_blueprint(bp)