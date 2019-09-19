from flask import Blueprint, request, jsonify, make_response, redirect, url_for
from .. import py_connection
from JN_PL_system.utils.response_code import RET
from ..models import DLHDM_IMG
import json

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
        # print(data)
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
    # print(dlmc)
    # print('-------------')
    if dlmc == None:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.dl_find_mc(dlmc)
        # print(data)
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
        # print(data)
        # 调道路横断面图片
        # image_objectid = int(data.get('features')[0].get('attributes').get('objectid'))
        # print(image_objectid)
        # redirect(url_for('dl.dl_dlhdm_image', image_objectid=image_objectid))
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@dl.route('/JN/JN_DLHDM/dl_search_road_image/<int:image_objectid>/', methods=['GET'])
def dl_dlhdm_image(image_objectid):
    '''
    某条道路的道路横断面图片
    :param image_objectid:
    :return:
    '''
    image_objectid = image_objectid
    try:
        dlhdm_img = DLHDM_IMG.objects(image_objectid=image_objectid).first()
        image = dlhdm_img['image']
        response = make_response(image)
        # print(image)
        response.headers['Content-Type'] = "image/png"
        # response.setContentType("text/html; charset=utf-8")
        return response
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


# 道路自定义范围内里程统计
@dl.route('/JN/JN_DL/dl_mileage_statistics/', methods=['GET'])
def dldj_measurement():
    '''
    道路划区域进行里程统计
    参数：由点坐标构成的polygon
    点坐标至少三个不同的点
    字典形式，{'rings':[[point1],[point2],[point3],....[point1]}
    :return:
    '''
    gkq_data = request.args
    print('原始数据', gkq_data)
    for k, v in gkq_data.to_dict().items():
        data = v
    rings = json.loads(data)
    points_list = rings.get('rings')
    print('polygon', points_list)
    if not rings:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    if len(points_list) < 4:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    first_points = points_list[0]
    last_points = points_list[-1]
    if first_points[0] != last_points[0] or first_points[1] != last_points[1]:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        polygon = ''
        for i in range(len(points_list)):
            if i == len(points_list)-1:
                point = '%s %s' % (points_list[i][0], points_list[i][1])
            else:
                point = '%s %s,' % (points_list[i][0], points_list[i][1])
            polygon += point
        data = py_connection.dl_mileage_statistics(polygon)
        if data != 'ERROR':
            return jsonify(errorno=RET.OK, errmsg='成功', data=data)
        else:
            return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')
