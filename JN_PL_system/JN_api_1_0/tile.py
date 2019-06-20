from flask import Blueprint, request, jsonify, Response, send_file
from JN_PL_system.utils.response_code import RET
from ..models import YJGKQ, DL, DLHDM, DY, GKQXZ, GX, KG, ZJ
import io


tile = Blueprint('tile', __name__)


@tile.route('JN/JNYX/MapServer/tile/<int:x>/<int:y>/<int:z>/', methods=['GET'])
def get_jnyx_tile(x, y, z):
    '''
    请求津南影像瓦片数据
    :param x:
    :param y:
    :param z:
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    try:
        pass
    except Exception as e:
        pass


@tile.route('JN/JNDL/MapServer/tile/<int:x>/<int:y>/<int:z>/')
def get_jndl_tile(x, y, z):
    '''
    请求津南道路瓦片数据
    :param x:
    :param y:
    :param z:
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = DL.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        print(image)
        return jsonify(errorno=RET.OK, errmsg='成功', data=dl_tile)
        # data = Response(image, minetype="image/jpg")
        # return send_file(io.BytesIO(image.read()), attachment_filename='tile.jpg', mimetype='image/jpg')
    except Exception as e:
        print('e')
