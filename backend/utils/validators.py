import re


# ==========================================
# Required Field Validation
# ==========================================

def validate_required(data, fields):

    errors = {}

    for field in fields:

        if field not in data or data[field] in [None, ""]:

            errors[field] = f"{field} is required."

    return errors


# ==========================================
# Email Validation
# ==========================================

def validate_email(email):

    if email is None:
        return False

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return re.match(pattern, email) is not None


# ==========================================
# Phone Validation
# ==========================================

def validate_phone(phone):

    if phone is None:
        return False

    pattern = r"^[0-9]{10}$"

    return re.match(pattern, str(phone)) is not None


# ==========================================
# Password Validation
# ==========================================

def validate_password(password):

    if password is None:
        return False

    if len(password) < 8:
        return False

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_upper and has_lower and has_digit


# ==========================================
# Vehicle Number Validation
# Example: TN45AB1234
# ==========================================

def validate_vehicle_number(vehicle_number):

    if vehicle_number is None:
        return False

    pattern = r"^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$"

    return re.match(pattern, vehicle_number.upper()) is not None


# ==========================================
# License Number Validation
# ==========================================

def validate_license_number(license_number):

    if license_number is None:
        return False

    return len(str(license_number).strip()) >= 8


# ==========================================
# Latitude Validation
# ==========================================

def validate_latitude(latitude):

    try:

        latitude = float(latitude)

        return -90 <= latitude <= 90

    except (TypeError, ValueError):

        return False


# ==========================================
# Longitude Validation
# ==========================================

def validate_longitude(longitude):

    try:

        longitude = float(longitude)

        return -180 <= longitude <= 180

    except (TypeError, ValueError):

        return False


# ==========================================
# Positive Number Validation
# ==========================================

def validate_positive_number(value):

    try:

        return float(value) >= 0

    except (TypeError, ValueError):

        return False


# ==========================================
# Validation Summary
# ==========================================

def validate_tracking_data(data):

    errors = {}

    required_errors = validate_required(
        data,
        [
            "vehicle_number",
            "latitude",
            "longitude"
        ]
    )

    errors.update(required_errors)

    if "vehicle_number" in data:

        if not validate_vehicle_number(
            data["vehicle_number"]
        ):
            errors["vehicle_number"] = "Invalid vehicle number."

    if "latitude" in data:

        if not validate_latitude(
            data["latitude"]
        ):
            errors["latitude"] = "Invalid latitude."

    if "longitude" in data:

        if not validate_longitude(
            data["longitude"]
        ):
            errors["longitude"] = "Invalid longitude."

    return errors


# ==========================================
# Check Validation Result
# ==========================================

def is_valid(errors):

    return len(errors) == 0