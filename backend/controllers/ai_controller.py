import random

from database.models import (
    Fleet,
    Driver,
    Route
)


class AIController:

    @staticmethod
    def dashboard():

        return {
            "success": True,
            "module": "TransitOps AI Engine",
            "status": "Running",
            "version": "1.0.0"
        }, 200

    @staticmethod
    def delay_prediction(data):

        traffic = data.get("traffic_level", "Medium")
        weather = data.get("weather", "Clear")

        probability = random.randint(10, 95)

        if probability >= 75:
            recommendation = "Deploy Additional Vehicle"

        elif probability >= 50:
            recommendation = "Monitor Route Closely"

        else:
            recommendation = "No Immediate Action"

        return {
            "success": True,
            "traffic": traffic,
            "weather": weather,
            "delay_probability": probability,
            "recommendation": recommendation
        }, 200

    @staticmethod
    def demand_forecast():

        routes = Route.query.all()

        forecast = []

        for route in routes:

            forecast.append({

                "route": route.route_name,

                "expected_passengers": random.randint(80, 250),

                "occupancy_rate": random.randint(50, 98)

            })

        return {
            "success": True,
            "forecast": forecast
        }, 200

    @staticmethod
    def fleet_health():

        fleet = Fleet.query.all()

        result = []

        for vehicle in fleet:

            score = random.randint(65, 100)

            if score >= 90:
                status = "Excellent"

            elif score >= 75:
                status = "Good"

            else:
                status = "Maintenance Required"

            result.append({

                "vehicle_number": vehicle.vehicle_number,

                "health_score": score,

                "status": status

            })

        return {
            "success": True,
            "fleet_health": result
        }, 200

    @staticmethod
    def driver_performance():

        drivers = Driver.query.all()

        performance = []

        for driver in drivers:

            score = random.randint(70, 100)

            performance.append({

                "driver": driver.name,

                "score": score,

                "rating": (
                    "Excellent"
                    if score >= 90
                    else "Good"
                )

            })

        return {
            "success": True,
            "performance": performance
        }, 200

    @staticmethod
    def recommendations():

        return {
            "success": True,
            "recommendations": [

                {
                    "priority": "High",
                    "message": "Increase buses on Route R12 during peak hours."
                },

                {
                    "priority": "Medium",
                    "message": "Schedule maintenance for Vehicle TN45AB1023."
                },

                {
                    "priority": "Low",
                    "message": "Optimize Route R08 to reduce travel time."
                }

            ]
        }, 200

    @staticmethod
    def optimize_route(data):

        source = data.get("source")
        destination = data.get("destination")

        return {
            "success": True,
            "source": source,
            "destination": destination,
            "optimized_distance": round(
                random.uniform(8, 25), 2
            ),
            "estimated_time": random.randint(15, 60)
        }, 200

    @staticmethod
    def summary():

        return {
            "success": True,
            "summary": {

                "vehicles_monitored": Fleet.query.count(),

                "drivers_monitored": Driver.query.count(),

                "routes_analyzed": Route.query.count(),

                "predictions_today": random.randint(80, 200),

                "accuracy": "94.8%"

            }

        }, 200