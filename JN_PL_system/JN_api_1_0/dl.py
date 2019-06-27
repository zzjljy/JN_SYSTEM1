from flask import Blueprint, request, jsonify
from .. import py_connection
from JN_PL_system.utils.response_code import RET

dl = Blueprint('dl', __name__)


@dl.route('/JN/JN_DL/dl_search/dldj/<string:dldj>/', methods=['GET'])
def dl_dldj_find(dldj):
    '''
    根据道路等级进行查询
    :return:
    '''
    # 获取参数
    dldj = dldj
    if not(dldj):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.dl_find_level(dldj)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@dl.route('/JN/JN_DL/dl_search/dlmc/<string:dlmc>/', methods=['GET'])
def dl_dlmc_find(dlmc):
    '''
    根据道路名称进行查询
    :return:
    '''
    # 获取参数
    dlmc = dlmc
    if not(dlmc):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.dl_find_mc(dlmc)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@dl.route('/JN/JN_DL/dl_search_road/<float:point_x>/<float:point_y>/', methods=['GET'])
def dl_search_road_info(point_x, point_y):
    '''
    根据点坐标查询相应的道路,道路信息，道路横断面图片
    xy坐标
    :return:
    '''
    x = point_x
    y = point_y
    if not(x, y):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.dl_search_road_info(x, y)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@dl.route('/JN/JN_DL/kg_plot_way/<int:land_gid>/', methods=['GET'])
def kg_plot_way(land_gid):
    '''
    根据地块的唯一标识符gid查找地块周围的道路
    :return:
    '''
    gid = land_gid
    try:
        data = py_connection.kg_plot_way(gid)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')
