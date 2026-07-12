from flask import Blueprint, request, jsonify

from database.db import db
from database.models import Driver

drivers_bp = Blueprint("drivers", __name__)


# ==========================================
# Get All Drivers
# ==========================================

@drivers_bp.route("/", methods=["GET"])
def get_drivers():

    drivers = Driver.query.all()

    return jsonify({
        "success": True,
        "count": len(drivers),
        "drivers": [driver.to_dict() for driver in drivers]
    })


# ==========================================
# Get Driver By ID
# ==========================================

@drivers_bp.route("/<int:driver_id>", methods=["GET"])
def get_driver(driver_id):

    driver = Driver.query.get(driver_id)

    if driver is None:
        return jsonify({
            "success": False,
            "message": "Driver not found."
        }), 404

    return jsonify({
        "success": True,
        "driver": driver.to_dict()
    })


# ==========================================
# Add Driver
# ==========================================

@drivers_bp.route("/add", methods=["POST"])
def add_driver():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received."
        }), 400

    if Driver.query.filter_by(
        license_number=data.get("license_number")
    ).first():

        return jsonify({
            "success": False,
            "message": "License number already exists."
        }), 409

    driver = Driver(
        name=data.get("name"),
        license_number=data.get("license_number"),
        phone=data.get("phone"),
        assigned_vehicle=data.get("assigned_vehicle"),
        status=data.get("status", "Available")
    )

    db.session.add(driver)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Driver added successfully.",
        "driver": driver.to_dict()
    }), 201


# ==========================================
# Update Driver
# ==========================================

@drivers_bp.route("/update/<int:driver_id>", methods=["PUT"])
def update_driver(driver_id):

    driver = Driver.query.get(driver_id)

    if driver is None:
        return jsonify({
            "success": False,
            "message": "Driver not found."
        }), 404

    data = request.get_json()

    driver.name = data.get(
        "name",
        driver.name
    )

    driver.phone = data.get(
        "phone",
        driver.phone
    )

    driver.assigned_vehicle = data.get(
        "assigned_vehicle",
        driver.assigned_vehicle
    )

    driver.status = data.get(
        "status",
        driver.status
    )

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Driver updated successfully.",
        "driver": driver.to_dict()
    })


# ==========================================
# Delete Driver
# ==========================================

@drivers_bp.route("/delete/<int:driver_id>", methods=["DELETE"])
def delete_driver(driver_id):

    driver = Driver.query.get(driver_id)

    if driver is None:
        return jsonify({
            "success": False,
            "message": "Driver not found."
        }), 404

    db.session.delete(driver)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Driver deleted successfully."
    })


# ==========================================
# Available Drivers
# ==========================================

@drivers_bp.route("/available", methods=["GET"])
def available_drivers():

    drivers = Driver.query.filter_by(
        status="Available"
    ).all()

    return jsonify({
        "success": True,
        "count": len(drivers),
        "drivers": [driver.to_dict() for driver in drivers]
    })


# ==========================================
# Busy Drivers
# ==========================================

@drivers_bp.route("/busy", methods=["GET"])
def busy_drivers():

    drivers = Driver.query.filter_by(
        status="Busy"
    ).all()

    return jsonify({
        "success": True,
        "count": len(drivers),
        "drivers": [driver.to_dict() for driver in drivers]
    })