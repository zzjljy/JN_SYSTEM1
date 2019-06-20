from flask import Blueprint, request, jsonify, current_app, redirect, url_for
from .. import py_connection
from JN_PL_system.utils.response_code import RET
gkq = Blueprint('gkq', __name__)


@gkq.route('/JN/JN_GKQ/gkq_find_info/', methods=['POST'])
def gkq_find_info():
    '''
    根据点坐标返回点坐标所在小范围的管控区的信息
    :return:
    '''
    # 获取参数
    gkq_data = request.get_json('data')
    if not gkq_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        x = gkq_data.get('x')
        y = gkq_data.get('y')
        data = py_connection.kg_find_elements(x, y)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@gkq.route('/JN/JN_GKQ/gkq_update_info_big/', methods=['POST'])
def gkq_update_info_big():
    '''
    根据管控区信息进行类型转换，大类别进行信息转换
    :return:
    '''
    # 获取参数
    gkq_data = request.get_json('data')
    if not gkq_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    if len(gkq_data) < 3:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        gid = gkq_data.get('gid')
        ydxz = gkq_data.get('ydxz')
        ydlb = gkq_data.get('ydlb')
        res = py_connection.gkq_update_info_big(gid, ydxz, ydlb)
        if res == '0K':
            return redirect(url_for('gkq_area_search'))
        else:
            return jsonify(errorno=RET.UPDATEERR, errmsg='数据库更改错误')
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@gkq.route('/JN/JN_GKQ/gkq_update_info_small/', methods=['POST'])
def gkq_update_info_small():
    '''
    根据管控区信息进行类型转换，小类别进行信息转换
    :return:
    '''
    # 获取参数
    gkq_data = request.get_json('data')
    if not gkq_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        gid = gkq_data.get('gid')
        ydlb = gkq_data.get('ydlb')
        res = py_connection.gkq_update_info_small(gid, ydlb)
        if res == '0K':
            return redirect(url_for('gkq_area_search'))
        else:
            return jsonify(errorno=RET.UPDATEERR, errmsg='数据库更改错误')
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@gkq.route('/JN/JN_GKQ/gkq_area_search/', methods=['GET'])
def gkq_area_search():
    '''
    点击管控区面积比重查询按钮进行各种类型面积比重查询
    :return:
    '''
    try:
        data = py_connection.sum_of_area()
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        current_app.logger.error(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@gkq.route('/JN/JN_GKQ/gkq_find_info_custom/', methods=['POST'])
def gkq_find_info_custom():
    '''
    一级管控区自定义转换，框选区域进行转换
    参数：由点坐标构成的polygon
    形式点号，坐标列表
    :return:
    '''
    gkq_data = request.get_json('data')
    if not gkq_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    num = len(gkq_data)
    if num < 4:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    first_point = gkq_data.get('1')
    last_point = gkq_data.get(num)
    if first_point[0] != last_point[0] or first_point[1] != last_point[1]:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        polygon = ''
        for k, v in gkq_data:
            if int(k) < num:
                point = '%s %s,' % (v[0], v[1])
            else:
                point = '%s %s' % (v[0], v[1])
            polygon += point
        data = py_connection.gkq_find_info_custom(polygon)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@gkq.route('/JN/JN_GKQ/gkq_custom_transformation_big/', methods=['POST'])
def gkq_custom_transformation_big():
    '''
    管控区自定义转换，根据大类进行转换
    :return:
    '''
    gkq_data = request.get_json('data')
    if not gkq_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    if len(gkq_data) < 3:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        gid = gkq_data.get('gid')
        ydxz = gkq_data.get('ydxz')
        ydlb = gkq_data.get('ydlb')
        res = py_connection.gkq_custom_transformation_big(gid, ydxz, ydlb)
        if res == 'OK':
            return redirect(url_for('gkq_area_search'))
        else:
            return jsonify(errorno=RET.UPDATEERR, errmsg='数据库更改错误')
        pass
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.UPDATEERR, errmsg='数据库更改错误')


@gkq.route('/JN/JN_GKQ/gkq_custom_transformation_small/', methods=['POST'])
def gkq_custom_transformation_small():
    '''
    一级管控区自定义小类别转换
    :return:
    '''
    gkq_data = request.get_json('data')
    if not gkq_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    if len(gkq_data) < 2:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        gid = gkq_data.get('gid')
        ydlb = gkq_data.get('ydlb')
        res = py_connection.gkq_custom_transformation_small(gid, ydlb)
        if res == 'OK':
            return redirect(url_for('gkq_area_search'))
        else:
            return jsonify(errorno=RET.UPDATEERR, errmsg='数据库更改错误')
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.UPDATEERR, errmsg='数据库更改错误')
