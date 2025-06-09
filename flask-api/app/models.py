from datetime import datetime
from app.extensions import db

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # ← ЛУЧШЕ ДЛЯ PYTHON-КОДА

