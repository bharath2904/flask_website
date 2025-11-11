from flask import Flask, request, redirect, url_for, render_template_string, jsonify, abort, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, 'site.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(DB_PATH)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET', 'dev-secret-key')

db = SQLAlchemy(app)