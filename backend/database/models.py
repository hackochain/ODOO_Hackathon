from datetime import datetime

from database.db import db


# ==============================
# User Model
# ==============================

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(50), default="admin")

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "role": self.role
        }


# ==============================
# Fleet Model
# ==============================

class Fleet(db.Model):
    __tablename__ = "fleet"

    id = db.Column(db.Integer, primary_key=True)

    vehicle_number = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    vehicle_type = db.Column(db.String(50))

    capacity = db.Column(db.Integer)

    status = db.Column(
        db.String(30),
        default="Active"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "vehicle_number": self.vehicle_number,
            "vehicle_type": self.vehicle_type,
            "capacity": self.capacity,
            "status": self.status
        }


# ==============================
# Driver Model
# ==============================

class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    license_number = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    phone = db.Column(db.String(20))

    assigned_vehicle = db.Column(db.String(50))

    status = db.Column(
        db.String(30),
        default="Available"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "license_number": self.license_number,
            "phone": self.phone,
            "assigned_vehicle": self.assigned_vehicle,
            "status": self.status
        }


# ==============================
# Route Model
# ==============================

class Route(db.Model):
    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True)

    route_name = db.Column(
        db.String(100),
        nullable=False
    )

    source = db.Column(db.String(100))

    destination = db.Column(db.String(100))

    distance = db.Column(db.Float)

    estimated_time = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "route_name": self.route_name,
            "source": self.source,
            "destination": self.destination,
            "distance": self.distance,
            "estimated_time": self.estimated_time
        }


# ==============================
# Tracking Model
# ==============================

class Tracking(db.Model):
    __tablename__ = "tracking"

    id = db.Column(db.Integer, primary_key=True)

    vehicle_number = db.Column(db.String(50))

    latitude = db.Column(db.Float)

    longitude = db.Column(db.Float)

    speed = db.Column(db.Float)

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "vehicle_number": self.vehicle_number,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "speed": self.speed,
            "updated_at": self.updated_at
        }


# ==============================
# Report Model
# ==============================

class Report(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)

    report_name = db.Column(db.String(100))

    report_type = db.Column(db.String(50))

    generated_by = db.Column(db.String(100))

    generated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "report_name": self.report_name,
            "report_type": self.report_type,
            "generated_by": self.generated_by,
            "generated_at": self.generated_at
        }