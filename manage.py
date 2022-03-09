from app import create_app, db
from flask import Manager, Server
from app.models import User
from flask import Migrate, MigrateCommand

# Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# Creating a python shell for  testing features in our apps and debugging using flask_script 

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User)


if __name__ == '__main__':
    manager.run()
