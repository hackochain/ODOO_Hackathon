from datetime import datetime
import random
import string


def success_response(message, data=None, status=200):

    response = {
        "success": True,
        "message": message
    }

    if data is not None:
        response["data"] = data

    return response, status


def error_response(message, status=400):

    return {
        "success": False,
        "message": message
    }, status


def generate_reference(prefix="TR"):

    timestamp = datetime.now().strftime("%Y%m%d")

    random_part = "".join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=6
        )
    )

    return f"{prefix}-{timestamp}-{random_part}"


def current_timestamp():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def format_date(date_object):

    if date_object is None:
        return None

    return date_object.strftime(
        "%Y-%m-%d"
    )


def format_datetime(date_object):

    if date_object is None:
        return None

    return date_object.strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def paginate(query, page=1, per_page=10):

    pagination = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return {
        "items": [
            item.to_dict()
            for item in pagination.items
        ],
        "page": pagination.page,
        "pages": pagination.pages,
        "per_page": pagination.per_page,
        "total": pagination.total,
        "has_next": pagination.has_next,
        "has_prev": pagination.has_prev
    }


def calculate_percentage(part, total):

    if total == 0:
        return 0

    return round(
        (part / total) * 100,
        2
    )


def calculate_average(values):

    if not values:
        return 0

    return round(
        sum(values) / len(values),
        2
    )


def clean_string(value):

    if value is None:
        return ""

    return str(value).strip()


def is_empty(value):

    if value is None:
        return True

    if isinstance(value, str):

        return value.strip() == ""

    return False


def serialize_model(model):

    if model is None:
        return None

    if hasattr(model, "to_dict"):

        return model.to_dict()

    return model


def health_check():

    return {
        "application": "TransitOps Backend",
        "status": "Running",
        "version": "1.0.0",
        "timestamp": current_timestamp()
    }