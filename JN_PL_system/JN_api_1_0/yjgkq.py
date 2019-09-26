from flask import Blueprint, request, jsonify, current_app, redirect, url_for
from .. import py_connection
from JN_PL_system.utils.response_code import RET
import json
gkq = Blueprint('gkq', __name__)


@gkq.route('/JN/JN_GKQ/gkq_find_info/<float:point_x>/<float:point_y>/', methods=['GET'])
def gkq_find_info(point_x, point_y):
    '''
    单个管控区范围test1
    根据点坐标返回点坐标所在小范围的管控区的信息
    :return:
    '''
    # 获取参数
    x = point_x
    y = point_y
    if not(x, y):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.gkq_find_info(x, y)
        # print(data)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@gkq.route('/JN/JN_GKQ/gkq_convert_info_big/', methods=['PUT'])
def gkq_update_info_big():
    '''
    单个管控区范围
    根据管控区信息进行类型转换，大类别进行信息转换
    :return:
    '''
    # 获取参数
    if request.method == 'PUT':
        gkq_data = request.get_json('data')
        if not gkq_data:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        if len(gkq_data) < 3:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        gid = gkq_data.get('gid')
        ydxz = gkq_data.get('ydxz')
        ydlb = gkq_data.get('ydlb')
        if str(gid) == '' or ydxz == '' or ydlb == '':
            return jsonify(errorno=RET.DATAERR, errmsg='数据为空')
        try:
            res = py_connection.gkq_update_info_big(gid, ydxz, ydlb)
            print(res)
            if res == 'OK':
                # return jsonify(errorno=0, errmsg='okok')
                return redirect(url_for('gkq.gkq_area_search'))
            else:
                return jsonify(errorno=RET.UPDATEERR, errmsg='数据更改错误')
        except Exception as e:
            print(e)
            return jsonify(errorno=RET.DBERR, errmsg='数据库错误')
    else:
        return jsonify(errorno=RET.REQERR, errmsg='非法请求')


@gkq.route('/JN/JN_GKQ/gkq_convert_info_small/', methods=['PUT', 'GET'])
def gkq_update_info_small():
    '''
    单个管控区范围
    根据管控区信息进行类型转换，小类别进行信息转换
    json数据(转换保存)：gid:地块的唯一标识符
                     ydlb:将要转换为的地块的用地类别（小类）
    json数据(转换不保存)：gid:地块的唯一标识符
                       meta_ydxz:选择的地块的用地性质（大类名称）
                       meta_shape_area:选择地块的面积
                       ydlb:将要转换为的地块的用地类别（小类）
    :return:
    '''
    # 获取参数
    if request.method == 'PUT':
        gkq_data = json.loads(request.get_json('data').get('key'))
        gid = gkq_data.get('gid')
        ydlb = gkq_data.get('ydlb')
        if not(gkq_data):
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        if len(gkq_data) < 2:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        if str(gid) == '' or ydlb == '':
            jsonify(errorno=RET.DATAERR, errmsg='数据为空')
        try:
            res = py_connection.gkq_update_info_small(gid, ydlb)
            if res == 'OK':
                return redirect(url_for('gkq.gkq_area_search'))
            else:
                return jsonify(errorno=RET.UPDATEERR, errmsg='数据库更改错误')
        except Exception as e:
            print(e)
            return jsonify(errorno=RET.DBERR, errmsg='数据库错误')
    if request.method == 'GET':
        # 点击地块转换，查看转换后的结果，但是数据库中并没有保存转换后的结果，只是查看转换后的比例
        gkq_data = request.args
        for k, v in gkq_data.to_dict().items():
            data = v
        data = json.loads(data)
        if not(data) or len(data) < 4:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        gid = data.get('gid')
        meta_ydxz = data.get('meta_ydxz')
        meta_shape_area = float(data.get('meta_shape_area'))
        ydlb = data.get('ydlb')
        if str(gid) == '' or ydlb == '' or meta_ydxz == '':
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        try:
            item_area_percentage, item_area_dict = py_connection.sum_of_area()
            # print(item_area_dict)
            total_area = 0
            for k, v in item_area_dict.items():
                total_area += v
            # print(total_area)
            item_area_dict[meta_ydxz] = float(item_area_dict[meta_ydxz])-meta_shape_area
            if ydlb == '一般耕地' or ydlb == '基本农田':
                ydxz = '田'
            elif ydlb == '湖泊水库' or ydlb == '坑塘沟渠' or ydlb == '河道' or ydlb == '现状水域':
                ydxz = '水'
            elif ydlb == '市政设施':
                ydxz = '市政设施'
            elif ydlb == '其他生态用地' or ydlb == '现状绿地':
                ydxz = '草'
            elif ydlb == '可造林区域（农用用地）' or ydlb == '现状林地' or ydlb == '可造林区域（清退用地）':
                ydxz = '林'
            elif ydlb == '保留村庄':
                ydxz = '保留村庄'
            elif ydlb == '工业园区':
                ydxz = '工业园区'
            elif ydlb == '交通设施':
                ydxz = '交通设施'
            else:
                return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
            item_area_dict[ydxz] = float(item_area_dict[ydxz]) + meta_shape_area
            percentage_area = {}
            # print(item_area_dict)
            for k, v in item_area_dict.items():
                v = '%.2f%%' % (float(v) / float(total_area) * 100)
                percentage_area[k] = v
            return jsonify(errorno=RET.OK, errmsg='成功', data=percentage_area)
        except Exception as e:
            print(e)
            return jsonify(errorno=RET.DBERR, errmsg='数据库错误')
    else:
        return jsonify(errorno=RET.REQERR, errmsg='非法请求')


@gkq.route('/JN/JN_GKQ/gkq_area_search/', methods=['GET', 'PUT'])
def gkq_area_search():
    '''
    点击管控区面积比重查询按钮进行各种类型面积比重查询
    :return:
    '''
    try:
        data, item_area1, item_area = py_connection.sum_of_area()
        print(data)
        print(item_area)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data, item_area=item_area)
    except Exception as e:
        print(e)
        current_app.logger.error(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


# 自定义范围查询
@gkq.route('/JN/JN_GKQ/gkq_find_info_custom/', methods=['GET'])
def gkq_find_info_custom():
    '''
    一级管控区自定义转换，框选区域进行转换,返回相交的区域的信息
    相交的区域都转换
    参数：由点坐标构成的polygon
    点坐标至少三个不同的点
    字典形式，{'rings':[[point1],[point2],[point3],....[point1]}
    :return:
    '''
    gkq_data = request.args
    print(gkq_data)
    for k, v in gkq_data.to_dict().items():
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
        data = py_connection.gkq_find_info_custom(polygon)
        print('数据', data)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@gkq.route('/JN/JN_GKQ/gkq_find_area_ranges/', methods=['GET'])
def find_area_ranges():
    '''
    暂时不用
    一级管控区自定义转换，框选区域进行转换
    求相交区域的area和用地性质
    参数：由点坐标构成的polygon
    点坐标至少三个不同的点
    字典形式，{'rings':[[point1],[point2],[point3],....[point1]], 'gids':[gid1,gid2]}
    :return:
    '''
    gkq_data = request.args
    print(gkq_data)
    for k, v in gkq_data.to_dict().items():
        data = v
    rings = json.loads(data)
    points_list = rings.get('rings')
    gids = rings.get('gids')
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
        data = py_connection.gkq_ranges_conversion(polygon, gids)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@gkq.route('/JN/JN_GKQ/gkq_custom_convert_big/', methods=['PUT'])
def gkq_custom_transformation_big():
    '''
    管控区自定义转换，根据大类进行转换
    json数据，gid:选择的n个地块组成的集合
            ydxz：将要转换为的地块的大类
            ydlb：将要转换为的地块的小类
    :return:
    '''
    if request.method == 'PUT':
        gkq_data = request.get_json('data')
        if not gkq_data:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        if len(gkq_data) < 3:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        gid = gkq_data.get('gid')
        ydxz = gkq_data.get('ydxz')
        ydlb = gkq_data.get('ydlb')
        if len(gid) == 0 or ydxz == '' or ydlb == '' or type(gid) != list:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        try:
            res = py_connection.gkq_custom_transformation_big(gid, ydxz, ydlb)
            if res == 'OK':
                return redirect(url_for('gkq.gkq_area_search'))
            else:
                return jsonify(errorno=RET.UPDATEERR, errmsg='数据库更改错误')
        except Exception as e:
            print(e)
            return jsonify(errorno=RET.UPDATEERR, errmsg='数据库更改错误')
    else:
        return jsonify(errorno=RET.REQERR, errmsg='非法请求')


@gkq.route('/JN/JN_GKQ/gkq_custom_convert_small/', methods=['PUT', 'GET'])
def gkq_custom_transformation_small():
    '''
    用
    一级管控区自定义小类别转换
    json类型数据(修改并保存)
            gid:列表类型
            ydlb:将要转换为的小类的类型
    json数据类型（修改不保存，查看使用）
            meta_datas:[{'meta_ydxz': *, 'meta_shape_area': *},{}....{}]
            ydlb:所有地块将要转为的小类的类型
    :return:
    '''
    if request.method == 'PUT':
        print('put方法')
        print(request.get_json('data'))
        gkq_data = json.loads(request.get_json('data').get('key'))
        print(gkq_data)
        if not gkq_data:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        if len(gkq_data) < 2:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        gid = gkq_data.get('gid')
        print(type(gid), len(gid), gid)
        ydlb = gkq_data.get('ydlb')
        if len(gid) == 0 or ydlb == '' or type(gid) != list:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        try:
            res = py_connection.gkq_custom_transformation_small(gid, ydlb)
            if res == 'OK':
                return redirect(url_for('gkq.gkq_area_search'))
            else:
                return jsonify(errorno=RET.UPDATEERR, errmsg='数据库更改错误')
        except Exception as e:
            print(e)
            return jsonify(errorno=RET.UPDATEERR, errmsg='数据库更改错误')
    if request.method == 'GET':
        # 多个地块选择后进行类型转换展示，但是并不保存修改结果到数据，仅仅只是为了展示结果看
        gkq_data = request.args
        for k, v in gkq_data.to_dict().items():
            data = v
        data = json.loads(data)
        print(11111, data)
        if not(data) or len(data) < 2:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        meta_datas = data.get('meta_datas')
        ydlb = data.get('ydlb')
        if ydlb == '':
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        if ydlb == '一般耕地' or ydlb == '基本农田':
            ydxz = '田'
        elif ydlb == '湖泊水库' or ydlb == '坑塘沟渠' or ydlb == '河道' or ydlb == '现状水域':
            ydxz = '水'
        elif ydlb == '市政设施':
            ydxz = '市政设施'
        elif ydlb == '其他生态用地' or ydlb == '现状绿地':
            ydxz = '草'
        elif ydlb == '可造林区域（农用用地）' or ydlb == '现状林地' or ydlb == '可造林区域（清退用地）':
            ydxz = '林'
        elif ydlb == '保留村庄':
            ydxz = '保留村庄'
        elif ydlb == '工业园区':
            ydxz = '工业园区'
        elif ydlb == '交通设施':
            ydxz = '交通设施'
        else:
            return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
        total_area = 0
        item_area_percentage, item_area_dict, item_area1 = py_connection.sum_of_area()
        for k, v in item_area_dict.items():
            total_area += v
        for item_data in meta_datas:
            item_meta_ydxz = item_data.get('meta_ydxz')
            item_meta_shape_area = float(item_data.get('meta_shape_area'))
            item_area_dict[item_meta_ydxz] = float(item_area_dict[item_meta_ydxz])-item_meta_shape_area
            item_area_dict[ydxz] = float(item_area_dict[ydxz])+item_meta_shape_area
        percentage_area = {}
        for k, v in item_area_dict.items():
            v = '%.2f%%' % (float(v) / float(total_area) * 100)
            percentage_area[k] = v
        return jsonify(errorno=RET.OK, errmsg='成功', data=percentage_area)
    else:
        return jsonify(errorno=RET.REQERR, errmsg='非法请求')
