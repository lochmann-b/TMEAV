import os
from app import create_app, db
from app.models import User
from flask_migrate import Migrate

application = create_app(os.getenv('TMEAV_FLASK_CONFIG') or 'default')
migrate = Migrate(application, db)

@application.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)