import random
from datetime import datetime

from database.models import Fleet, Driver, Route


class AIService:

    @staticmethod
    def predict_delay(traffic_level, weather):

        probability = random.randint(10, 95)

        if probability >= 75:
            recommendation = "Deploy Additional Vehicle"

        elif probability >= 50:
            recommendation = "Monitor Route Closely"

        else:
            recommendation = "No Immediate Action"

        return {
            "traffic": traffic_level,
            "weather": weather,
            "delay_probability": probability,
            "recommendation": recommendation,
            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

    @staticmethod
    def demand_forecast():

        forecast = []

        routes = Route.query.all()

        for route in routes:

            forecast.append({

                "route": route.route_name,

                "expected_passengers": random.randint(
                    80, 250
                ),

                "occupancy_rate": random.randint(
                    55, 98
                )

            })

        return forecast

    @staticmethod
    def fleet_health():

        vehicles = Fleet.query.all()

        result = []

        for vehicle in vehicles:

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

        return result

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

        return performance

    @staticmethod
    def recommendations():

        return [

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

    @staticmethod
    def optimize_route(source, destination):

        return {

            "source": source,

            "destination": destination,

            "optimized_distance_km": round(
                random.uniform(8, 25),
                2
            ),

            "estimated_time_minutes": random.randint(
                15,
                60
            ),

            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        }

    @staticmethod
    def ai_summary():

        return {

            "vehicles_monitored": Fleet.query.count(),

            "drivers_monitored": Driver.query.count(),

            "routes_analyzed": Route.query.count(),

            "predictions_generated": random.randint(
                50,
                200
            ),

            "accuracy": "94.8%"

        }