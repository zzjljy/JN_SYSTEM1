from flask import Blueprint, request, jsonify
from .. import py_connection
from JN_PL_system.utils.response_code import RET

gx = Blueprint('gx', __name__)


@gx.route('/JN/JN_GX/gx_plot_pipeline/', methods=['POST'])
def gx_plot_pipeline():
    '''
    根据地块的唯一标识符gid查找地块周围的管线
    :return:
    '''
    kg_data = request.get_json('data')
    if not kg_data:
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    gid = kg_data.get('gid')
    try:
        data = py_connection.gx_plot_pipeline(gid)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')
