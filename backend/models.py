# backend/models.py
from database import db

class DailyWeatherSummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    avg_temp = db.Column(db.Float, nullable=False)
    max_temp = db.Column(db.Float, nullable=False)
    min_temp = db.Column(db.Float, nullable=False)
    dominant_condition = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "date": self.date,
            "avg_temp": self.avg_temp,
            "max_temp": self.max_temp,
            "min_temp": self.min_temp,
            "dominant_condition": self.dominant_condition
        }
