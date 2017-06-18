from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from jinja2 import Environment as EnvJinja
from .models import (
	db,
	User
)

environment = EnvJinja()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

toolbar = DebugToolbarExtension()

moment = Moment()

bootstrap = Bootstrap()

@login_manager.user_loader
def load_user(userid):
	return User.query.get(userid)

def create_app(config_object):
	app = Flask(__name__)
	app.config.from_object(config_object)

	######## Register Database ########

	db.init_app(app)

	######## Register Extentions ########

	login_manager.init_app(app)
	toolbar.init_app(app)
	moment.init_app(app)
	bootstrap.init_app(app)

	######## Register Application Routes ########
	
	from .main import main_route
	app.register_blueprint(main_route)

	from .auth import auth_route
	app.register_blueprint(auth_route)

	return app