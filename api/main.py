from flask import Blueprint
from api.utils import APIResponse

main= Blueprint('main' , __name__)

@main.route('/')
def home():
    return APIResponse.response(
        data={'message' : 'Welcome to meet REST API' , 'version': 1.2}
    )