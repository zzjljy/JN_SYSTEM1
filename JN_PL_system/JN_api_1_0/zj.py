from flask import Blueprint, request, jsonify
from .. import py_connection
from JN_PL_system.utils.response_code import RET
zj = Blueprint('zj', __name__)


@zj.route('/JN/JN_ZJ/', methods=['GET'])
def jn_zj():
    '''
    返回镇界的所有范围，由前端进行画出范围
    :return:
    '''
    # 获取参数
    try:
        data = py_connection.zj_areas_geom()
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')

