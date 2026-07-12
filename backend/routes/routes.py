from flask import Blueprint, request, jsonify

from database.db import db
from database.models import Route

routes_bp = Blueprint("routes", __name__)


# ==========================================
# Get All Routes
# ==========================================

@routes_bp.route("/", methods=["GET"])
def get_routes():

    routes = Route.query.all()

    return jsonify({
        "success": True,
        "count": len(routes),
        "routes": [route.to_dict() for route in routes]
    })


# ==========================================
# Get Route By ID
# ==========================================

@routes_bp.route("/<int:route_id>", methods=["GET"])
def get_route(route_id):

    route = Route.query.get(route_id)

    if route is None:
        return jsonify({
            "success": False,
            "message": "Route not found."
        }), 404

    return jsonify({
        "success": True,
        "route": route.to_dict()
    })


# ==========================================
# Add Route
# ==========================================

@routes_bp.route("/add", methods=["POST"])
def add_route():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received."
        }), 400

    route = Route(
        route_name=data.get("route_name"),
        source=data.get("source"),
        destination=data.get("destination"),
        distance=data.get("distance"),
        estimated_time=data.get("estimated_time")
    )

    db.session.add(route)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Route added successfully.",
        "route": route.to_dict()
    }), 201


# ==========================================
# Update Route
# ==========================================

@routes_bp.route("/update/<int:route_id>", methods=["PUT"])
def update_route(route_id):

    route = Route.query.get(route_id)

    if route is None:
        return jsonify({
            "success": False,
            "message": "Route not found."
        }), 404

    data = request.get_json()

    route.route_name = data.get(
        "route_name",
        route.route_name
    )

    route.source = data.get(
        "source",
        route.source
    )

    route.destination = data.get(
        "destination",
        route.destination
    )

    route.distance = data.get(
        "distance",
        route.distance
    )

    route.estimated_time = data.get(
        "estimated_time",
        route.estimated_time
    )

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Route updated successfully.",
        "route": route.to_dict()
    })


# ==========================================
# Delete Route
# ==========================================

@routes_bp.route("/delete/<int:route_id>", methods=["DELETE"])
def delete_route(route_id):

    route = Route.query.get(route_id)

    if route is None:
        return jsonify({
            "success": False,
            "message": "Route not found."
        }), 404

    db.session.delete(route)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Route deleted successfully."
    })


# ==========================================
# Search Routes
# ==========================================

@routes_bp.route("/search", methods=["GET"])
def search_routes():

    keyword = request.args.get("q", "")

    routes = Route.query.filter(
        Route.route_name.ilike(f"%{keyword}%")
    ).all()

    return jsonify({
        "success": True,
        "count": len(routes),
        "routes": [route.to_dict() for route in routes]
    })


# ==========================================
# Route Statistics
# ==========================================

@routes_bp.route("/stats", methods=["GET"])
def route_statistics():

    total_routes = Route.query.count()

    total_distance = sum(
        route.distance or 0
        for route in Route.query.all()
    )

    average_distance = (
        total_distance / total_routes
        if total_routes > 0 else 0
    )

    return jsonify({
        "success": True,
        "statistics": {
            "total_routes": total_routes,
            "total_distance": round(total_distance, 2),
            "average_distance": round(average_distance, 2)
        }
    })