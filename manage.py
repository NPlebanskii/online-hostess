from flask_script import Manager  # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from onlinehostess.app import db, create_app, models

config_name = 'dev'
app = create_app(config_name=config_name)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
