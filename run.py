from app import create_app, db

app = create_app()

# ✅ Automatically create database if missing
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
