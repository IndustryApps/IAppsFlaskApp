import requests
from flask import jsonify

AAS_BASE_URL = 'https://aasgateway.uat.industryapps.net'


def get_auth_token():
    payload = {'grant_type': 'client_credentials', 'client_id': 'developer-test',
               'client_secret': 'c5378d99-68bd-44ee-bd6c-5dc77064a061'}
    resp = requests.post('https://auth.uat.industryapps.net/auth/realms/IndustryApps/protocol/openid-connect/token',
                         data=payload)

    data = resp.json()
    return data['access_token']


def get_aas_list(user_token, asset_type, plant_code):
    headers = {'Authorization': get_auth_token(), 'UserToken': user_token}
    params = {'AssetType': asset_type, 'PlantCode': plant_code}
    url = AAS_BASE_URL + '/aasList'
    resp = requests.get(url, params=params, headers=headers)
    return jsonify(resp.json())


def get_aas_by_id(user_token, aas_id):
    headers = {'Authorization': get_auth_token(), 'UserToken': user_token}
    aas_id = aas_id.replace('#', '%23')
    url = AAS_BASE_URL + '/aasList/' + aas_id
    resp = requests.get(url, headers=headers)
    return jsonify(resp.json())


def get_submodel_list(user_token, aas_id):
    headers = {'Authorization': get_auth_token(), 'UserToken': user_token}
    aas_id = aas_id.replace('#', '%23')
    url = AAS_BASE_URL + '/aasList/' + aas_id + '/aas/submodels'
    resp = requests.get(url, headers=headers)
    return jsonify(resp.json())


def get_submodel_by_id(user_token, aas_id, submodel_id):
    headers = {'Authorization': get_auth_token(), 'UserToken': user_token}
    aas_id = aas_id.replace('#', '%23')
    url = AAS_BASE_URL + '/aasList/' + aas_id + '/aas/submodels/' + submodel_id
    resp = requests.get(url, headers=headers)
    return jsonify(resp.json())


def get_submodel_elements(user_token, aas_id, submodel_id):
    headers = {'Authorization': get_auth_token(), 'UserToken': user_token}
    aas_id = aas_id.replace('#', '%23')
    url = AAS_BASE_URL + '/aasList/' + aas_id + '/aas/submodels/' + submodel_id + '/submodel/submodelElements'
    resp = requests.get(url, headers=headers)
    return jsonify(resp.json())


def get_submodel_element_by_id(user_token, aas_id, submodel_id, element_id):
    headers = {'Authorization': get_auth_token(), 'UserToken': user_token}
    aas_id = aas_id.replace('#', '%23')
    url = AAS_BASE_URL + '/aasList/' + aas_id + '/aas/submodels/' + submodel_id + \
          '/submodel/submodelElements/' + element_id
    resp = requests.get(url, headers=headers)
    return jsonify(resp.json())


def get_submodel_element_value(user_token, aas_id, submodel_id, element_id):
    headers = {'Authorization': get_auth_token(), 'UserToken': user_token}
    aas_id = aas_id.replace('#', '%23')
    url = AAS_BASE_URL + '/aasList/' + aas_id + '/aas/submodels/' + submodel_id + \
          '/submodel/submodelElements/' + element_id + "/value"
    resp = requests.get(url, headers=headers)
    return jsonify(resp.json())
