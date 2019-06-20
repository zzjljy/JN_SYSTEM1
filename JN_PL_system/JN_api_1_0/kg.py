from flask import Blueprint, request, jsonify
from .. import py_connection
from JN_PL_system.utils.response_code import RET

kg = Blueprint('kg', __name__)


@kg.route('/JN/JN_KG/search_info/', methods=['POST'])
def kg_info_find():
    '''
    控规信息查询，根据用地类型和、设施名称
    :return:
    '''
    # 获取参数
    kg_data = request.get_json('data')
    # 判断参数是否存在
    if not kg_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    params = []
    for k, v in kg_data.items():
        params.append(v)
    # 原生语句进行控规信息查询
    try:
        data = py_connection.kg_find_land(params[0], params[1])
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@kg.route('/JN/JN_KG/search_element/', methods=['POST'])
def kg_element_find():
    '''
    根据控规用地绿地率或容积率进行查询
    :return:
    '''
    # 获取参数
    kg_data = request.get_json('data')
    if not kg_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        for k, v in kg_data.items():
            kg_element = v
        data = py_connection.kg_find_elements(kg_element)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@kg.route('/JN/JN_KG/kg_search_land/', methods=['POST'])
def kg_search_land_info():
    '''
    根据点坐标查询地块信息
    :return:
    '''
    # 获取参数
    kg_data = request.get_json('data')
    if not kg_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        x = kg_data.get('x')
        y = kg_data.get('y')
        data = py_connection.kg_search_land_info(x, y)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')
