from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_apscheduler import APScheduler

db = MongoEngine()
bcrypt = Bcrypt()
scheduler = APScheduler()
