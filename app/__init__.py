import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    """App factory"""
    load_dotenv()
    app = Flask(__name__)
    
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DB_PATH = os.path.join(BASE_DIR, '..', 'site.db')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET', 'dev-secret')
    
    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    app.jinja_env.globals['site_name'] = 'My Idea Website'
    return app


def init_db(app):
    """Initialize the database and seed sample posts."""
    from app.models import Post
    with app.app_context():
        if not os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'site.db')):
            db.create_all()
            p1 = Post(title='Welcome', slug='welcome', content='This is your starter website. Edit this content.')
            p2 = Post(title='About Project', slug='about-project', content='Describe your project here.')
            db.session.add_all([p1, p2])
            db.session.commit()
