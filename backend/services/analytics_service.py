from sqlalchemy import func

from database.models import (
    Fleet,
    Driver,
    Route,
    Tracking
)


class AnalyticsService:

    @staticmethod
    def dashboard():

        return {
            "total_vehicles": Fleet.query.count(),
            "active_vehicles": Fleet.query.filter_by(
                status="Active"
            ).count(),
            "inactive_vehicles": Fleet.query.filter_by(
                status="Inactive"
            ).count(),

            "total_drivers": Driver.query.count(),
            "available_drivers": Driver.query.filter_by(
                status="Available"
            ).count(),
            "busy_drivers": Driver.query.filter_by(
                status="Busy"
            ).count(),

            "total_routes": Route.query.count(),
            "tracking_records": Tracking.query.count()
        }

    @staticmethod
    def fleet_statistics():

        vehicles = Fleet.query.all()

        return [
            {
                "vehicle_number": vehicle.vehicle_number,
                "vehicle_type": vehicle.vehicle_type,
                "capacity": vehicle.capacity,
                "status": vehicle.status
            }
            for vehicle in vehicles
        ]

    @staticmethod
    def driver_statistics():

        drivers = Driver.query.all()

        return [
            {
                "name": driver.name,
                "assigned_vehicle": driver.assigned_vehicle,
                "status": driver.status
            }
            for driver in drivers
        ]

    @staticmethod
    def route_statistics():

        routes = Route.query.all()

        total_distance = sum(
            route.distance or 0
            for route in routes
        )

        average_distance = (
            total_distance / len(routes)
            if routes else 0
        )

        return {
            "total_routes": len(routes),
            "total_distance": round(total_distance, 2),
            "average_distance": round(average_distance, 2)
        }

    @staticmethod
    def average_speed():

        average = Tracking.query.with_entities(
            func.avg(Tracking.speed)
        ).scalar()

        if average is None:
            return 0

        return round(float(average), 2)

    @staticmethod
    def vehicle_status_summary():

        return {
            "active": Fleet.query.filter_by(
                status="Active"
            ).count(),

            "inactive": Fleet.query.filter_by(
                status="Inactive"
            ).count(),

            "maintenance": Fleet.query.filter_by(
                status="Maintenance"
            ).count()
        }

    @staticmethod
    def driver_status_summary():

        return {
            "available": Driver.query.filter_by(
                status="Available"
            ).count(),

            "busy": Driver.query.filter_by(
                status="Busy"
            ).count(),

            "off_duty": Driver.query.filter_by(
                status="Off Duty"
            ).count()
        }

    @staticmethod
    def latest_tracking(limit=10):

        tracking = Tracking.query.order_by(
            Tracking.updated_at.desc()
        ).limit(limit).all()

        return [
            {
                "vehicle_number": item.vehicle_number,
                "latitude": item.latitude,
                "longitude": item.longitude,
                "speed": item.speed,
                "updated_at": item.updated_at.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            }
            for item in tracking
        ]

    @staticmethod
    def analytics_summary():

        return {
            "dashboard": AnalyticsService.dashboard(),
            "route_statistics": AnalyticsService.route_statistics(),
            "average_speed": AnalyticsService.average_speed(),
            "vehicle_status": AnalyticsService.vehicle_status_summary(),
            "driver_status": AnalyticsService.driver_status_summary()
        }