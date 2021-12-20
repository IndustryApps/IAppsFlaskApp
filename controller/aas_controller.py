from flask import Blueprint, request

from service import aas_service

aas = Blueprint('aas', __name__)


@aas.route("/list", methods=['POST'])
def get_aas_list():
    head = request.headers
    user_token = head['UserToken']
    req = request.json
    asset_type = req['assetType']
    plant_code = req['plantCode']
    aas_list = aas_service.get_aas_list(user_token, asset_type, plant_code)
    return aas_list


@aas.route("/get", methods=['POST'])
def get_aas():
    head = request.headers
    user_token = head['UserToken']
    req = request.json
    aas_id = req['aasId']
    aas_data = aas_service.get_aas_by_id(user_token, aas_id)
    return aas_data


@aas.route("/submodel/list", methods=['POST'])
def get_submodel_list():
    head = request.headers
    user_token = head['UserToken']
    req = request.json
    aas_id = req['aasId']
    submodel_list = aas_service.get_submodel_list(user_token, aas_id)
    return submodel_list


@aas.route("/submodel/get", methods=['POST'])
def get_submodel():
    head = request.headers
    user_token = head['UserToken']
    req = request.json
    aas_id = req['aasId']
    submodel_id = req['submodelIdShort']
    submodel = aas_service.get_submodel_by_id(user_token, aas_id, submodel_id)
    return submodel


@aas.route("/submodel/elements/list", methods=['POST'])
def get_submodel_element_list():
    head = request.headers
    user_token = head['UserToken']
    req = request.json
    aas_id = req['aasId']
    submodel_id = req['submodelIdShort']
    submodel_elements = aas_service.get_submodel_elements(user_token, aas_id, submodel_id)
    return submodel_elements


@aas.route("/submodel/element/get", methods=['POST'])
def get_submodel_element():
    head = request.headers
    user_token = head['UserToken']
    req = request.json
    aas_id = req['aasId']
    submodel_id = req['submodelIdShort']
    element_id = req['submodelElementIdShort']
    submodel_elements = aas_service.get_submodel_element_by_id(user_token, aas_id, submodel_id, element_id)
    return submodel_elements


@aas.route("/submodel/element/value", methods=['POST'])
def get_submodel_element_value():
    head = request.headers
    user_token = head['UserToken']
    req = request.json
    aas_id = req['aasId']
    submodel_id = req['submodelIdShort']
    element_id = req['submodelElementIdShort']
    submodel_elements = aas_service.get_submodel_element_value(user_token, aas_id, submodel_id, element_id)
    return submodel_elements
