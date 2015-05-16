from extensions import db

from sqlalchemy import (
	Column,
	Integer,
	String,
	Text,
	ForeignKey,
	Table
	)

from sqlalchemy.orm import backref, relationship

class User(db.Model):
	"""
	usuario de nuestra aplicacion
	"""

	__tablename__ = "users"

	id= Column(Integer, primary_key=True)
	stp_id = Column(String(255, convert_unicode=True), unique=True)
	username = Column(String(40, convert_unicode=True), unique=True)
	email = Column(String(40, convert_unicode=True), unique=True)

	recetas = relationship("Receta", order_by="Receta.id", backref="user")

	def __init__(self, username):
		self.username = username

	def __repr__(self):
		return "<this is user {}>".format(self.username)

class Receta(db.Model):
	"""
	recetas de los usuarios
	"""

	__tablename__ = "recetas"

	id = Column(Integer, primary_key=True)
	nombre = Column(String(60, convert_unicode=True))
	categoria = Column(String(60, convert_unicode=True))
	utencilios = Column(String(255, convert_unicode=True))
	ingredientes = Column(String(255, convert_unicode=True))
	instrucciones = Column(String(255, convert_unicode=True))

	user_id = Column(Integer, ForeignKey("users.id"))

	def __init__(self, recipe, user_id):
		self.nombre = recipe
		self.user_id = user_id

	def __repr__(self):
			return "<esta receta pertenece a {}>".format(self.user_id)			
