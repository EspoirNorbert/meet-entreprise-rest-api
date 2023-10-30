from datetime import datetime
from flask import make_response, jsonify, Blueprint
from sqlalchemy.exc import SQLAlchemyError , IntegrityError
from api.http_status_code import (
    HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT,
    HTTP_500_INTERNAL_SERVER_ERROR, HTTP_405_METHOD_NOT_ALLOWED
)

errors = Blueprint('errors', __name__)

def error_response(code, message, description, status_code):
    response = {
        'code': code,
        'message': message,
        'description': description,
        'dateTime': datetime.utcnow().isoformat()
    }
    from api.utils import Utils
    Utils.print_exception()
    return make_response(jsonify(response), status_code)

@errors.app_errorhandler(HTTP_404_NOT_FOUND)
def resource_not_found(e):
    return error_response(
        code=HTTP_404_NOT_FOUND,
        message="Not Found",
        description=str(e),
        status_code=HTTP_404_NOT_FOUND
    )

@errors.app_errorhandler(HTTP_400_BAD_REQUEST)
def bad_request(e):
    return error_response(
        code=HTTP_400_BAD_REQUEST,
        message="Bad Request",
        description=str(e),
        status_code=HTTP_400_BAD_REQUEST
    )

@errors.app_errorhandler(IntegrityError)
def sqlalchemy_integrity_error(e):
    return error_response(
        code=HTTP_400_BAD_REQUEST,
        message="Database integrity error",
        description=str(e),
        status_code=HTTP_400_BAD_REQUEST
    )


@errors.app_errorhandler(SQLAlchemyError)
def handle_sqlAlchemy_error(e):
    return error_response(
        code=HTTP_500_INTERNAL_SERVER_ERROR,
        message="Internal Server Error",
        description=str(e),
        status_code=HTTP_500_INTERNAL_SERVER_ERROR
    )


@errors.app_errorhandler(Exception)
def handle_error(e):
    return error_response(
        code=HTTP_500_INTERNAL_SERVER_ERROR,
        message="Internal Server Error",
        description="An error occurred",
        status_code=HTTP_500_INTERNAL_SERVER_ERROR
    )

@errors.app_errorhandler(HTTP_405_METHOD_NOT_ALLOWED)
def not_allowed_method(e):
    return error_response(
        code=HTTP_405_METHOD_NOT_ALLOWED,
        message="Method Not Allowed",
        description="The method is not allowed for the requested URL.",
        status_code=HTTP_405_METHOD_NOT_ALLOWED
    )

@errors.app_errorhandler(HTTP_409_CONFLICT)
def conflict_method(e):
    return error_response(
        code=HTTP_409_CONFLICT,
        message="Conflit",
        description=str(e),
        status_code=HTTP_409_CONFLICT
    )
