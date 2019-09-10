from flask import Blueprint, request, jsonify, make_response, send_file
from .. import py_connection
from JN_PL_system.utils.response_code import RET
import json
from datetime import datetime
import random, string
import flask_excel as excel


kg = Blueprint('kg', __name__)


@kg.route('/JN/JN_KG/search_info', methods=['GET'])
def kg_info_find():
    '''
    控规信息查询，根据用地类型和、设施名称
    最开始以json方式传数据 ImmutableMultiDict([('key', '{"ydxz":"一类工业用地","ssmc":"公厕"}')])
    现在改为request.args.get()方式
    :return:
    '''
    yddm = request.args.get('yddm')
    ssmc = request.args.get('ssmc')
    dybh = request.args.get('dybh')
    if yddm == None and ssmc != '':
        if dybh == None:
            data = py_connection.kg_find_land({'ssmc': ssmc})
        else:
            # 加入单元编号的查询
            dy_gid = dybh.split(',')
            data = py_connection.kg_find_land({'ssmc': ssmc, 'dybh': dy_gid})
        if data != 'ERROR':
            return jsonify(errorno=RET.OK, errmsg='成功', data=data)
        else:
            return jsonify({'error': '查询错误'})
    elif yddm != '' and ssmc == None:
        if dybh == None:
            print('无地块编号的用地代码')
            data = py_connection.kg_find_land({'yddm': yddm})
        else:
            # 加入单元编号后查询
            dy_gid = dybh.split(',')
            data = py_connection.kg_find_land({'yddm': yddm, 'dybh': dy_gid})
        if data != 'ERROR':
            return jsonify(errorno=RET.OK, errmsg='成功', data=data)
        else:
            return jsonify({'error': '查询错误'})
    elif yddm != '' and ssmc != '':
        if dybh == None:
            # 在所有的单元中进行查询
            data = py_connection.kg_find_land({'yddm': yddm, 'ssmc': ssmc})
        else:
            # 加入单元编号查询
            dy_gid = dybh.split(',')
            data = py_connection.kg_find_land({'yddm': yddm, 'ssmc': ssmc, 'dybh': dy_gid})
        if data != 'ERROR':
            return jsonify(errorno=RET.OK, errmsg='成功', data=data)
        else:
            return jsonify({'error': '查询错误'})
        pass
    else:
        return jsonify(errorno=RET.PARAMERR, errmsg='两个参数不能同时为空')


@kg.route('/JN/JN_KG/search_info/download', methods=['GET'])
def kg_info_download():
    '''
    对查询的信息进行下载
    :return:
    '''
    yddm = request.args.get('yddm')
    ssmc = request.args.get('ssmc')
    dybh = request.args.get('dybh')
    if yddm == None and ssmc != '':
        if dybh == None:
            data, table_name = py_connection.kg_find_land_download({'ssmc': ssmc})
        else:
            dybh = dybh.split(',')
            data, table_name = py_connection.kg_find_land_download({'ssmc': ssmc, 'dybh': dybh})
        if data != 'ERROR':
            kg_data, excel_name = data_to_excel(data, table_name)
            return excel.make_response_from_array(kg_data, "xlsx",
                                                  file_name=excel_name)
        else:
            return jsonify({'error': '查询错误'})
    elif yddm != '' and ssmc == None:
        if dybh == None:
            data, table_name = py_connection.kg_find_land_download({'yddm': yddm})
        else:
            dybh = dybh.split(',')
            data, table_name = py_connection.kg_find_land_download({'yddm': yddm, 'dybh': dybh})
        if data != 'ERROR':
            kg_data, excel_name = data_to_excel(data, table_name)
            return excel.make_response_from_array(kg_data, "xlsx",
                                                  file_name=excel_name)
        else:
            return jsonify({'error': '查询错误'})
    elif yddm != '' and ssmc != '':
        if dybh == None:
            data, table_name = py_connection.kg_find_land_download({'yddm': yddm, 'ssmc': ssmc})
        else:
            dybh = dybh.split(',')
            data, table_name = py_connection.kg_find_land_download({'yddm': yddm, 'ssmc': ssmc, 'dybh': dybh})
        if data != 'ERROR':
            if len(data) != 0:
                kg_data, excel_name = data_to_excel(data, table_name)
                return excel.make_response_from_array(kg_data, "xlsx",
                                                  file_name=excel_name)
            else:
                return jsonify({'error': '没有查询到符合条件的数据'})
        else:
            return jsonify({'error': '查询错误'})
    else:
        return jsonify(errorno=RET.PARAMERR, errmsg='两个参数不能同时为空')


def data_to_excel(data, table_name):
    '''
    将查询到的数据写入excel表格并返回前端下载
    :param data:
    :return:
    '''
    # today = datetime.today()
    # today_date = datetime.date(today)
    ran_str = ''.join(random.sample(string.digits, 10))
    excel_name = '控规-' + ran_str
    kg_data = []
    table_name.remove('GID')
    table_name.remove('GEOM')
    kg_data.append(table_name)
    for data_item in data:
        item_list = []
        for item in data_item:
            if item != data_item[0] or item != data_item[-3]:
                item_list.append(item)
        kg_data.append(item_list)
    return kg_data, excel_name


@kg.route('/JN/JN_KG/search_element/RJL/<int:rjl_min>/', methods=['GET'])
def kg_element_find_rjl(rjl_min):
    '''
    根据控规用地绿地率或容积率进行查询
    :return:
    '''
    # 获取参数
    s_rjl = rjl_min
    try:
        data = py_connection.kg_find_elements_rjl(s_rjl)
        # print(data)
        if data != 'ERROR':
            return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@kg.route('/JN/JN_KG/search_element/LDL/<int:ldl_min>/', methods=['GET'])
def kg_element_find_ldl(ldl_min):
    '''
    根据控规用地绿地率或容积率进行查询
    :return:
    '''
    # 获取参数
    s_ldl = ldl_min
    try:
        data = py_connection.kg_find_elements_ldl(s_ldl)
        # print(data)
        if data != 'ERROR':
            return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@kg.route('/JN/JN_KG/JZMD/<string:jzmd>/', methods=['GET'])
def kg_jzmd(jzmd):
    '''
    根据控规建筑密度进行查询
    :return:
    '''
    # 获取参数
    jzmd = jzmd
    try:
        if jzmd != '':
            data = py_connection.kg_find_jzmd(jzmd)
            if data != 'ERROR':
                return jsonify(errorno=RET.OK, errmsg='成功', data=data)
        else:
            return jsonify({'参数错误': '参数不能为空'})
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@kg.route('/JN/JN_KG/kg_search_land/<float:point_x>/<float:point_y>/', methods=['GET'])
def kg_search_land_info(point_x, point_y):
    '''
    根据点坐标查询地块信息
    :return:
    '''
    # 获取参数
    x = float(point_x)
    y = float(point_y)
    if not(x, y):
        return jsonify(errorno=RET.PARAMERR, errmsg='参数错误')
    try:
        data = py_connection.kg_search_land_info(x, y)
        # print(data)
        return jsonify(errorno=RET.OK, errmsg='成功', data=data)
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')
