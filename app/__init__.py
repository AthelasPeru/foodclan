from flask import Flask

from config import config

from extensions import toolbar, db, foundation

def create_app(config_mode):
	app = Flask(__name__)
	app.config.from_object(config[config_mode])

	toolbar.init_app(app)
	foundation.init_app(app)


	from views import main

	app.register_blueprint(main)

	db.init_app(app)

	db.create_all(app=app)	

	return app