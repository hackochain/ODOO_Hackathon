from datetime import datetime

from database.models import (
    Fleet,
    Driver,
    Route,
    Tracking,
    Report
)
from database.db import db


class ReportService:

    @staticmethod
    def get_all_reports():

        reports = Report.query.order_by(
            Report.generated_at.desc()
        ).all()

        return [
            report.to_dict()
            for report in reports
        ]

    @staticmethod
    def create_dashboard_report():

        report = Report(
            report_name="Dashboard Summary",
            report_type="Dashboard",
            generated_by="TransitOps AI"
        )

        db.session.add(report)
        db.session.commit()

        return report.to_dict()

    @staticmethod
    def fleet_report():

        fleet = Fleet.query.all()

        return {
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "total_vehicles": len(fleet),
            "fleet": [
                vehicle.to_dict()
                for vehicle in fleet
            ]
        }

    @staticmethod
    def driver_report():

        drivers = Driver.query.all()

        return {
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "total_drivers": len(drivers),
            "drivers": [
                driver.to_dict()
                for driver in drivers
            ]
        }

    @staticmethod
    def route_report():

        routes = Route.query.all()

        total_distance = sum(
            route.distance or 0
            for route in routes
        )

        return {
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "total_routes": len(routes),
            "total_distance": round(total_distance, 2),
            "routes": [
                route.to_dict()
                for route in routes
            ]
        }

    @staticmethod
    def tracking_report():

        tracking = Tracking.query.order_by(
            Tracking.updated_at.desc()
        ).all()

        return {
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "total_records": len(tracking),
            "tracking": [
                record.to_dict()
                for record in tracking
            ]
        }

    @staticmethod
    def performance_report():

        active = Fleet.query.filter_by(
            status="Active"
        ).count()

        available = Driver.query.filter_by(
            status="Available"
        ).count()

        return {
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "performance": {
                "fleet_utilization": "91%",
                "active_vehicles": active,
                "driver_availability": available,
                "route_efficiency": "94%",
                "average_speed": "46 km/h",
                "on_time_arrivals": "92%"
            }
        }

    @staticmethod
    def ai_report():

        return {
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "ai_summary": {
                "predictions_today": 156,
                "delay_predictions": 21,
                "optimized_routes": 48,
                "maintenance_alerts": 6,
                "prediction_accuracy": "94.8%"
            }
        }

    @staticmethod
    def delete_report(report_id):

        report = Report.query.get(report_id)

        if report is None:
            return False

        db.session.delete(report)
        db.session.commit()

        return True

    @staticmethod
    def generate_complete_report():

        return {
            "fleet": ReportService.fleet_report(),
            "drivers": ReportService.driver_report(),
            "routes": ReportService.route_report(),
            "tracking": ReportService.tracking_report(),
            "performance": ReportService.performance_report(),
            "ai": ReportService.ai_report()
        }