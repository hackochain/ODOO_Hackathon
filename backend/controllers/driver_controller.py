from database.db import db
from database.models import Driver


class DriverController:

    @staticmethod
    def get_all():

        drivers = Driver.query.all()

        return {
            "success": True,
            "count": len(drivers),
            "drivers": [
                driver.to_dict()
                for driver in drivers
            ]
        }, 200


    @staticmethod
    def get_by_id(driver_id):

        driver = Driver.query.get(driver_id)

        if driver is None:
            return {
                "success": False,
                "message": "Driver not found."
            }, 404

        return {
            "success": True,
            "driver": driver.to_dict()
        }, 200


    @staticmethod
    def add(data):

        existing = Driver.query.filter_by(
            license_number=data.get("license_number")
        ).first()

        if existing:
            return {
                "success": False,
                "message": "License number already exists."
            }, 409

        driver = Driver(
            name=data.get("name"),
            license_number=data.get("license_number"),
            phone=data.get("phone"),
            assigned_vehicle=data.get("assigned_vehicle"),
            status=data.get("status", "Available")
        )

        db.session.add(driver)
        db.session.commit()

        return {
            "success": True,
            "message": "Driver added successfully.",
            "driver": driver.to_dict()
        }, 201


    @staticmethod
    def update(driver_id, data):

        driver = Driver.query.get(driver_id)

        if driver is None:
            return {
                "success": False,
                "message": "Driver not found."
            }, 404

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

        return {
            "success": True,
            "message": "Driver updated successfully.",
            "driver": driver.to_dict()
        }, 200


    @staticmethod
    def delete(driver_id):

        driver = Driver.query.get(driver_id)

        if driver is None:
            return {
                "success": False,
                "message": "Driver not found."
            }, 404

        db.session.delete(driver)
        db.session.commit()

        return {
            "success": True,
            "message": "Driver deleted successfully."
        }, 200


    @staticmethod
    def available():

        drivers = Driver.query.filter_by(
            status="Available"
        ).all()

        return {
            "success": True,
            "count": len(drivers),
            "drivers": [
                driver.to_dict()
                for driver in drivers
            ]
        }, 200


    @staticmethod
    def busy():

        drivers = Driver.query.filter_by(
            status="Busy"
        ).all()

        return {
            "success": True,
            "count": len(drivers),
            "drivers": [
                driver.to_dict()
                for driver in drivers
            ]
        }, 200


    @staticmethod
    def statistics():

        total = Driver.query.count()

        available = Driver.query.filter_by(
            status="Available"
        ).count()

        busy = Driver.query.filter_by(
            status="Busy"
        ).count()

        off_duty = Driver.query.filter_by(
            status="Off Duty"
        ).count()

        return {
            "success": True,
            "statistics": {
                "total": total,
                "available": available,
                "busy": busy,
                "off_duty": off_duty
            }
        }, 200