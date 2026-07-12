from flask import Blueprint, jsonify
from sqlalchemy import func

from database.models import (
    Fleet,
    Driver,
    Route,
    Tracking
)

analytics_bp = Blueprint("analytics", __name__)


# ==========================================
# Dashboard Analytics
# ==========================================

@analytics_bp.route("/", methods=["GET"])
def analytics_dashboard():

    total_vehicles = Fleet.query.count()
    total_drivers = Driver.query.count()
    total_routes = Route.query.count()
    total_tracking = Tracking.query.count()

    active_vehicles = Fleet.query.filter_by(
        status="Active"
    ).count()

    inactive_vehicles = Fleet.query.filter_by(
        status="Inactive"
    ).count()

    available_drivers = Driver.query.filter_by(
        status="Available"
    ).count()

    busy_drivers = Driver.query.filter_by(
        status="Busy"
    ).count()

    return jsonify({
        "success": True,
        "analytics": {
            "vehicles": {
                "total": total_vehicles,
                "active": active_vehicles,
                "inactive": inactive_vehicles
            },
            "drivers": {
                "total": total_drivers,
                "available": available_drivers,
                "busy": busy_drivers
            },
            "routes": total_routes,
            "tracking_records": total_tracking
        }
    })


# ==========================================
# Fleet Analytics
# ==========================================

@analytics_bp.route("/fleet", methods=["GET"])
def fleet_analytics():

    fleet = Fleet.query.all()

    data = [
        {
            "vehicle_number": vehicle.vehicle_number,
            "type": vehicle.vehicle_type,
            "capacity": vehicle.capacity,
            "status": vehicle.status
        }
        for vehicle in fleet
    ]

    return jsonify({
        "success": True,
        "fleet": data
    })


# ==========================================
# Driver Analytics
# ==========================================

@analytics_bp.route("/drivers", methods=["GET"])
def driver_analytics():

    drivers = Driver.query.all()

    data = [
        {
            "name": driver.name,
            "vehicle": driver.assigned_vehicle,
            "status": driver.status
        }
        for driver in drivers
    ]

    return jsonify({
        "success": True,
        "drivers": data
    })


# ==========================================
# Route Analytics
# ==========================================

@analytics_bp.route("/routes", methods=["GET"])
def route_analytics():

    routes = Route.query.all()

    total_distance = sum(
        route.distance or 0
        for route in routes
    )

    average_distance = (
        total_distance / len(routes)
        if routes else 0
    )

    return jsonify({
        "success": True,
        "statistics": {
            "total_routes": len(routes),
            "total_distance": round(total_distance, 2),
            "average_distance": round(average_distance, 2)
        }
    })


# ==========================================
# Speed Analytics
# ==========================================

@analytics_bp.route("/speed", methods=["GET"])
def speed_analytics():

    average_speed = db_speed_average()

    return jsonify({
        "success": True,
        "average_speed": average_speed
    })


def db_speed_average():

    avg = (
        Tracking.query.with_entities(
            func.avg(Tracking.speed)
        ).scalar()
    )

    if avg is None:
        return 0

    return round(float(avg), 2)


# ==========================================
# Vehicle Status Summary
# ==========================================

@analytics_bp.route("/vehicle-status", methods=["GET"])
def vehicle_status():

    active = Fleet.query.filter_by(
        status="Active"
    ).count()

    inactive = Fleet.query.filter_by(
        status="Inactive"
    ).count()

    maintenance = Fleet.query.filter_by(
        status="Maintenance"
    ).count()

    return jsonify({
        "success": True,
        "status": {
            "active": active,
            "inactive": inactive,
            "maintenance": maintenance
        }
    })


# ==========================================
# Driver Status Summary
# ==========================================

@analytics_bp.route("/driver-status", methods=["GET"])
def driver_status():

    available = Driver.query.filter_by(
        status="Available"
    ).count()

    busy = Driver.query.filter_by(
        status="Busy"
    ).count()

    off_duty = Driver.query.filter_by(
        status="Off Duty"
    ).count()

    return jsonify({
        "success": True,
        "status": {
            "available": available,
            "busy": busy,
            "off_duty": off_duty
        }
    })


# ==========================================
# Tracking Analytics
# ==========================================

@analytics_bp.route("/tracking", methods=["GET"])
def tracking_analytics():

    latest = Tracking.query.order_by(
        Tracking.updated_at.desc()
    ).limit(10).all()

    data = [
        {
            "vehicle": item.vehicle_number,
            "speed": item.speed,
            "latitude": item.latitude,
            "longitude": item.longitude,
            "updated_at": item.updated_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }
        for item in latest
    ]

    return jsonify({
        "success": True,
        "tracking": data
    })