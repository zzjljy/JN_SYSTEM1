from flask import Blueprint, request, jsonify
from .. import py_connection
from JN_PL_system.utils.response_code import RET
import json
from werkzeug.datastructures import CombinedMultiDict, MultiDict

kg = Blueprint('kg', __name__)


@kg.route('/JN/JN_KG/search_info/<string:ydxz>/<string:ssmc>/', methods=['GET'])
def kg_info_find(ydxz, ssmc):
    '''
    控规信息查询，根据用地类型和、设施名称
    第二个参数为空的时候还没有解决
    :return:
    '''
    # 获取参数
    ydxz = ydxz
    ssmc = ssmc
    # print(ydxz, ssmc)
    if not(ydxz, ssmc):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.kg_find_land(ydxz, ssmc)
        # print(data)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@kg.route('/JN/JN_KG/search_info/', methods=['GET'])
def kg_info_find1():
    '''
    控规信息查询，根据用地类型和、设施名称
    以json方式传数据
    :return:
    '''
    # 获取参数
    data = request.args
    for k, v in data.to_dict().items():
        data_dict = k
    data_dict = json.loads(data_dict)
    ydxz = data_dict.get('ydxz')
    ssmc = data_dict.get('ssmc')
    if not(ydxz, ssmc):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.kg_find_land(ydxz, ssmc)
        print(data)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@kg.route('/JN/JN_KG/search_element/RJL/<int:rjl_min>/<int:rjl_max>/', methods=['GET'])
def kg_element_find_rjl(rjl_min, rjl_max):
    '''
    根据控规用地绿地率或容积率进行查询
    :return:
    '''
    # 获取参数
    s_rjl = rjl_min
    b_rjl = rjl_max
    if not(s_rjl, b_rjl):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.kg_find_elements_rjl(s_rjl, b_rjl)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@kg.route('/JN/JN_KG/search_element/LDL/<int:ldl_min>/<int:ldl_max>/', methods=['GET'])
def kg_element_find_ldl(ldl_min, ldl_max):
    '''
    根据控规用地绿地率或容积率进行查询
    :return:
    '''
    # 获取参数
    s_ldl = ldl_min
    b_ldl = ldl_max
    if not(s_ldl, b_ldl):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.kg_find_elements_ldl(s_ldl, b_ldl)
        print(data)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@kg.route('/JN/JN_KG/kg_search_land/<float:point_x>/<float:point_y>/', methods=['GET'])
def kg_search_land_info(point_x, point_y):
    '''
    根据点坐标查询地块信息
    :return:
    '''
    # 获取参数
    x = point_x
    y = point_y
    if not(x, y):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.kg_search_land_info(x, y)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')
