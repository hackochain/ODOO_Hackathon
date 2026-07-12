from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from database.db import db
from database.models import User

auth_bp = Blueprint("auth", __name__)


# ==========================================
# Register
# ==========================================

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received."
        }), 400

    full_name = data.get("full_name")
    email = data.get("email")
    password = data.get("password")

    if not full_name or not email or not password:
        return jsonify({
            "success": False,
            "message": "All fields are required."
        }), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "success": False,
            "message": "Email already exists."
        }), 409

    hashed_password = generate_password_hash(password)

    new_user = User(
        full_name=full_name,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "User registered successfully."
    }), 201


# ==========================================
# Login
# ==========================================

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received."
        }), 400

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({
            "success": False,
            "message": "Invalid email or password."
        }), 401

    if not check_password_hash(user.password, password):
        return jsonify({
            "success": False,
            "message": "Invalid email or password."
        }), 401

    access_token = create_access_token(
        identity=user.id
    )

    return jsonify({
        "success": True,
        "message": "Login successful.",
        "token": access_token,
        "user": user.to_dict()
    }), 200


# ==========================================
# Profile
# ==========================================

@auth_bp.route("/profile/<int:user_id>", methods=["GET"])
def profile(user_id):

    user = User.query.get(user_id)

    if user is None:
        return jsonify({
            "success": False,
            "message": "User not found."
        }), 404

    return jsonify({
        "success": True,
        "user": user.to_dict()
    })


# ==========================================
# Update Profile
# ==========================================

@auth_bp.route("/profile/<int:user_id>", methods=["PUT"])
def update_profile(user_id):

    user = User.query.get(user_id)

    if user is None:
        return jsonify({
            "success": False,
            "message": "User not found."
        }), 404

    data = request.get_json()

    user.full_name = data.get(
        "full_name",
        user.full_name
    )

    user.email = data.get(
        "email",
        user.email
    )

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Profile updated successfully.",
        "user": user.to_dict()
    })


# ==========================================
# Delete User
# ==========================================

@auth_bp.route("/delete/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    user = User.query.get(user_id)

    if user is None:
        return jsonify({
            "success": False,
            "message": "User not found."
        }), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "User deleted successfully."
    })