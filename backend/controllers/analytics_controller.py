from sqlalchemy import func

from database.models import (
    Fleet,
    Driver,
    Route,
    Tracking
)


class AnalyticsController:

    @staticmethod
    def dashboard():

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

        return {
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
        }, 200

    @staticmethod
    def fleet():

        vehicles = Fleet.query.all()

        return {
            "success": True,
            "fleet": [
                {
                    "vehicle_number": vehicle.vehicle_number,
                    "type": vehicle.vehicle_type,
                    "capacity": vehicle.capacity,
                    "status": vehicle.status
                }
                for vehicle in vehicles
            ]
        }, 200

    @staticmethod
    def drivers():

        drivers = Driver.query.all()

        return {
            "success": True,
            "drivers": [
                {
                    "name": driver.name,
                    "assigned_vehicle": driver.assigned_vehicle,
                    "status": driver.status
                }
                for driver in drivers
            ]
        }, 200

    @staticmethod
    def routes():

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
            "success": True,
            "statistics": {
                "total_routes": len(routes),
                "total_distance": round(total_distance, 2),
                "average_distance": round(average_distance, 2)
            }
        }, 200

    @staticmethod
    def average_speed():

        average = Tracking.query.with_entities(
            func.avg(Tracking.speed)
        ).scalar()

        return {
            "success": True,
            "average_speed": round(float(average), 2)
            if average else 0
        }, 200

    @staticmethod
    def vehicle_status():

        return {
            "success": True,
            "status": {
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
        }, 200

    @staticmethod
    def driver_status():

        return {
            "success": True,
            "status": {
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
        }, 200

    @staticmethod
    def tracking_summary():

        tracking = Tracking.query.order_by(
            Tracking.updated_at.desc()
        ).limit(10).all()

        return {
            "success": True,
            "tracking": [
                {
                    "vehicle": item.vehicle_number,
                    "speed": item.speed,
                    "latitude": item.latitude,
                    "longitude": item.longitude,
                    "updated_at": item.updated_at.strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                }
                for item in tracking
            ]
        }, 200