from database.db import db
from database.models import Tracking


class TrackingController:

    @staticmethod
    def get_all():

        records = Tracking.query.order_by(
            Tracking.updated_at.desc()
        ).all()

        return {
            "success": True,
            "count": len(records),
            "tracking": [
                record.to_dict()
                for record in records
            ]
        }, 200

    @staticmethod
    def get_by_id(tracking_id):

        record = Tracking.query.get(tracking_id)

        if record is None:
            return {
                "success": False,
                "message": "Tracking record not found."
            }, 404

        return {
            "success": True,
            "tracking": record.to_dict()
        }, 200

    @staticmethod
    def add(data):

        tracking = Tracking(
            vehicle_number=data.get("vehicle_number"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            speed=data.get("speed")
        )

        db.session.add(tracking)
        db.session.commit()

        return {
            "success": True,
            "message": "Tracking record created successfully.",
            "tracking": tracking.to_dict()
        }, 201

    @staticmethod
    def update(tracking_id, data):

        record = Tracking.query.get(tracking_id)

        if record is None:
            return {
                "success": False,
                "message": "Tracking record not found."
            }, 404

        record.vehicle_number = data.get(
            "vehicle_number",
            record.vehicle_number
        )

        record.latitude = data.get(
            "latitude",
            record.latitude
        )

        record.longitude = data.get(
            "longitude",
            record.longitude
        )

        record.speed = data.get(
            "speed",
            record.speed
        )

        db.session.commit()

        return {
            "success": True,
            "message": "Tracking updated successfully.",
            "tracking": record.to_dict()
        }, 200

    @staticmethod
    def delete(tracking_id):

        record = Tracking.query.get(tracking_id)

        if record is None:
            return {
                "success": False,
                "message": "Tracking record not found."
            }, 404

        db.session.delete(record)
        db.session.commit()

        return {
            "success": True,
            "message": "Tracking record deleted successfully."
        }, 200

    @staticmethod
    def get_vehicle_tracking(vehicle_number):

        record = Tracking.query.filter_by(
            vehicle_number=vehicle_number
        ).order_by(
            Tracking.updated_at.desc()
        ).first()

        if record is None:
            return {
                "success": False,
                "message": "Vehicle not found."
            }, 404

        return {
            "success": True,
            "tracking": record.to_dict()
        }, 200

    @staticmethod
    def live_tracking():

        records = Tracking.query.order_by(
            Tracking.updated_at.desc()
        ).all()

        live = []

        for record in records:

            live.append({
                "vehicle_number": record.vehicle_number,
                "latitude": record.latitude,
                "longitude": record.longitude,
                "speed": record.speed,
                "updated_at": record.updated_at.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            })

        return {
            "success": True,
            "vehicles": live
        }, 200

    @staticmethod
    def statistics():

        total = Tracking.query.count()

        latest = Tracking.query.order_by(
            Tracking.updated_at.desc()
        ).first()

        return {
            "success": True,
            "statistics": {
                "total_records": total,
                "latest_update": (
                    latest.updated_at.strftime("%Y-%m-%d %H:%M:%S")
                    if latest else None
                )
            }
        }, 200