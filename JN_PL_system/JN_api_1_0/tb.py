from flask import Blueprint, request, jsonify
from .. import py_connection
from JN_PL_system.utils.response_code import RET
import json
tb = Blueprint('tb', __name__)


# 自定义范围查询
@tb.route('/JN/JN_TB/tb_find_info_custom/', methods=['GET'])
def tb_find_info_custom():
    '''
    图斑自定义转换，框选区域进行转换
    参数：由点坐标构成的polygon
    点坐标至少三个不同的点
    字典形式，{'rings':[[point1],[point2],[point3],....[point1]}
    :return:
    '''
    tb_data = request.args
    print(tb_data)
    for k, v in tb_data.to_dict().items():
        data = v
    rings = json.loads(data)
    points_list = rings.get('rings')
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
        # print('-----------------------')
        # print(type(polygon), polygon)
        # print('-----------------------------')
        data = py_connection.tb_find_info_custom(polygon)
        # print('数据', data)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tb.route('/JN/JN_TB/tb_find_info/<float:point_x>/<float:point_y>/', methods=['GET'])
def tb_find_info(point_x, point_y):
    '''
    单个图斑范围查询
    根据点坐标返回点坐标所在小范围的管控区的信息
    :return:
    '''
    # 获取参数
    x = point_x
    y = point_y
    if not(x, y):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.tb_find_info(x, y)
        # print(data)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')