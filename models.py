from datetime import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://devgrid:devgrid@localhost:5432/api'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Weather(db.Model):
    __tablename__ = 'weather'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    data = db.Column(db.JSON)

    def __init__(self, id, date, data):
        self.id = id
        self.date = date
        self.data = data