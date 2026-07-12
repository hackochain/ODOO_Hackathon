from database.db import db
from database.models import Fleet


class FleetController:

    @staticmethod
    def get_all():

        vehicles = Fleet.query.all()

        return {
            "success": True,
            "count": len(vehicles),
            "fleet": [
                vehicle.to_dict()
                for vehicle in vehicles
            ]
        }, 200


    @staticmethod
    def get_by_id(vehicle_id):

        vehicle = Fleet.query.get(vehicle_id)

        if vehicle is None:
            return {
                "success": False,
                "message": "Vehicle not found."
            }, 404

        return {
            "success": True,
            "vehicle": vehicle.to_dict()
        }, 200


    @staticmethod
    def add(data):

        existing = Fleet.query.filter_by(
            vehicle_number=data.get("vehicle_number")
        ).first()

        if existing:
            return {
                "success": False,
                "message": "Vehicle already exists."
            }, 409

        vehicle = Fleet(
            vehicle_number=data.get("vehicle_number"),
            vehicle_type=data.get("vehicle_type"),
            capacity=data.get("capacity"),
            status=data.get("status", "Active")
        )

        db.session.add(vehicle)
        db.session.commit()

        return {
            "success": True,
            "message": "Vehicle added successfully.",
            "vehicle": vehicle.to_dict()
        }, 201


    @staticmethod
    def update(vehicle_id, data):

        vehicle = Fleet.query.get(vehicle_id)

        if vehicle is None:
            return {
                "success": False,
                "message": "Vehicle not found."
            }, 404

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

        return {
            "success": True,
            "message": "Vehicle updated successfully.",
            "vehicle": vehicle.to_dict()
        }, 200


    @staticmethod
    def delete(vehicle_id):

        vehicle = Fleet.query.get(vehicle_id)

        if vehicle is None:
            return {
                "success": False,
                "message": "Vehicle not found."
            }, 404

        db.session.delete(vehicle)
        db.session.commit()

        return {
            "success": True,
            "message": "Vehicle deleted successfully."
        }, 200


    @staticmethod
    def get_active():

        vehicles = Fleet.query.filter_by(
            status="Active"
        ).all()

        return {
            "success": True,
            "count": len(vehicles),
            "fleet": [
                vehicle.to_dict()
                for vehicle in vehicles
            ]
        }, 200


    @staticmethod
    def get_inactive():

        vehicles = Fleet.query.filter_by(
            status="Inactive"
        ).all()

        return {
            "success": True,
            "count": len(vehicles),
            "fleet": [
                vehicle.to_dict()
                for vehicle in vehicles
            ]
        }, 200


    @staticmethod
    def statistics():

        total = Fleet.query.count()

        active = Fleet.query.filter_by(
            status="Active"
        ).count()

        inactive = Fleet.query.filter_by(
            status="Inactive"
        ).count()

        maintenance = Fleet.query.filter_by(
            status="Maintenance"
        ).count()

        return {
            "success": True,
            "statistics": {
                "total": total,
                "active": active,
                "inactive": inactive,
                "maintenance": maintenance
            }
        }, 200