from flask.ext.script import Manager

from app import create_app
from app.extensions import db

from app.models import User

from app.models import Receta

app = create_app("default")

manager = Manager(app)

@manager.shell

def make_shell_context():
	return dict(
		app=app,
		db=db,
		user=User,
		receta=Receta
	)

if __name__ == '__main__':
	manager.run()	