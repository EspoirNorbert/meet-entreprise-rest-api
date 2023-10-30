from functools import wraps
from flask import request, abort
from api.validators import Validator

def validate_json_payload(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.json:
            return abort(400, description="JSON object required")
        return func(*args, **kwargs)
    return wrapper

def validate_data(entity):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.json
            validator_response = Validator.check_validity_data(data=data, entity=entity)
            if validator_response:
                return abort(400, description=validator_response)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_gender(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        gender = request.json.get('gender')
        if not Validator.check_gender(gender):
            return abort(400, description="Gender should be 'F' or 'M'")
        return func(*args, **kwargs)
    return wrapper

def check_entity_existence(entity, field_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            field_value = request.json.get(field_name)
            if entity.exist_by_field(field_name):
                return abort(409, description=f"{entity.__name__} with {field_name} '{field_value}' already exists")
            return func(*args, **kwargs)
        return wrapper
    return decorator
