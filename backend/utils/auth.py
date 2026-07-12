from functools import wraps

from flask import jsonify
from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt_identity
)

from database.models import User


def jwt_required_custom(fn):
    """
    Verify JWT token before accessing protected routes.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):

        try:

            verify_jwt_in_request()

            return fn(*args, **kwargs)

        except Exception as error:

            return jsonify({
                "success": False,
                "message": "Unauthorized access.",
                "error": str(error)
            }), 401

    return wrapper


def get_current_user():

    try:

        user_id = get_jwt_identity()

        if user_id is None:
            return None

        return User.query.get(user_id)

    except Exception:

        return None


def admin_required(fn):
    """
    Allow only admin users.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):

        user = get_current_user()

        if user is None:

            return jsonify({
                "success": False,
                "message": "Authentication required."
            }), 401

        if getattr(user, "role", "user") != "admin":

            return jsonify({
                "success": False,
                "message": "Admin access required."
            }), 403

        return fn(*args, **kwargs)

    return wrapper


def authenticated():

    """
    Returns True if JWT is valid.
    """

    try:

        verify_jwt_in_request()

        return True

    except Exception:

        return False


def current_user_data():

    """
    Returns current logged-in user's data.
    """

    user = get_current_user()

    if user is None:
        return None

    return user.to_dict()