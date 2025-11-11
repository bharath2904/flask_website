
# Flask Auto Website - Starter

A minimal self-contained Flask starter site with SQLite (SQLAlchemy).  
Files included:
- Flask_AutoWebsite.py : the main application
- requirements.txt : dependencies
- README.md : this file

Quick start:
1. python -m venv venv
2. source venv/bin/activate   # or venv\Scripts\activate on Windows
3. pip install -r requirements.txt
4. python Flask_AutoWebsite.py
5. Visit http://127.0.0.1:5000

Admin:
- Default admin key: 'admin' (set env var FLASK_ADMIN_KEY to change)
- Simple demo admin only — do NOT use in production.

Customize the templates embedded in the single-file app to change layout/content.
