from datetime import datetime

from database.db import db
from database.models import Tracking


class TrackingService:

    @staticmethod
    def get_all():

        records = Tracking.query.order_by(
            Tracking.updated_at.desc()
        ).all()

        return [
            record.to_dict()
            for record in records
        ]

    @staticmethod
    def get_by_id(tracking_id):

        return Tracking.query.get(tracking_id)

    @staticmethod
    def get_vehicle_location(vehicle_number):

        return Tracking.query.filter_by(
            vehicle_number=vehicle_number
        ).order_by(
            Tracking.updated_at.desc()
        ).first()

    @staticmethod
    def create(data):

        tracking = Tracking(
            vehicle_number=data.get("vehicle_number"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            speed=data.get("speed")
        )

        db.session.add(tracking)
        db.session.commit()

        return tracking

    @staticmethod
    def update(tracking_id, data):

        tracking = Tracking.query.get(tracking_id)

        if tracking is None:
            return None

        tracking.vehicle_number = data.get(
            "vehicle_number",
            tracking.vehicle_number
        )

        tracking.latitude = data.get(
            "latitude",
            tracking.latitude
        )

        tracking.longitude = data.get(
            "longitude",
            tracking.longitude
        )

        tracking.speed = data.get(
            "speed",
            tracking.speed
        )

        db.session.commit()

        return tracking

    @staticmethod
    def delete(tracking_id):

        tracking = Tracking.query.get(tracking_id)

        if tracking is None:
            return False

        db.session.delete(tracking)
        db.session.commit()

        return True

    @staticmethod
    def latest_locations():

        records = Tracking.query.order_by(
            Tracking.updated_at.desc()
        ).all()

        vehicles = []

        for record in records:

            vehicles.append({

                "vehicle_number": record.vehicle_number,

                "latitude": record.latitude,

                "longitude": record.longitude,

                "speed": record.speed,

                "updated_at": record.updated_at.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

            })

        return vehicles

    @staticmethod
    def statistics():

        total = Tracking.query.count()

        latest = Tracking.query.order_by(
            Tracking.updated_at.desc()
        ).first()

        return {

            "total_tracking_records": total,

            "latest_update": (
                latest.updated_at.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                if latest else None
            )

        }

    @staticmethod
    def average_speed():

        records = Tracking.query.all()

        if not records:
            return 0

        speeds = [
            record.speed
            for record in records
            if record.speed is not None
        ]

        if not speeds:
            return 0

        return round(
            sum(speeds) / len(speeds),
            2
        )

    @staticmethod
    def tracking_summary():

        return {

            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "total_records": Tracking.query.count(),

            "average_speed": TrackingService.average_speed(),

            "active_vehicles": len(
                Tracking.query.all()
            )

        }