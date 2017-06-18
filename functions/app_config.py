from config import Config

def app_config():
	return """# -*- coding: utf-8 -*-

import os

class Config(object):
	SECRET_KEY = os.urandom(128).encode('base64')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = '{0}'

	# DB_USERNAME = ''
	# DB_PASSWORD = ''
	# DB_DATABASE = ''
	# SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@localhost:5432/%s'%(DB_USERNAME, DB_PASSWORD, DB_DATABASE)

	@staticmethod
	def init_app(app):
		pass

class ProdConfig(Config):
	SQLALCHEMY_DATABASE_URI = '{0}'
	DEBUG = False

class DevConfig(Config):

	SQLALCHEMY_DATABASE_URI = '{0}'
	DEBUG = True
	DEBUG_TB_INTERCEPT_REDIRECTS = False
	APP_NAME = '{1}'
	""".format(Config.DB_PATH, Config.APP_NAME)