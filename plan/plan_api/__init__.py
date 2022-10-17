from flask import Blueprint

plan_api_blueprint = Blueprint('plan_api', __name__)

from . import routes
