from flask import Blueprint, request, jsonify
from .. import py_connection
from JN_PL_system.utils.response_code import RET
import json

kg = Blueprint('kg', __name__)


@kg.route('/JN/JN_KG/search_info/', methods=['GET'])
def kg_info_find():
    '''
    控规信息查询，根据用地类型和、设施名称
    以json方式传数据 ImmutableMultiDict([('key', '{"ydxz":"一类工业用地","ssmc":"公厕"}')])
    :return:
    '''
    # 获取参数
    data = request.args
    print(data)
    for k, v in data.to_dict().items():
        data_dict = v
    data_dict = json.loads(data_dict)

    print(data_dict)
    ydxz = data_dict.get('ydxz')
    ssmc = data_dict.get('ssmc')
    # print(ydxz)
    # print(ssmc)
    if not(ydxz, ssmc):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        if ssmc == '':
            data = py_connection.kg_find_land(ydxz)
        else:
            data = py_connection.kg_find_land(ydxz, ssmc)
            print(data)
        # print(data)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@kg.route('/JN/JN_KG/search_element/RJL/<int:rjl_min>/', methods=['GET'])
def kg_element_find_rjl(rjl_min):
    '''
    根据控规用地绿地率或容积率进行查询
    :return:
    '''
    # 获取参数
    s_rjl = rjl_min
    try:
        data = py_connection.kg_find_elements_rjl(s_rjl)
        # print(data)
        if data != 'ERROR':
            return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@kg.route('/JN/JN_KG/search_element/LDL/<int:ldl_min>/', methods=['GET'])
def kg_element_find_ldl(ldl_min):
    '''
    根据控规用地绿地率或容积率进行查询
    :return:
    '''
    # 获取参数
    s_ldl = ldl_min
    try:
        data = py_connection.kg_find_elements_ldl(s_ldl)
        # print(data)
        if data != 'ERROR':
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
    x = float(point_x)
    y = float(point_y)
    if not(x, y):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.kg_search_land_info(x, y)
        # print(data)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')
