from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from database.db import db
from database.models import User


class AuthController:

    @staticmethod
    def register(full_name, email, password):

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:
            return {
                "success": False,
                "message": "Email already exists."
            }, 409

        user = User(
            full_name=full_name,
            email=email,
            password=generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

        return {
            "success": True,
            "message": "User registered successfully.",
            "user": user.to_dict()
        }, 201


    @staticmethod
    def login(email, password):

        user = User.query.filter_by(
            email=email
        ).first()

        if user is None:
            return {
                "success": False,
                "message": "Invalid email or password."
            }, 401

        if not check_password_hash(
            user.password,
            password
        ):
            return {
                "success": False,
                "message": "Invalid email or password."
            }, 401

        token = create_access_token(
            identity=user.id
        )

        return {
            "success": True,
            "token": token,
            "user": user.to_dict()
        }, 200


    @staticmethod
    def get_profile(user_id):

        user = User.query.get(user_id)

        if user is None:
            return {
                "success": False,
                "message": "User not found."
            }, 404

        return {
            "success": True,
            "user": user.to_dict()
        }, 200


    @staticmethod
    def update_profile(user_id, data):

        user = User.query.get(user_id)

        if user is None:
            return {
                "success": False,
                "message": "User not found."
            }, 404

        user.full_name = data.get(
            "full_name",
            user.full_name
        )

        user.email = data.get(
            "email",
            user.email
        )

        db.session.commit()

        return {
            "success": True,
            "message": "Profile updated successfully.",
            "user": user.to_dict()
        }, 200


    @staticmethod
    def delete_user(user_id):

        user = User.query.get(user_id)

        if user is None:
            return {
                "success": False,
                "message": "User not found."
            }, 404

        db.session.delete(user)
        db.session.commit()

        return {
            "success": True,
            "message": "User deleted successfully."
        }, 200