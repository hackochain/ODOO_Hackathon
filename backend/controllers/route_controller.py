from database.db import db
from database.models import Route


class RouteController:

    @staticmethod
    def get_all():

        routes = Route.query.all()

        return {
            "success": True,
            "count": len(routes),
            "routes": [
                route.to_dict()
                for route in routes
            ]
        }, 200

    @staticmethod
    def get_by_id(route_id):

        route = Route.query.get(route_id)

        if route is None:
            return {
                "success": False,
                "message": "Route not found."
            }, 404

        return {
            "success": True,
            "route": route.to_dict()
        }, 200

    @staticmethod
    def add(data):

        route = Route(
            route_name=data.get("route_name"),
            source=data.get("source"),
            destination=data.get("destination"),
            distance=data.get("distance"),
            estimated_time=data.get("estimated_time")
        )

        db.session.add(route)
        db.session.commit()

        return {
            "success": True,
            "message": "Route added successfully.",
            "route": route.to_dict()
        }, 201

    @staticmethod
    def update(route_id, data):

        route = Route.query.get(route_id)

        if route is None:
            return {
                "success": False,
                "message": "Route not found."
            }, 404

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

        return {
            "success": True,
            "message": "Route updated successfully.",
            "route": route.to_dict()
        }, 200

    @staticmethod
    def delete(route_id):

        route = Route.query.get(route_id)

        if route is None:
            return {
                "success": False,
                "message": "Route not found."
            }, 404

        db.session.delete(route)
        db.session.commit()

        return {
            "success": True,
            "message": "Route deleted successfully."
        }, 200

    @staticmethod
    def search(keyword):

        routes = Route.query.filter(
            Route.route_name.ilike(f"%{keyword}%")
        ).all()

        return {
            "success": True,
            "count": len(routes),
            "routes": [
                route.to_dict()
                for route in routes
            ]
        }, 200

    @staticmethod
    def statistics():

        routes = Route.query.all()

        total_routes = len(routes)

        total_distance = sum(
            route.distance or 0
            for route in routes
        )

        average_distance = (
            total_distance / total_routes
            if total_routes > 0 else 0
        )

        return {
            "success": True,
            "statistics": {
                "total_routes": total_routes,
                "total_distance": round(total_distance, 2),
                "average_distance": round(average_distance, 2)
            }
        }, 200