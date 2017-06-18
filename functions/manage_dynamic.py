from config import Config

def manage_dynamic():

	return """from {0} import create_app
from {0}.models import db,User
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app('{0}.config.DevConfig')

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
	return dict(app=app, db=db)

@manager.command
def inituser():
	user = User()
	user.username = 'reznov'
	user.set_password('123123123')
	user.email = 'example@email.com'
	db.session.add(user)
	db.session.commit()
	
	return 'User created.'

if __name__ == '__main__':
	manager.run()
	""".format(Config.APP_NAME)