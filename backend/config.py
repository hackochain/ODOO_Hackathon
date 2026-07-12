import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    """
    Application Configuration
    """

    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "transitops-secret-key")

    # JWT
    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "transitops-jwt-secret-key"
    )

    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:password@localhost/transitops"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Uploads
    UPLOAD_FOLDER = "uploads"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

    # AI Settings
    AI_MODEL = "TransitOps AI Engine"

    # Report Settings
    REPORT_FOLDER = "reports"

    # Tracking
    GPS_REFRESH_INTERVAL = 10  # seconds

    # Analytics
    ANALYTICS_CACHE_TIMEOUT = 300  # seconds

    # Debug
    DEBUG = True