from flask import Blueprint, jsonify, make_response
from JN_PL_system.utils.response_code import RET
from ..models import YJGKQ, DL, DLHDM, DY, GKQXZ, GX, KG, ZJ, YX


tile = Blueprint('tile', __name__)


@tile.route('/JN/JNYX/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jnyx_tile(x, y, z):
    '''
    请求津南影像瓦片数据,
    png图片
    :param x:
    :param y:
    :param z:
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=4103, errmsg='参数错误')
    try:
        dl_tile = YX.objects(x=x, y=y, z=z).first()
        if dl_tile != None:
            image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=4001, errmsg='查询数据库错误')


@tile.route('/JN/JNDL/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jndl_tile(x, y, z):
    '''
    请求津南道路瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = DL.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNDLHDM/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jndlhdm_tile(x, y, z):
    '''
    请求津南道路横断面瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = DLHDM.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNDY/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jndy_tile(x, y, z):
    '''
    请求津南单元瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = DY.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNGKQXZ/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jngkqxz_tile(x, y, z):
    '''
    请求津南管控区现状瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = GKQXZ.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNGX/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jngx_tile(x, y, z):
    '''
    请求津南管管线瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = GX.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNKG/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jnkg_tile(x, y, z):
    '''
    请求津南控规瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = KG.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNYJGKQ/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jnyjgkq_tile(x, y, z):
    '''
    请求津南一级管控区瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = YJGKQ.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNZJ/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jnzj_tile(x, y, z):
    '''
    请求津南镇界瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        zj_tile = ZJ.objects(x=x, y=y, z=z).first()
        if zj_tile == None:
            return jsonify(errorno=RET.PARAMERR, errmsg='瓦片参数错误')
        else:
            image = zj_tile['image']
            response = make_response(image)
            response.headers['Content-Type'] = 'image/png'
            return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')
