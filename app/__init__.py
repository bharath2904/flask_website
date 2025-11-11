from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET", "dev_secret_key")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    db.init_app(app)

    from app import routes
    app.register_blueprint(routes.main)

    return app
