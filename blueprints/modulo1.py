# -*- coding: utf-8 -*-
from flask import Blueprint

modulo1_blueprint = Blueprint(name='modulo1', import_name=__name__)


@modulo1_blueprint.route('/', methods=['GET'])
def index():
    return 'modulo1'
