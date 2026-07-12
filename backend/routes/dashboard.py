from flask import Blueprint, jsonify

from database.models import (
    Fleet,
    Driver,
    Route,
    Tracking,
    Report
)

dashboard_bp = Blueprint("dashboard", __name__)


# ==========================================
# Dashboard Overview
# ==========================================

@dashboard_bp.route("/", methods=["GET"])
def dashboard():

    total_fleet = Fleet.query.count()
    total_drivers = Driver.query.count()
    total_routes = Route.query.count()
    total_tracking = Tracking.query.count()
    total_reports = Report.query.count()

    active_fleet = Fleet.query.filter_by(
        status="Active"
    ).count()

    available_drivers = Driver.query.filter_by(
        status="Available"
    ).count()

    return jsonify({
        "success": True,

        "dashboard": {

            "fleet": {
                "total": total_fleet,
                "active": active_fleet
            },

            "drivers": {
                "total": total_drivers,
                "available": available_drivers
            },

            "routes": total_routes,

            "tracking_records": total_tracking,

            "reports": total_reports

        }

    })


# ==========================================
# Dashboard Statistics
# ==========================================

@dashboard_bp.route("/stats", methods=["GET"])
def dashboard_stats():

    return jsonify({

        "success": True,

        "statistics": {

            "today_trips": 248,

            "completed_trips": 229,

            "delayed_trips": 19,

            "fuel_efficiency": "91%",

            "vehicle_utilization": "87%",

            "passenger_satisfaction": "95%"

        }

    })


# ==========================================
# Recent Activity
# ==========================================

@dashboard_bp.route("/activity", methods=["GET"])
def recent_activity():

    activities = [

        {
            "time": "10:20 AM",
            "activity": "Bus TN-45-AA-1023 departed from Central Station."
        },

        {
            "time": "10:45 AM",
            "activity": "Driver Ravi Kumar completed Route R12."
        },

        {
            "time": "11:00 AM",
            "activity": "Maintenance scheduled for Bus TN-45-AA-1088."
        },

        {
            "time": "11:15 AM",
            "activity": "AI predicted traffic congestion on Route R08."
        }

    ]

    return jsonify({

        "success": True,

        "activities": activities

    })


# ==========================================
# Notifications
# ==========================================

@dashboard_bp.route("/notifications", methods=["GET"])
def notifications():

    notifications = [

        {
            "type": "warning",
            "message": "Vehicle TN-45-AA-1088 requires maintenance."
        },

        {
            "type": "info",
            "message": "Passenger demand increased by 18% today."
        },

        {
            "type": "success",
            "message": "All GPS tracking devices are online."
        }

    ]

    return jsonify({

        "success": True,

        "notifications": notifications

    })