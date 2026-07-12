from flask import Blueprint, request, jsonify

from database.db import db
from database.models import Fleet

fleet_bp = Blueprint("fleet", __name__)


# ==========================================
# Get All Vehicles
# ==========================================

@fleet_bp.route("/", methods=["GET"])
def get_fleet():

    vehicles = Fleet.query.all()

    return jsonify({
        "success": True,
        "count": len(vehicles),
        "fleet": [vehicle.to_dict() for vehicle in vehicles]
    })


# ==========================================
# Get Single Vehicle
# ==========================================

@fleet_bp.route("/<int:vehicle_id>", methods=["GET"])
def get_vehicle(vehicle_id):

    vehicle = Fleet.query.get(vehicle_id)

    if vehicle is None:
        return jsonify({
            "success": False,
            "message": "Vehicle not found."
        }), 404

    return jsonify({
        "success": True,
        "vehicle": vehicle.to_dict()
    })


# ==========================================
# Add Vehicle
# ==========================================

@fleet_bp.route("/add", methods=["POST"])
def add_vehicle():

    data = request.get_json()

    vehicle_number = data.get("vehicle_number")

    if Fleet.query.filter_by(vehicle_number=vehicle_number).first():
        return jsonify({
            "success": False,
            "message": "Vehicle already exists."
        }), 409

    vehicle = Fleet(
        vehicle_number=vehicle_number,
        vehicle_type=data.get("vehicle_type"),
        capacity=data.get("capacity"),
        status=data.get("status", "Active")
    )

    db.session.add(vehicle)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Vehicle added successfully.",
        "vehicle": vehicle.to_dict()
    }), 201


# ==========================================
# Update Vehicle
# ==========================================

@fleet_bp.route("/update/<int:vehicle_id>", methods=["PUT"])
def update_vehicle(vehicle_id):

    vehicle = Fleet.query.get(vehicle_id)

    if vehicle is None:
        return jsonify({
            "success": False,
            "message": "Vehicle not found."
        }), 404

    data = request.get_json()

    vehicle.vehicle_number = data.get(
        "vehicle_number",
        vehicle.vehicle_number
    )

    vehicle.vehicle_type = data.get(
        "vehicle_type",
        vehicle.vehicle_type
    )

    vehicle.capacity = data.get(
        "capacity",
        vehicle.capacity
    )

    vehicle.status = data.get(
        "status",
        vehicle.status
    )

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Vehicle updated successfully.",
        "vehicle": vehicle.to_dict()
    })


# ==========================================
# Delete Vehicle
# ==========================================

@fleet_bp.route("/delete/<int:vehicle_id>", methods=["DELETE"])
def delete_vehicle(vehicle_id):

    vehicle = Fleet.query.get(vehicle_id)

    if vehicle is None:
        return jsonify({
            "success": False,
            "message": "Vehicle not found."
        }), 404

    db.session.delete(vehicle)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Vehicle deleted successfully."
    })


# ==========================================
# Active Vehicles
# ==========================================

@fleet_bp.route("/active", methods=["GET"])
def active_vehicles():

    vehicles = Fleet.query.filter_by(status="Active").all()

    return jsonify({
        "success": True,
        "count": len(vehicles),
        "fleet": [vehicle.to_dict() for vehicle in vehicles]
    })


# ==========================================
# Inactive Vehicles
# ==========================================

@fleet_bp.route("/inactive", methods=["GET"])
def inactive_vehicles():

    vehicles = Fleet.query.filter_by(status="Inactive").all()

    return jsonify({
        "success": True,
        "count": len(vehicles),
        "fleet": [vehicle.to_dict() for vehicle in vehicles]
    })