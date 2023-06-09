from dynaconf import FlaskDynaconf
from importlib import import_module

def load_extensions(app):
	for extension in app.config.get('EXTENSIONS'):
		mod = import_module(extension)
		mod.init_app(app)


def init_app(app):
	FlaskDynaconf(app, settings_files=['settings.toml'])