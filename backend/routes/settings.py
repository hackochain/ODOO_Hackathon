from flask import Blueprint, request, jsonify

settings_bp = Blueprint("settings", __name__)

# In-memory settings (replace with DB storage in production)
app_settings = {
    "organization_name": "TransitOps",
    "admin_email": "admin@transitops.com",
    "theme": "dark",
    "language": "English",
    "timezone": "Asia/Kolkata",
    "notifications": True,
    "gps_refresh_interval": 10,
    "ai_enabled": True,
    "maintenance_alerts": True,
    "report_auto_generate": False
}


# ==========================================
# Get All Settings
# ==========================================

@settings_bp.route("/", methods=["GET"])
def get_settings():

    return jsonify({
        "success": True,
        "settings": app_settings
    })


# ==========================================
# Update Settings
# ==========================================

@settings_bp.route("/update", methods=["PUT"])
def update_settings():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received."
        }), 400

    for key, value in data.items():

        if key in app_settings:
            app_settings[key] = value

    return jsonify({
        "success": True,
        "message": "Settings updated successfully.",
        "settings": app_settings
    })


# ==========================================
# Reset Settings
# ==========================================

@settings_bp.route("/reset", methods=["POST"])
def reset_settings():

    global app_settings

    app_settings = {
        "organization_name": "TransitOps",
        "admin_email": "admin@transitops.com",
        "theme": "dark",
        "language": "English",
        "timezone": "Asia/Kolkata",
        "notifications": True,
        "gps_refresh_interval": 10,
        "ai_enabled": True,
        "maintenance_alerts": True,
        "report_auto_generate": False
    }

    return jsonify({
        "success": True,
        "message": "Settings reset successfully.",
        "settings": app_settings
    })


# ==========================================
# Change Theme
# ==========================================

@settings_bp.route("/theme", methods=["PUT"])
def change_theme():

    data = request.get_json()

    theme = data.get("theme")

    if theme not in ["light", "dark"]:
        return jsonify({
            "success": False,
            "message": "Invalid theme."
        }), 400

    app_settings["theme"] = theme

    return jsonify({
        "success": True,
        "message": "Theme updated successfully.",
        "theme": theme
    })


# ==========================================
# Toggle Notifications
# ==========================================

@settings_bp.route("/notifications", methods=["PUT"])
def toggle_notifications():

    data = request.get_json()

    enabled = bool(data.get("enabled", True))

    app_settings["notifications"] = enabled

    return jsonify({
        "success": True,
        "notifications": enabled
    })


# ==========================================
# AI Settings
# ==========================================

@settings_bp.route("/ai", methods=["PUT"])
def ai_settings():

    data = request.get_json()

    app_settings["ai_enabled"] = bool(
        data.get("ai_enabled", True)
    )

    return jsonify({
        "success": True,
        "ai_enabled": app_settings["ai_enabled"]
    })


# ==========================================
# GPS Settings
# ==========================================

@settings_bp.route("/gps", methods=["PUT"])
def gps_settings():

    data = request.get_json()

    interval = int(
        data.get("gps_refresh_interval", 10)
    )

    app_settings["gps_refresh_interval"] = interval

    return jsonify({
        "success": True,
        "gps_refresh_interval": interval
    })


# ==========================================
# System Information
# ==========================================

@settings_bp.route("/system", methods=["GET"])
def system_info():

    return jsonify({
        "success": True,
        "system": {
            "application": "TransitOps",
            "version": "1.0.0",
            "backend": "Flask",
            "database": "MySQL",
            "python": "3.x",
            "status": "Running"
        }
    })