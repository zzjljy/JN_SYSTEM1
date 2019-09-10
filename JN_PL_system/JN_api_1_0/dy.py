from io import BytesIO

from flask import Blueprint, request, jsonify, send_file
from .. import py_connection
from JN_PL_system.utils.response_code import RET
import json, pymongo, zipfile
from config import Config, TestConfig
from gridfs import *
from .. import app


coon = pymongo.MongoClient(Config.MONGODB_HOST, Config.MONGODB_PORT)
db = coon.JN_SYSTEM
fs = GridFS(db, collection='DY_DATA')
dy = Blueprint('dy', __name__)


# 自定义范围查询
@dy.route('/JN/JN_DY/dy_find_info_custom/', methods=['GET'])
def dy_find_info_custom():
    '''
    单元自定义转换，框选区域进行转换
    参数：由点坐标构成的polygon
    点坐标至少三个不同的点
    字典形式，{'rings':[[point1],[point2],[point3],....[point1]]}
    :return:
    '''
    dy_data = request.args
    # print(dy_data)
    for k, v in dy_data.to_dict().items():
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
        data = py_connection.dy_find_info_custom(polygon)
        # print('数据', data)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@dy.route('/JN/JN_DY/data_download/<target_fid>/', methods=['GET'])
def dy_data_downloads(target_fid):
    '''
    单元对应资料下载
    json数据：
            target_fid:0
    :return:
    '''
    # 获取参数
    if request.method == 'GET':
        target_fid = str(target_fid)
        objects = fs.find({'target_fid': target_fid})
        # print(list(objects))
        if objects.count() == 0:
            return jsonify(errorno=4503, errmsg='数据不存在')
        dl_name = '{}.zip'.format(target_fid)
        memory_file = BytesIO()
        with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            for object in objects:
                datas = fs.get(object._id).read()
                zf.writestr(object.file_name + '.' + object.file_type, datas)
        memory_file.seek(0)
        return send_file(memory_file, attachment_filename=dl_name,  as_attachment=True)
    else:
        return jsonify(errorno=RET.REQERR, errmsg='非法请求')


@dy.route('/JN1/JN_DY/data_download/<target_fid>/', methods=['GET'])
def dy1_data_downloads(target_fid):
    '''
    单元对应资料下载
    json数据：
            target_fid:0
    :return:
    '''
    # 获取参数
    import os
    if request.method == 'GET':
        target_fid = str(target_fid)
        file_name = os.path.dirname(app.instance_path)
        file = os.path.join(file_name, 'JN_PL_system\\static\\files', target_fid+'.zip')

        return send_file(file, attachment_filename=target_fid+'.zip',  as_attachment=True)

    else:
        return jsonify(errorno=RET.REQERR, errmsg='非法请求')
