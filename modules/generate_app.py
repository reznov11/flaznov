import os, sys
import errno
import time
import subprocess
from .colors import colors
from config import Config, script_dir
from functions.app_config import app_config
from functions.base_html import base_html
from functions.manage_dynamic import manage_dynamic

def get_snippet(to_read, to_write):
	with open(script_dir+'/snippets/'+to_read) as fread:
	    with open(to_write, "w") as fwirte:
	        for line in fread:
	            fwirte.write(line)

def init_app():

	print colors.CYAN + '\n[*] ' + colors.ENDC + 'Initiating the app'
	time.sleep(1.5)

	if os.path.exists('__init__.py'):
		get_snippet('__init__.sp',script_dir+'/'+Config.APP_NAME+'/__init__.py')

def controllers():

	print colors.YELLOW + '\n[*] ' + colors.ENDC + 'Creating Controllers'
	time.sleep(1.5)

	try:
		for controller in Config.CONTROLLERS:
			if not os.path.exists(controller):
				while True:
					os.makedirs(controller)
					with open(os.path.join(script_dir, Config.APP_NAME, controller, '__init__.py'), 'wb') as f:
						f.write("from flask import Blueprint\n{0}_route = Blueprint('{0}',__name__,static_folder='../static')\nfrom . import views".format(controller))
					with open(os.path.join(script_dir, Config.APP_NAME, controller, 'views.py'), 'wb') as f:
						f.write("#!-*- coding: utf-8 -*-\n\n\nfrom flask import render_template, redirect, url_for, flash, session, g\nfrom ..models import *\n\nfrom . import {0}_route \n\n\n@{0}_route.route('/')\ndef {0}():\n\n\treturn render_template('base.html')".format(controller))
					with open(os.path.join(script_dir, Config.APP_NAME, controller, 'forms.py'), 'wb') as f:
						f.write("#!-*- coding: utf-8 -*-\n\n\nfrom flask_wtf import Form\nfrom wtforms import TextAreaField, TextField, PasswordField, StringField, BooleanField, Field, HiddenField, DateField, SelectField, IntegerField\nfrom wtforms.validators import Required, Length, Email, Regexp, EqualTo, InputRequired")
					break

	except OSError as exc:
		if exc.errno != errno.EEXIST:
		    raise

def virtual_env(activate=False):

	print colors.DARKCYAN + '\n[*] ' + colors.ENDC + 'Creating virtual environment'
	time.sleep(1.5)

	if activate == True:
		os.system('virtualenv venv')

		print colors.GREEN + '\n[*] ' + colors.ENDC + 'Generating requirements.txt'
		time.sleep(1.5)
		os.system('/bin/bash venv/bin/activate')

		for req in Config.REQUIREMENTS:	
			while True:
				with open(os.path.join(script_dir, Config.APP_NAME, 'requirements.txt'), 'wb') as f:
					f.write("\n".join(Config.REQUIREMENTS))
				break
			# 	os.system('pip install {}'.format(req))
			# 	subprocess.call(['pip', 'install', '{}'.format(req)])

def create_app(name):

	try:
		print colors.RED + '\n[*] ' + colors.ENDC + 'Creating the app and all it dependinces'
		time.sleep(1.5)
		os.makedirs(name)
		os.chdir(name)
		for folder in Config.FRONT_END_FOLDERS:
			if not os.path.exists(folder):
				while True:
					os.makedirs(folder)
					with open(os.path.join(script_dir, Config.APP_NAME, '__init__.py'), 'wb') as f:
						f.write("")
					with open(os.path.join(script_dir, Config.APP_NAME, 'config.py'), 'wb') as f:
						f.write(app_config())
					with open(os.path.join(script_dir, Config.APP_NAME, 'models.py'), 'wb') as f:
						f.write("")
						f.close()
					# with open(os.path.join(script_dir, Config.APP_NAME, 'requirements.txt'), 'wb') as f:
					# 	f.write("")
					break
		if os.path.exists('templates'):
			with open(os.path.join(script_dir, Config.APP_NAME, 'templates', Config.FILENAME), 'wb') as f:
				f.write(base_html())
				f.close()

			controllers()
			init_app()
			virtual_env(activate=True)

		if os.path.exists('models.py'):
			get_snippet('models.sp',script_dir+'/'+Config.APP_NAME+'/models.py')

		print colors.BLUE + '\n[*] ' + colors.ENDC + 'Configuring manage.py'
		time.sleep(1.5)

		os.chdir(script_dir)
		with open(os.path.join(script_dir, 'manage.py'), 'wb') as f:
			f.write("")
		if os.path.exists('manage.py'):
			with open(os.path.join(script_dir, 'manage.py'), 'wb') as f:
				f.write(manage_dynamic())
				f.close()

	except OSError as exc:
		if exc.errno != errno.EEXIST:
		    raise