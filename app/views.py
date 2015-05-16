from flask import render_template, Blueprint, redirect, url_for

main = Blueprint("main", __name__)

from extensions import db
from models import User, Receta

@main.route("/")
def index():

	users = db.session.query(User).all()
	recetas = db.session.query(Receta).all()
	return render_template(
		"index.html",
		users=users,
		recetas=recetas
		)

@main.route("/addUser/<string:name>")
def addUser(name):
	user = User(name)
	db.session.add(user)
	db.session.commit()
	return redirect(url_for("main.index"))	

@main.route("/addReceta/<string:name>/<string:username>")
def addReceta(name,username):

	user = db.session.query(User).filter_by(username=username).first()

	if user:	
		newreceta = Receta(name, user.id)

		db.session.add(newreceta)
		db.session.commit()
	return redirect(url_for("main.index"))		