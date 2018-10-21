from dotenv import load_dotenv
load_dotenv()

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app.models import camera, role, room, user, checkin, checkin_status

config_name = os.getenv("APP_SETTINGS")
app = create_app(config_name)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()