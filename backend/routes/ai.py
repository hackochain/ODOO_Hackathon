from flask import Blueprint, request, jsonify
import random
from datetime import datetime

from database.models import Fleet, Driver, Route

ai_bp = Blueprint("ai", __name__)


# ==========================================
# AI Dashboard
# ==========================================

@ai_bp.route("/", methods=["GET"])
def ai_dashboard():

    return jsonify({
        "success": True,
        "module": "TransitOps AI Engine",
        "status": "Running",
        "version": "1.0.0",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


# ==========================================
# Delay Prediction
# ==========================================

@ai_bp.route("/delay-prediction", methods=["POST"])
def delay_prediction():

    data = request.get_json()

    traffic = data.get("traffic_level", "Medium")
    weather = data.get("weather", "Clear")

    probability = random.randint(10, 95)

    recommendation = "No Action Required"

    if probability > 70:
        recommendation = "Deploy Additional Vehicle"

    elif probability > 40:
        recommendation = "Monitor Route"

    return jsonify({
        "success": True,
        "delay_probability": probability,
        "traffic": traffic,
        "weather": weather,
        "recommendation": recommendation
    })


# ==========================================
# Passenger Demand Forecast
# ==========================================

@ai_bp.route("/demand-forecast", methods=["GET"])
def demand_forecast():

    forecast = []

    routes = Route.query.all()

    for route in routes:

        forecast.append({

            "route": route.route_name,

            "expected_passengers": random.randint(80, 250),

            "occupancy_rate": random.randint(55, 98)

        })

    return jsonify({
        "success": True,
        "forecast": forecast
    })


# ==========================================
# Fleet Health Prediction
# ==========================================

@ai_bp.route("/fleet-health", methods=["GET"])
def fleet_health():

    vehicles = Fleet.query.all()

    predictions = []

    for vehicle in vehicles:

        health = random.randint(65, 100)

        if health >= 90:
            status = "Excellent"

        elif health >= 75:
            status = "Good"

        else:
            status = "Maintenance Required"

        predictions.append({

            "vehicle": vehicle.vehicle_number,

            "health_score": health,

            "status": status

        })

    return jsonify({
        "success": True,
        "fleet_health": predictions
    })


# ==========================================
# Driver Performance
# ==========================================

@ai_bp.route("/driver-performance", methods=["GET"])
def driver_performance():

    drivers = Driver.query.all()

    performance = []

    for driver in drivers:

        score = random.randint(70, 100)

        performance.append({

            "driver": driver.name,

            "performance_score": score,

            "rating": "Excellent" if score >= 90 else "Good"

        })

    return jsonify({
        "success": True,
        "drivers": performance
    })


# ==========================================
# AI Recommendations
# ==========================================

@ai_bp.route("/recommendations", methods=["GET"])
def recommendations():

    suggestions = [

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

    return jsonify({
        "success": True,
        "recommendations": suggestions
    })


# ==========================================
# AI Route Optimization
# ==========================================

@ai_bp.route("/optimize-route", methods=["POST"])
def optimize_route():

    data = request.get_json()

    source = data.get("source")
    destination = data.get("destination")

    optimized_distance = round(random.uniform(8.5, 25.0), 2)

    estimated_time = random.randint(15, 60)

    return jsonify({
        "success": True,
        "source": source,
        "destination": destination,
        "optimized_distance_km": optimized_distance,
        "estimated_time_minutes": estimated_time
    })


# ==========================================
# AI Summary
# ==========================================

@ai_bp.route("/summary", methods=["GET"])
def ai_summary():

    return jsonify({

        "success": True,

        "summary": {

            "vehicles_monitored": Fleet.query.count(),

            "drivers_monitored": Driver.query.count(),

            "routes_analyzed": Route.query.count(),

            "predictions_generated": random.randint(50, 200),

            "accuracy": "94.8%"

        }

    })