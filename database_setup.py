from app import app, db

print("Starting table creation...")  #Debug line

with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")
