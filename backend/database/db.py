from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy instance
db = SQLAlchemy()


def init_db(app):
    """
    Initialize the database with the Flask app.
    """

    db.init_app(app)

    with app.app_context():
        # Import models before creating tables
        from database import models

        # Create all tables if they don't exist
        db.create_all()

        print("✅ Database initialized successfully.")