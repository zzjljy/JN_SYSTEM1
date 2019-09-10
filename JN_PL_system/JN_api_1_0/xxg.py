from flask import Blueprint, request, jsonify
from .. import py_connection
from JN_PL_system.utils.response_code import RET
xxg = Blueprint('xxg', __name__)


@xxg.route('/JN/JN_XXG/xxg_find_info/<float:point_x>/<float:point_y>/', methods=['GET'])
def gkq_find_info(point_x, point_y):
    '''
    修详规查询，返回建筑信息（房屋和公建）和地界信息
    :return:
    '''
    # 获取参数
    x = point_x
    y = point_y
    if not(x, y):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.xxg_find_info(x, y)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@xxg.route('/JN/JN_XXG/xxg_dj_centroid/', methods=['GET'])
def xxg_dijie():
    try:
        data = py_connection.xxg_find_centroid('')
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@xxg.route('/JN/JN_XXG/search_village_name/')
def xxg_village_name():
    '''
    根据小区名称进行查询
    :return:
    '''
    xqmc = request.args.get('xqmc')
    if xqmc == None or xqmc.strip() == '':
        return jsonify({'error': '小区名称不能为空'})
    else:
        data = py_connection.xxg_find_centroid(xqmc)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    pass