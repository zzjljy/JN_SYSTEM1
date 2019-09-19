from flask import Blueprint, request, jsonify, make_response, send_file, redirect, url_for
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
            print('无地块编号的用地代码查询')
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
            print(11111111111)
            data, table_name = py_connection.kg_find_land_download({'ssmc': ssmc})
        else:
            dybh = dybh.split(',')
            data, table_name = py_connection.kg_find_land_download({'ssmc': ssmc, 'dybh': dybh})
        if data != 'ERROR':
            # pass
            # pdf
            # path = generate_pdf(table_name, data)
            # return path
            # excel
            # kg_data, excel_name = data_to_excel(data, table_name)
            # return excel.make_response_from_array(kg_data, "xlsx",
            #                                       file_name=excel_name)
            # 图片
            im_new = image(table_name, data)
            from io import BytesIO
            buf = BytesIO()
            im_new.save(buf, 'PNG')
            buf_str = buf.getvalue()
            response = make_response(buf_str)
            response.headers['Content-Type'] = 'image/png'
            return response
            # return redirect(url_for('kg.image', table_header=table_name, datas=data))
        else:
            return jsonify({'error': '查询错误'})
    elif yddm != '' and ssmc == None:
        if dybh == None:
            print('无单元编号的用地代码下载')
            data, table_name = py_connection.kg_find_land_download({'yddm': yddm})
        else:
            dybh = dybh.split(',')
            data, table_name = py_connection.kg_find_land_download({'yddm': yddm, 'dybh': dybh})
        if data != 'ERROR':
            # path = generate_pdf(table_name, data)
            # return path
            im_new = image(table_name, data)
            from io import BytesIO
            buf = BytesIO()
            im_new.save(buf, 'PNG')
            buf_str = buf.getvalue()
            response = make_response(buf_str)
            response.headers['Content-Type'] = 'image/png'
            return response
            # return redirect(url_for('kg.image', table_header=table_name, datas=data))
            # kg_data, excel_name = data_to_excel(data, table_name)
            # return excel.make_response_from_array(kg_data, "xlsx",
            #                                       file_name=excel_name)
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
                # path = generate_pdf(table_name, data)
                # return path
                im_new = image(table_name, data)
                from io import BytesIO
                buf = BytesIO()
                im_new.save(buf, 'PNG')
                buf_str = buf.getvalue()
                response = make_response(buf_str)
                response.headers['Content-Type'] = 'image/png'
                return response
                # return redirect(url_for('kg.image', table_header=table_name, datas=data))
                # kg_data, excel_name = data_to_excel(data, table_name)
                # return excel.make_response_from_array(kg_data, "xlsx",
                #                                   file_name=excel_name)
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
    ran_str = ''.join(random.sample(string.digits, 10))
    excel_name = '控规-' + ran_str
    kg_data = []
    table_name.remove('GID')
    table_name.remove('GEOM')
    kg_data.append(table_name)
    for data_item in data:
        item_list = []
        for item in data_item:
            item_list.append(item)
        del item_list[0]
        del item_list[-3]
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



#暂未解决中文乱码问题
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, Frame, PageBreak, Paragraph, LongTable, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors, fonts
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 增加的字体，支持中文显示,需要自行下载支持中文的字体

# styles.add(ParagraphStyle(fontName='SimSun', name='SimSun', leading=20, fontSize=12))
# Paragraph('描述', styles['SimSun'])


def table_model(table_header, datas):
    """
    添加表格
    :return:
    """
    base = []
    del table_header[0], table_header[-3], table_header[-1]
    base.append(table_header)
    for data_row in datas:
        item_row_list = []
        for item in data_row:
            item_row_list.append(str(item))
        del item_row_list[0], item_row_list[-3], item_row_list[-1]
        base.append(item_row_list)
    # print(base)
    pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))
    # fonts.addMapping('SimSun', 0, 0, 'SimSun')
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(fontName='SimSun', name='SimSun', leading=20, fontSize=12))
    styleN = styles['SimSun']
    # styleN.wordWrap = 'CJK'
    # base = [['gid', 'objectid', 'dkbh', 'yddm', 'ydxz', 'ydmj', 'rjl', 'jzxg', 'jzmd', 'ldl', 'ssmc'],
    #               ['1', '1', '01-37', 'C3', '文化娱乐用地', '34567.9', '1.1', '/', '', '35', '厕所1处'],
    #               ]

    style = [
        # 设置字体
        # (列,行)
        ('fontName', (0, 0), (-1, -1), 'SimSun'),

        # 字体颜色
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#548DD4')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.antiquewhite),
        # 对齐设置
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

        # 单元格框线
        # 表格内部线的颜色
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        # 表格四个框线的颜色
        ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
        ('WordWrap', (0, 0), (-1, -1), True)

    ]
    base2 = [[Paragraph(cell, styleN) for cell in row] for row in base]
    # frame = Frame(10, 10, 420, 590, id='normal')
    # colwidths = [frame._width/3. for i in range(3)]
    component_table = Table(base2, colWidths=[70, 43, 38, 120, 80, 38, 38, 38, 38, 80, 70, 70, 70, 70, 70, 80, 100, 100, \
                                              130], style=style)
    return component_table


def generate_pdf(table_header, datas):
    """
    生成pdf
    :return:
    """
    path = "test.pdf"
    data = list()
    # 添加table
    table = table_model(table_header, datas)
    data.append(table)
    data.append(PageBreak())  # 分页标识
    # 设置生成pdf的名字和编剧
    pdf = SimpleDocTemplate(path, rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)
    # 设置pdf每页的大小
    pdf.pagesize = (20 * inch, 16 * inch)

    pdf.multiBuild(data)

    # buff.seek(0)
    # return buff
    return path


@kg.route('/testPDF', methods=["GET"])
def test_pdf():
    """
    测试输出pdf
    :return:
    """
    path = generate_pdf(1, 1)
    # return send_file(path, attachment_filename='test.pdf', as_attachment=True)
    return path


# @kg.route('/download/image/<table_header>/<datas>/')
def image(table_header, datas):
    from prettytable import PrettyTable
    from PIL import Image, ImageDraw, ImageFont
    tab = PrettyTable()
    # del table_header[0], table_header[-3], table_header[-1]
    tab.field_names = [table_header[0], table_header[1], table_header[2], table_header[3], table_header[4],\
                       table_header[5], table_header[6], table_header[7], table_header[8], table_header[9],\
                       table_header[-5], table_header[-4], table_header[-2], table_header[10], table_header[11],\
                       table_header[12], table_header[13], table_header[14], table_header[15], table_header[16]]
    for data_row in datas:
        item_row_list = []
        for item in data_row:
            if item == '/' or item == '—' or item == None:
                item_row_list.append('/')
            else:
                item_row_list.append(str(item).strip())
        # del item_row_list[0], item_row_list[-3], item_row_list[-1]
        item_row_list = [item_row_list[0], item_row_list[1], item_row_list[2], item_row_list[3], item_row_list[4],\
                         item_row_list[5], item_row_list[6], item_row_list[7], item_row_list[8], item_row_list[9],\
                         item_row_list[-5], item_row_list[-4], item_row_list[-2], item_row_list[10], item_row_list[11],\
                         item_row_list[12], item_row_list[13], item_row_list[14], item_row_list[15], item_row_list[16]]
        tab.add_row(item_row_list)
    tab_info = str(tab)
    space = 5

    # PIL模块中，确定写入到图片中的文本字体
    font = ImageFont.truetype(r'D:\new_py_project\JN_PM_system\evne\Lib\site-packages\reportlab\fonts\SimSun.ttf', 15, encoding='utf-8')
    # Image模块创建一个图片对象
    im = Image.new('RGB', (10, 10), (0, 0, 0, 0))
    # ImageDraw向图片中进行操作，写入文字或者插入线条都可以
    draw = ImageDraw.Draw(im, "RGB")
    # 根据插入图片中的文字内容和字体信息，来确定图片的最终大小
    img_size = draw.multiline_textsize(tab_info, font=font)
    # 图片初始化的大小为10-10，现在根据图片内容要重新设置图片的大小
    im_new = im.resize((img_size[0] + space * 2, img_size[1] + space * 2))
    del draw
    del im
    draw = ImageDraw.Draw(im_new, 'RGB')
    # 批量写入到图片中，这里的multiline_text会自动识别换行符
    # python3
    draw.multiline_text((space, space), tab_info, fill=(255, 255, 255), font=font)
    return im_new

    # im_new.save('12345.PNG', "PNG")
    # del draw
    # return 'hello world'

