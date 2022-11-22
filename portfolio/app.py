import os

from flask import Flask

from portfolio.extensions import (
  db,
  bcrypt,
  scheduler
)

def create_app(config_filename="flask.cfg"):
  """Create Flask application factories."""

  app = Flask(__name__, instance_relative_config=True)
  app.config.from_pyfile(config_filename)

  register_blueprints(app)
  initialize_extensions(app)

  return app

def initialize_extensions(app):
  """Initializing Flask extensions."""

  db.init_app(app)
  bcrypt.init_app(app)

  return None

def register_blueprints(app):
  from portfolio.main.views import main

  app.register_blueprint(main)

  return None

def register_scheduler(app):
  """Registering Flask scheduler tasks."""
  from portfolio.tasks import updatePrices

  ## Stops flask_apscheduler from running twice
  if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    scheduler.init_app(app)
    scheduler.start()

  return None
