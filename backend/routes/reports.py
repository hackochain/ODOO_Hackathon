from flask import Blueprint, jsonify
from datetime import datetime

from database.models import (
    Fleet,
    Driver,
    Route,
    Tracking,
    Report
)
from database.db import db

reports_bp = Blueprint("reports", __name__)


# ==========================================
# Get All Reports
# ==========================================

@reports_bp.route("/", methods=["GET"])
def get_reports():

    reports = Report.query.order_by(
        Report.generated_at.desc()
    ).all()

    return jsonify({
        "success": True,
        "count": len(reports),
        "reports": [report.to_dict() for report in reports]
    })


# ==========================================
# Generate Dashboard Report
# ==========================================

@reports_bp.route("/dashboard", methods=["POST"])
def generate_dashboard_report():

    report = Report(
        report_name="Dashboard Summary",
        report_type="Dashboard",
        generated_by="TransitOps AI"
    )

    db.session.add(report)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Dashboard report generated successfully.",
        "report": report.to_dict()
    })


# ==========================================
# Fleet Report
# ==========================================

@reports_bp.route("/fleet", methods=["GET"])
def fleet_report():

    fleet = Fleet.query.all()

    return jsonify({
        "success": True,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_vehicles": len(fleet),
        "fleet": [vehicle.to_dict() for vehicle in fleet]
    })


# ==========================================
# Driver Report
# ==========================================

@reports_bp.route("/drivers", methods=["GET"])
def driver_report():

    drivers = Driver.query.all()

    return jsonify({
        "success": True,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_drivers": len(drivers),
        "drivers": [driver.to_dict() for driver in drivers]
    })


# ==========================================
# Route Report
# ==========================================

@reports_bp.route("/routes", methods=["GET"])
def route_report():

    routes = Route.query.all()

    total_distance = sum(
        route.distance or 0
        for route in routes
    )

    return jsonify({
        "success": True,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_routes": len(routes),
        "total_distance": round(total_distance, 2),
        "routes": [route.to_dict() for route in routes]
    })


# ==========================================
# Tracking Report
# ==========================================

@reports_bp.route("/tracking", methods=["GET"])
def tracking_report():

    tracking = Tracking.query.order_by(
        Tracking.updated_at.desc()
    ).all()

    return jsonify({
        "success": True,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_records": len(tracking),
        "tracking": [item.to_dict() for item in tracking]
    })


# ==========================================
# Performance Report
# ==========================================

@reports_bp.route("/performance", methods=["GET"])
def performance_report():

    active_vehicles = Fleet.query.filter_by(
        status="Active"
    ).count()

    available_drivers = Driver.query.filter_by(
        status="Available"
    ).count()

    return jsonify({
        "success": True,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "performance": {
            "fleet_utilization": "91%",
            "driver_availability": available_drivers,
            "active_vehicles": active_vehicles,
            "route_efficiency": "94%",
            "average_speed": "46 km/h",
            "on_time_arrivals": "92%"
        }
    })


# ==========================================
# AI Report
# ==========================================

@reports_bp.route("/ai", methods=["GET"])
def ai_report():

    return jsonify({
        "success": True,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ai_summary": {
            "predictions_today": 156,
            "delay_predictions": 21,
            "optimized_routes": 48,
            "maintenance_alerts": 6,
            "prediction_accuracy": "94.8%"
        }
    })


# ==========================================
# Delete Report
# ==========================================

@reports_bp.route("/delete/<int:report_id>", methods=["DELETE"])
def delete_report(report_id):

    report = Report.query.get(report_id)

    if report is None:
        return jsonify({
            "success": False,
            "message": "Report not found."
        }), 404

    db.session.delete(report)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Report deleted successfully."
    })