from datetime import datetime

from database.db import db
from database.models import (
    Fleet,
    Driver,
    Route,
    Tracking,
    Report
)


class ReportController:

    @staticmethod
    def get_all():

        reports = Report.query.order_by(
            Report.generated_at.desc()
        ).all()

        return {
            "success": True,
            "count": len(reports),
            "reports": [
                report.to_dict()
                for report in reports
            ]
        }, 200


    @staticmethod
    def generate_dashboard_report():

        report = Report(
            report_name="Dashboard Summary",
            report_type="Dashboard",
            generated_by="TransitOps AI"
        )

        db.session.add(report)
        db.session.commit()

        return {
            "success": True,
            "message": "Dashboard report generated successfully.",
            "report": report.to_dict()
        }, 201


    @staticmethod
    def fleet_report():

        fleet = Fleet.query.all()

        return {
            "success": True,
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "total_vehicles": len(fleet),
            "fleet": [
                vehicle.to_dict()
                for vehicle in fleet
            ]
        }, 200


    @staticmethod
    def driver_report():

        drivers = Driver.query.all()

        return {
            "success": True,
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "total_drivers": len(drivers),
            "drivers": [
                driver.to_dict()
                for driver in drivers
            ]
        }, 200


    @staticmethod
    def route_report():

        routes = Route.query.all()

        total_distance = sum(
            route.distance or 0
            for route in routes
        )

        return {
            "success": True,
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "total_routes": len(routes),
            "total_distance": round(total_distance, 2),
            "routes": [
                route.to_dict()
                for route in routes
            ]
        }, 200


    @staticmethod
    def tracking_report():

        tracking = Tracking.query.order_by(
            Tracking.updated_at.desc()
        ).all()

        return {
            "success": True,
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "total_records": len(tracking),
            "tracking": [
                record.to_dict()
                for record in tracking
            ]
        }, 200


    @staticmethod
    def performance_report():

        active_vehicles = Fleet.query.filter_by(
            status="Active"
        ).count()

        available_drivers = Driver.query.filter_by(
            status="Available"
        ).count()

        return {
            "success": True,
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "performance": {
                "fleet_utilization": "91%",
                "driver_availability": available_drivers,
                "active_vehicles": active_vehicles,
                "route_efficiency": "94%",
                "average_speed": "46 km/h",
                "on_time_arrivals": "92%"
            }
        }, 200


    @staticmethod
    def ai_report():

        return {
            "success": True,
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
        }, 200


    @staticmethod
    def delete(report_id):

        report = Report.query.get(report_id)

        if report is None:

            return {
                "success": False,
                "message": "Report not found."
            }, 404

        db.session.delete(report)
        db.session.commit()

        return {
            "success": True,
            "message": "Report deleted successfully."
        }, 200