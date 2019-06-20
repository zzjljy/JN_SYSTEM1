from flask import Blueprint, request, jsonify
from .. import py_connection
from JN_PL_system.utils.response_code import RET

dl = Blueprint('dl', __name__)


@dl.route('/JN/JN_DL/dl_search/', methods=['POST'])
def dl_find():
    '''
    道路信息查询
    :return:
    '''
    # 获取参数
    dl_data = request.get_json('data')
    # 判断参数是否存在
    if not dl_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    # 原生语句进行控规信息查询
    try:
        for k, v in dl_data.items():
            if k == 'dlmc':
                data = py_connection.dl_find_mc(v)
            else:
                # 道路级别查询
                data = py_connection.dl_find_level(v)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@dl.route('/JN/JN_DL/dl_search_road/', methods=['POST'])
def dl_search_road_info():
    '''
    根据点坐标查询相应的道路
    xy坐标
    :return:
    '''
    dl_data = request.get_json('data')
    if not dl_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        x = dl_data.get('x')
        y = dl_data.get('y')
        data = py_connection.dl_search_road_info(x, y)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@dl.route('/JN/JN_DL/kg_plot_way/', methods=['POST'])
def kg_plot_way():
    '''
    根据地块的唯一标识符gid查找地块周围的道路
    :return:
    '''
    kg_data = request.get_json('data')
    if not kg_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    gid = kg_data.get('gid')
    try:
        data = py_connection.kg_plot_way(gid)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')