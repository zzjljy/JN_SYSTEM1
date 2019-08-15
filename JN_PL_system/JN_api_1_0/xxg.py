from flask import Blueprint, request, jsonify
from .. import py_connection
from JN_PL_system.utils.response_code import RET
xxg = Blueprint('xxg', __name__)


@xxg.route('/JN/JN_XXG/xxg_find_info/<float:point_x>/<float:point_y>/', methods=['GET'])
def gkq_find_info(point_x, point_y):
    '''
    修详规查询，返回建筑信息（房屋和公建）和地界信息
    :return:
    '''
    # 获取参数
    x = point_x
    y = point_y
    if not(x, y):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.xxg_find_info(x, y)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')

