from crypt import methods
from urllib import response
from . import plan_api_blueprint
from .. import db
from ..models import PlanAlimenticio
from flask import jsonify, request

@plan_api_blueprint.route('/api/planes', methods=['GET'])
def planes():
    planes = []
    for row in PlanAlimenticio.query.all():
        planes.append(row.to_json())
    
    response = jsonify({'results', planes})
    return response
    