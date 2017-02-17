# -*- coding: utf-8 -*-
from flask import Blueprint

modulo2_blueprint = Blueprint(name='modulo2', import_name=__name__, url_prefix='/modulo2/')


@modulo2_blueprint.route('add/<message>', methods=['GET'])
@modulo2_blueprint.route('add/', defaults={'message': 'sem mensagem no add'},methods=['GET'])
@modulo2_blueprint.route('/', defaults={'message': 'sem mensagem'}, methods=['GET'])
def add(message):
    return 'modulo2 - {}'.format(message)
