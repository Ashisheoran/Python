from flask import Flask
from models import db
from config import Config
from routes import app_routes

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(app_routes)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)


### config.py

import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "secret123")