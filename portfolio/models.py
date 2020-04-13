from datetime import datetime
from portfolio import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(130))
    content = db.Column(db.String)
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
