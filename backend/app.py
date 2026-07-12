from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from database.db import init_db

# Route Blueprints
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.fleet import fleet_bp
from routes.drivers import drivers_bp
from routes.routes import routes_bp
from routes.tracking import tracking_bp
from routes.analytics import analytics_bp
from routes.ai import ai_bp
from routes.reports import reports_bp
from routes.settings import settings_bp


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # JWT Authentication
    JWTManager(app)

    # Initialize Database
    init_db(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
    app.register_blueprint(fleet_bp, url_prefix="/api/fleet")
    app.register_blueprint(drivers_bp, url_prefix="/api/drivers")
    app.register_blueprint(routes_bp, url_prefix="/api/routes")
    app.register_blueprint(tracking_bp, url_prefix="/api/tracking")
    app.register_blueprint(analytics_bp, url_prefix="/api/analytics")
    app.register_blueprint(ai_bp, url_prefix="/api/ai")
    app.register_blueprint(reports_bp, url_prefix="/api/reports")
    app.register_blueprint(settings_bp, url_prefix="/api/settings")

    @app.route("/")
    def home():
        return {
            "project": "TransitOps Backend",
            "status": "Running",
            "version": "1.0.0"
        }

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )