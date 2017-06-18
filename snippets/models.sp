# -*- coding: utf-8 -*-

from flask import current_app, Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):

	__tablename__ = 'user'

	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String())
	password = db.Column(db.String())
	email = db.Column(db.String())
	joined = db.Column(db.DateTime(), default=datetime.utcnow)

	def __repr__(self):
		return '{}'.format(self.username)

	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, value):
		return check_password_hash(self.password, value)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)