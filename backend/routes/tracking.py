from flask import Blueprint, request, jsonify
from datetime import datetime

from database.db import db
from database.models import Tracking

tracking_bp = Blueprint("tracking", __name__)


# ==========================================
# Get All Tracking Records
# ==========================================

@tracking_bp.route("/", methods=["GET"])
def get_tracking():

    records = Tracking.query.order_by(
        Tracking.updated_at.desc()
    ).all()

    return jsonify({
        "success": True,
        "count": len(records),
        "tracking": [record.to_dict() for record in records]
    })


# ==========================================
# Get Tracking By ID
# ==========================================

@tracking_bp.route("/<int:tracking_id>", methods=["GET"])
def get_tracking_record(tracking_id):

    record = Tracking.query.get(tracking_id)

    if record is None:
        return jsonify({
            "success": False,
            "message": "Tracking record not found."
        }), 404

    return jsonify({
        "success": True,
        "tracking": record.to_dict()
    })


# ==========================================
# Update Vehicle Location
# ==========================================

@tracking_bp.route("/update", methods=["POST"])
def update_location():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received."
        }), 400

    tracking = Tracking(
        vehicle_number=data.get("vehicle_number"),
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
        speed=data.get("speed")
    )

    db.session.add(tracking)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Vehicle location updated.",
        "tracking": tracking.to_dict()
    }), 201


# ==========================================
# Vehicle Current Location
# ==========================================

@tracking_bp.route("/vehicle/<string:vehicle_number>", methods=["GET"])
def vehicle_location(vehicle_number):

    record = Tracking.query.filter_by(
        vehicle_number=vehicle_number
    ).order_by(
        Tracking.updated_at.desc()
    ).first()

    if record is None:
        return jsonify({
            "success": False,
            "message": "Vehicle not found."
        }), 404

    return jsonify({
        "success": True,
        "tracking": record.to_dict()
    })


# ==========================================
# Delete Tracking Record
# ==========================================

@tracking_bp.route("/delete/<int:tracking_id>", methods=["DELETE"])
def delete_tracking(tracking_id):

    record = Tracking.query.get(tracking_id)

    if record is None:
        return jsonify({
            "success": False,
            "message": "Tracking record not found."
        }), 404

    db.session.delete(record)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Tracking record deleted successfully."
    })


# ==========================================
# Live Tracking Dashboard
# ==========================================

@tracking_bp.route("/live", methods=["GET"])
def live_tracking():

    vehicles = Tracking.query.order_by(
        Tracking.updated_at.desc()
    ).all()

    live_data = []

    for vehicle in vehicles:
        live_data.append({
            "vehicle_number": vehicle.vehicle_number,
            "latitude": vehicle.latitude,
            "longitude": vehicle.longitude,
            "speed": vehicle.speed,
            "last_updated": vehicle.updated_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        })

    return jsonify({
        "success": True,
        "vehicles": live_data
    })


# ==========================================
# Tracking Statistics
# ==========================================

@tracking_bp.route("/stats", methods=["GET"])
def tracking_statistics():

    total_records = Tracking.query.count()

    latest_record = Tracking.query.order_by(
        Tracking.updated_at.desc()
    ).first()

    return jsonify({
        "success": True,
        "statistics": {
            "total_tracking_records": total_records,
            "last_update": (
                latest_record.updated_at.strftime("%Y-%m-%d %H:%M:%S")
                if latest_record else None
            )
        }
    })