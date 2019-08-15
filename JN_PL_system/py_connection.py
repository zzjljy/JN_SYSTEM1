import psycopg2
from config import Config
import re, json

coon = ''
cur = ''


# 数据库初始连接信息
def db_connection():
    try:
        global coon, cur
        # coon = psycopg2.connect(database="my_first_postgis", user="postgres", password='123456', host='localhost',
        #                         port='5432')
        # 以后用下面这个p
        # coon = db_coon
        coon = psycopg2.connect(database=Config.POSTGRES_DB, user=Config.POSTGRES_USER, password=Config.POSTGRES_PASSWORD, host=Config.POSTGRES_HOST,
                                port=Config.POSTGRES_PORT)
        cur = coon.cursor()
        print('connected successful!!')
    except Exception as e:
        print('数据库连接失败%s' % e)


# 数据库关闭连接
def coon_close():
    '''
    定义关闭数据库的连接
    :return:
    '''
    cur.close()
    coon.close()
    print('database has been closed!!')


'''-----------------控规地块----------------------'''


def kg_find_land(*args):
    '''
    控规地块查询，主要用地类型/设施名称查询
    :return:符合条件的dict数据
    '''
    db_connection()
    # table_name = get_table_name()
    if len(args) > 1:
        kg_ydxz = args[0]
        kg_ssmc = args[1]
        sql = "select ST_AsGeoJson(geom) from kg where ydxz='%s' and ssmc like '%%%s%%' order by gid asc" % (
        kg_ydxz, kg_ssmc)
    else:
        kg_ydxz = args[0]
        sql = "select ST_AsGeoJson(geom) from kg where ydxz='%s' order by gid asc" % kg_ydxz

    cur.execute(sql)
    results = cur.fetchall()
    finally_results = data_to_dict_coordinates(results)

    # except Exception as e:
    #     print('查询失败%s' % e)
    coon_close()
    return finally_results


def kg_find_elements_rjl(param1):
    '''
    控规要素查询，容积率和绿地率的查询
    容积率分五个层次，(0,1]，(1,2]...(4,]
    :return:符合条件的json数据
    '''
    db_connection()
    try:
        s_rjl = str(param1)[0]
        if s_rjl == '4':
            sql = "select ST_AsGeoJson(geom) from kg where rjl like '4%%' or rjl like '5%%'"
        else:
            sql = "select ST_AsGeoJson(geom) from kg where rjl like '%s%%'" % s_rjl
        cur.execute(sql)
        results = cur.fetchall()
        finally_result = data_to_dict_coordinates(results)
    except Exception as e:
        print('查询失败%s' % e)
        finally_result = 'ERROR'
    coon_close()
    return finally_result


def kg_find_elements_ldl(param1):
    '''
    控规要素查询，绿地率的查询
    绿地率分十个层次，(0,10],(10,20]...(90,100]
    :return:符合条件的json数据
    '''
    s_ldl = str(param1)[0]
    db_connection()
    try:
        if s_ldl == '0':
            sql = "select ST_AsGeoJson(geom) from kg where ldl ='1' or ldl ='0' or ldl ='2' or ldl ='3' or \
            ldl = '4' or ldl = '5' or ldl = '6' or ldl = '7' or ldl = '8' or ldl = '9'"
        else:
            sql = "select ST_AsGeoJson(geom) from kg where ldl like'%s%%' and ldl !='%s'" % (s_ldl, s_ldl)
        cur.execute(sql)
        results = cur.fetchall()
        results_i = data_to_dict_coordinates(results)
        finally_result = results_i
    except Exception as e:
        print('查询失败%s' % e)
        finally_result == 'ERROR'
        # finally_result = results_i = 'ERROR'
    # coon_close()
    return finally_result


def kg_search_land_info(*args):
    '''
    控规信息地块查询，点击地块，返回地块信息，
    参数xy点坐标
    :return:
    '''
    db_connection()
    try:
        x = args[0]
        y = args[1]
        sql = "select ST_AsGeoJson(geom), * from kg where st_within(GeomFromEWKT('SRID=4548;POINT(%s %s)'),geom) order by gid asc" % (x, y)
        cur.execute(sql)
        results = cur.fetchall()
        finally_result = data_to_dict(results)
    except Exception as e:
        print('查询失败%s' % e)
    return finally_result


def data_to_dict(data):
    '''
    将数据转为dict，所有数据
    :param data:
    :param table_name:
    :return:
    '''
    desc = cur.description
    table_name = []
    for s in desc:
        table_name.append(s.name)
    results = {}
    results["features"] = []
    for i in range(len(data)):
        item_dict = {}
        item_dict["attributes"] = {}
        for j in range(1, len(data[i])):
            if table_name[j] == 'geom':
                item_dict["geometry"] = json.loads(data[i][0])
            else:
                # shape_leng和shape_area 的类型为 数字类型
                if table_name[j] == 'shape_leng' or table_name[j] == 'shape_area':
                    item_dict["attributes"][table_name[j]] = float(str(data[i][j]))
                else:
                    item_dict["attributes"][table_name[j]] = str(data[i][j])
        results["features"].append(item_dict)
    return results


def data_to_dict_coordinates(data):
    '''
    将数据转为dict，只有坐标范围，其他的信息不要
    :param data:
    :return:
    '''
    results = {}
    results["features"] = []
    for i in range(len(data)):
        item_dict = {}
        item_dict["geometry"] = json.loads(data[i][0])
        results["features"].append(item_dict)
    return results


# 将控规数据转为json数据,最原始方法

def kg_data_to_dict(data):
    '''
    将查询出的数据进行整理，为dict格式
    :param data:
    :return:
    '''
    try:
        desc = cur.description
        table_name = []
        for s in desc:
            table_name.append(s.name)
        results = {}
        results["features"] = []
        if len(data) != 0:
            for i in range(len(data)):
                # 每一条数据是一个字典
                item_dict = {}
                item_dict["attributes"] = {}
                item_dict["geometry"] = {}
                for j in range(1, len(data[i])):
                    if table_name[j] != 'geom':
                        # shape_leng和shape_area 的类型为 数字类型
                        if table_name[j] == 'shape_leng' or table_name[j] == 'shape_area':
                            item_dict["attributes"][table_name[j]] = float(str(data[i][j]))
                        else:
                            item_dict["attributes"][table_name[j]] = str(data[i][j])
                    else:
                        # 判断有几个环
                        item_dict["geometry"]["rings"] = []
                        str1 = data[i][0]
                        p = re.compile(r'[(][(][(](.*)[)][)][)]', re.S)
                        # 列表类型的一条数据
                        s1 = re.findall(p, str1)
                        # print(s1)
                        # print('---------')
                        if ')),((' in s1[0]:
                            s2 = s1[0].split(')),((')
                            # print(type(s2), s2)
                            for s3 in s2:
                                # print(s3)
                                if '),(' not in s3:
                                    coor_list = []
                                    s4 = s3.split(",")
                                    for st in s4:
                                        s4 = st.split(" ")
                                        coor_list.append([float(s4[0]), float(s4[1])])
                                    item_dict["geometry"]["rings"].append(coor_list)
                                else:
                                    s4 = s3.split('),(')
                                    for s5 in s4:
                                        s6 = s5.split(",")
                                        coor_list = []
                                        for st in s6:
                                            s6 = st.split(" ")
                                            coor_list.append([float(s6[0]), float(s6[1])])
                                        item_dict["geometry"]["rings"].append(coor_list)
                                #     s2 = s1[0].split(')),((')

                        elif '),(' in s1[0]:
                            s2 = s1[0].split('),(')
                            for s3 in s2:
                                coor_list = []
                                s3 = s3.split(',')
                                for st in s3:
                                    s4 = st.split(" ")
                                    coor_list.append([float(s4[0]), float(s4[1])])
                                item_dict["geometry"]["rings"].append(coor_list)
                        else:
                            s2 = s1
                            for s3 in s2:
                                coor_list = []
                                s3 = s3.split(',')
                                for st in s3:
                                    s4 = st.split(" ")
                                    coor_list.append([float(s4[0]), float(s4[1])])
                                item_dict["geometry"]["rings"].append(coor_list)
                item_dict = item_dict
                results["features"].append(item_dict)
            # print(json.dumps(results, ensure_ascii=False))
        return results
    except Exception as e:
        print(e)
    # return results


'''------------------------道路查询-------------------'''


def dl_find_mc(dl_name):
    '''
    根据道路名称查询
    :return:
    '''
    db_connection()
    try:
        sql = "select ST_AsGeoJson(geom) from dl where dlmc='%s' order by gid asc" % dl_name
        cur.execute(sql)
        results = cur.fetchall()
        finally_result = data_to_dict_coordinates(results)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result
    pass


def dl_find_level(dl_level):
    '''
    根据道路级别进行查询
    :return:
    '''
    db_connection()
    try:
        sql = "select ST_AsGeoJson(geom) from dl where dldj='%s' order by gid asc" % dl_level
        cur.execute(sql)
        results = cur.fetchall()
        finally_result = data_to_dict_coordinates(results)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result
    pass


def dl_search_road_info(*args):
    '''
    道路信息查询，出现道路信息
    :return:
    '''
    db_connection()
    try:
        x = args[0]
        y = args[1]
        sql = "select ST_AsGeoJson(geom),* from public.dl where ST_DWithin(GeomFromEWKT('SRID=4548;POINT(%s %s)'),geom, 5) order by gid asc" % (x, y)
        cur.execute(sql)
        results = cur.fetchall()
        finally_result = data_to_dict(results)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    # print(finally_result)
    return finally_result


def kg_plot_way(gid):
    '''
    点击地块出现弹窗后，点击道路显示地块周围的道路信息
    标识地块的唯一参数gid传入，根据gid进行查询
    :return:
    '''
    gid = gid
    db_connection()
    try:
        sql = "select ST_AsGeoJson(geom),* from public.dlzxx where ST_DWithin((select geom from public.kg1 where " \
              "gid='%s'),geom,20.0) order by gid asc" % gid
        cur.execute(sql)
        results = cur.fetchall()
        finally_result = data_to_dict(results)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result
    pass


def dl_data_to_dict(data):
    '''
    道路数据处理，将道路数据转为json数据，最原始，现在不用
    :return:
    '''
    try:
        desc = cur.description
        table_name = []
        for s in desc:
            table_name.append(s.name)
        results = {}
        results["features"] = []
        if len(data) != 0:
            for i in range(len(data)):
                # 每一条数据是一个字典
                item_dict = {}
                item_dict["attributes"] = {}
                item_dict["geometry"] = {}
                for j in range(1, len(data[i])):
                    if table_name[j] != 'geom':
                        # shape_leng和shape_area 的类型为 数字类型
                        if table_name[j] == 'shape_leng':
                            item_dict["attributes"][table_name[j]] = float(str(data[i][j]))
                        else:
                            item_dict["attributes"][table_name[j]] = str(data[i][j])
                    else:
                        # 判断有几个环
                        item_dict["geometry"]["paths"] = []
                        str1 = data[i][0]
                        p = re.compile(r'[(][(](.*)[)][)]', re.S)
                        # 列表类型的一条数据
                        s1 = re.findall(p, str1)
                        # print('---------')
                        if '),(' in s1[0]:
                            s2 = s1[0].split('),(')
                            # print(len(s2), s2)
                        else:
                            s2 = s1
                        for s3 in s2:
                            coor_list = []
                            s3 = s3.split(',')
                            for st in s3:
                                s4 = st.split(" ")
                                coor_list.append([float(s4[0]), float(s4[1])])
                            item_dict["geometry"]["paths"].append(coor_list)
                item_dict = item_dict
                results["features"].append(item_dict)
        # return json.dumps(results, ensure_ascii=False)
        return results
    except Exception as e:
        print(e)
    pass


'''-------------------------------管线-------------------------------'''


def gx_plot_pipeline(gid):
    '''
    点击地块出现弹窗后，点击管线显示地块周围的管线信息
    标识地块的唯一参数gid传入，根据gid进行查询
    :param gid:
    :return:
    '''
    gid = gid
    db_connection()
    try:
        sql = "select ST_AsGeoJson(geom),* from public.gx where ST_DWithin((select geom from public.kg1 where " \
              "gid='%s'),geom,25.0) order by gid asc" % gid
        cur.execute(sql)
        results = cur.fetchall()
        finally_result = data_to_dict(results)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result
    pass


'''------------------------------一级管控区---------------------------------'''


def gkq_find_info(*args):
    '''
    点击一级管控区坐标
    由点坐标查询那一块的信息
    :param args:
    :return:
    '''
    x = args[0]
    y = args[1]
    db_connection()
    try:
        sql = "select ST_AsGeoJson(geom),* from gkq where st_within(GeomFromEWKT('SRID=32650;POINT(%s %s)'),geom)" % (x, y)
        cur.execute(sql)
        results = cur.fetchall()
        # for item in results:
        #     print(item)
        finally_result = data_to_dict(results)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result


def gkq_update_info_big(*args):
    '''
    管控区数据按照大类ydxz进行更改
    三个参数，地块唯一标识符gid，将要转换为的大类名称ydxz，将要转换为的小类名称ydlb
    :param args:
    :return:
    '''
    gid = args[0]
    ydxz = args[1]
    ydlb = args[2]
    db_connection()
    try:
        sql = "update gkq set ydxz='%s',ydlb='%s' where gid='%s'" % (ydxz, ydlb, gid)
        cur.execute(sql)
        coon.commit()
        msg = 'OK'
    except Exception as e:
        print('类型转换失败%s' % e)
        msg = 'ERROR'
    coon_close()
    return msg


def gkq_update_info_small(*args):
    '''
    一级管控区数据的转换根据小类型ydlb转换
    两个参数，地块的唯一标识符gid,将要转换为的用地类别ydlb
    :param args:
    :return:
    '''
    gid = args[0]
    ydlb = args[1]
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
        return 'ERROR'
    db_connection()
    try:
        sql = "update gkq set ydlb='%s',ydxz='%s' where gid='%s'" % (ydlb, ydxz, gid)
        cur.execute(sql)
        coon.commit()
        msg = 'OK'
    except Exception as e:
        print('类型转换失败%s' % e)
        msg = 'ERROR'
    coon_close()
    return msg


'''--------------管控区框选区域进行地块查询，进行地块转换-----------------'''


def gkq_find_info_custom(polygon):
    '''
    一级管控区自定义转换
    框选区域进行相交查询，将得到的结果返回
    如果就两个点，则用四个点构成有个polygon
    :param args:
    :return:
    '''
    db_connection()
    try:
        # polygon = '115924.61838536352 281700.1978399141,115963.565125079 281700.1978399141,115963.565125079 281640.5077189189,115924.61838536352 281640.5077189189,115924.61838536352 281700.1978399141'
        # polygon = '116526.59956833233 281435.1906739168,116600.68304983265 281435.1906739168,116600.68304983265 281385.23724390636,116526.59956833233 281385.23724390636,116526.59956833233 281435.1906739168'
        # polygon = '116526.59956833233 281435.1906739168,116600.68304983265 281435.1906739168,116600.68304983265 281385.23724390636,116526.59956833233 281385.23724390636,116526.59956833233 281435.1906739168'
        sql = "select ST_AsGeoJson(geom), * from gkq where ST_Intersects(GeomFromEWKT('SRID=32650;MULTIPOLYGON(((%s)))'),geom) order by gid asc" % polygon
        cur.execute(sql)
        result = cur.fetchall()
        finally_results = data_to_dict(result)
        # print(finally_result)
    except Exception as e:
        print('查询失败%s' % e)
    # coon_close()
    return finally_results


def gkq_custom_transformation_big(gid, ydxz, ydlb):
    '''
    自定义管控区查询
    根据选定区域的唯一表示符gid进行类型转换
    参数一是勾选的的gid，看选择的个数，列表形式
    参数二是将要转换为的大类的类型用地性质
    参数三是将要转换为的小类的类型用地类别
    :param args:
    :return:
    '''

    db_connection()
    try:
        ydxz = ydxz
        ydlb = ydlb
        for gid_item in gid:
            sql = "update gkq set ydxz='%s' ,ydlb='%s' where gid='%s'" % (ydxz, ydlb, gid_item)
            cur.execute(sql)
        coon.commit()
        print('类型转换成功')
        msg = 'OK'
    except Exception as e:
        print('类型转换错误%e' % e)
        msg = 'ERROR'
    coon_close()
    return msg


def gkq_custom_transformation_small(gid, ydlb):
    '''
    一级管控区根据小类别进行转换
    第一个参数是选择地块的唯一标识符gid,是gid组成的列表
    第二个参数是将要转为的小类型ydlb
    :param args:
    :return:
    '''
    gid = gid
    ydlb = ydlb
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
        return 'ERROR'
    db_connection()
    try:
        for item_gid in gid:
            sql = "update gkq set ydxz='%s', ydlb='%s' where gid='%s'" % (ydxz, ydlb, item_gid)
            cur.execute(sql)
        coon.commit()
        msg = 'OK'
    except Exception as e:
        print('类型转换失败%s' % e)
        msg = 'ERROR'
    coon_close()
    return msg


def sum_of_area():
    '''
    根据一级管控区不同的用地性质求和
    返回值是不同用地所占比例,字典形式，键：用地性质，值：所占百分比
    :return:
    '''
    db_connection()
    try:
        sql = "select distinct ydxz from gkq"
        cur.execute(sql)
        ydxz_results = cur.fetchall()
        area_dict = {}
        for ydxz_item in ydxz_results:
            a_sql = "select sum(shape_area) from gkq where ydxz='%s'" % ydxz_item[0]
            cur.execute(a_sql)
            area_dict[ydxz_item[0]] = cur.fetchall()[0][0]
        cur.execute("select sum(shape_area) from gkq")
        area_total = cur.fetchall()[0][0]
        percentage_area = {}
        for k, v in area_dict.items():
            v = '%.2f%%' % (v/area_total*100)
            percentage_area[k] = v
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return percentage_area, area_dict


'''---------------单元----------------'''


def dy_find_info_custom(polygon):
    '''
    根据polygon来查询范围内有哪些单元
    :param polygon: 由坐标点组成的polygon
    :return: 由单元信息组成的dict
    '''
    # 114246.43169079 274304.627395291,113634.68309079 274240.472595291,113611.75459079 274674.206295291,113601.78349079 274858.469995291,114202.25409079 274921.423395291,114246.43169079 274304.627395291
    polygon = polygon
    db_connection()
    try:
        sql = "select ST_AsGeoJson(geom), * from danyuan where ST_Intersects(GeomFromEWKT('SRID=32650;MULTIPOLYGON(((%s)))'),geom) order by gid asc" % polygon
        cur.execute(sql)
        result = cur.fetchall()
        # for item in result:
        #     print(item)
        finally_result = data_to_dict(result)
        # print(finally_result)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result


'''--------------图斑-----------------'''


def tb_find_info_custom(polygon):
    '''
    图斑自定义转换
    框选区域进行相交查询，将得到的结果返回
    如果就两个点，则用四个点构成有个polygon
    :param args:
    :return:
    '''
    db_connection()
    try:
        polygon = polygon
        sql = "select ST_AsGeoJson(geom), * from tuban where ST_Intersects(GeomFromEWKT('SRID=32650;MULTIPOLYGON(((%s)))'),geom) order by gid asc" % polygon
        cur.execute(sql)
        result = cur.fetchall()
        finally_result = data_to_dict(result)
        # print(finally_result)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result


def tb_find_info(*args):
    '''
    点击图斑坐标
    由点坐标查询那一块的信息
    :param args:
    :return:
    '''
    x = args[0]
    y = args[1]
    db_connection()
    try:
        sql = "select ST_AsGeoJson(geom),* from tuban where st_within(GeomFromEWKT('SRID=32650;POINT(%s %s)'),geom)" % (x, y)
        cur.execute(sql)
        results = cur.fetchall()
        # for item in results:
        #     print(item)
        finally_result = data_to_dict(results)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result


'''------------------------------'''


def czc_find_info_custom(polygon):
    '''
    城镇村自定义转换
    框选区域进行相交查询，将得到的结果返回
    如果就两个点，则用四个点构成有个polygon
    :param args:
    :return:
    '''
    db_connection()
    try:
        polygon = polygon
        sql = "select ST_AsGeoJson(geom), * from czc where ST_Intersects(GeomFromEWKT('SRID=32650;MULTIPOLYGON(((%s)))'),geom) order by gid asc" % polygon
        cur.execute(sql)
        result = cur.fetchall()
        finally_result = data_to_dict(result)
        # print(finally_result)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result


def czc_find_info(*args):
    '''
    点击城镇村坐标
    由点坐标查询那一块的信息
    :param args:
    :return:
    '''
    x = args[0]
    y = args[1]
    db_connection()
    try:
        sql = "select ST_AsGeoJson(geom),* from czc where st_within(GeomFromEWKT('SRID=32650;POINT(%s %s)'),geom)" % (x, y)
        cur.execute(sql)
        results = cur.fetchall()
        # for item in results:
        #     print(item)
        finally_result = data_to_dict(results)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result


'''----------------镇界---------------------'''


def zj_areas_geom():
    '''
    津南所有镇界的坐标范围信息
    :return:
    '''
    db_connection()
    try:
        sql = "select ST_AsGeoJson(geom) from zj "
        cur.execute(sql)
        results = cur.fetchall()
        finally_result = data_to_dict_coordinates(results)
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result


'''------------修详规-------------'''


def xxg_find_info(*args):
    '''
    修详规建筑及地界的信息
    :return:
    '''
    point_x = args[0]
    point_y = args[1]
    db_connection()
    try:
        sql_jianzhu = "select ST_AsGeoJson(geom),* from xxg_jianzhu where st_within(GeomFromEWKT('SRID=4548;POINT(%s %s)'),geom)" % (
        point_x, point_y)
        sql_dijie = "select ST_AsGeoJson(geom),* from xxg_dijie where st_within(GeomFromEWKT('SRID=4548;POINT(%s %s)'),geom)" % (
            point_x, point_y)
        cur.execute(sql_jianzhu)
        results = cur.fetchall()
        result_jianzhu = data_to_dict(results)
        cur.execute(sql_dijie)
        result_dijie = data_to_dict(cur.fetchall())
        finally_result = {'修详规建筑': result_jianzhu, '修详规地界':result_dijie}
    except Exception as e:
        print('查询失败%s' % e)
    coon_close()
    return finally_result


'''-------------------------------'''


if __name__ == '__main__':
    # results = kg_find_land('商业金融业用地', '')
    # print(results)
    # s = kg_search_land_info(120197.800092194, 278553.847476402)
    # s = dl_find_mc('昌盛路')
    # print(s)
    # print(results)
    # s = gkq_find_info(113550.176112053, 274596.480054953)
    # s = gkq_update_info_big(1, '水', '坑塘沟渠')
    # s = gkq_update_info_small(1, '其他生态用地')
    # print(s)
    '''
    MULTIPOLYGON ZM (((122869.566101074 278635.717102051 0 -1.79769e+308,122871.94654105 278638.225935593 0 -1.79769e+308,122871.990112305 278638.268758138 0 -1.79769e+308,122877.6796875 278644.258300781 0 -1.79769e+308,122884.00411377 278637.275671387 0 -1.79769e+308,122888.662902832 278632.121704102 0 -1.79769e+308,122872.873474121 278614.760498047 0 -1.79769e+308,122853.772094727 278595.501098633 0 -1.79769e+308,122837.82989502 278583.874328613 0 -1.79769e+308,122795.057128906 278544.600097656 0 -1.79769e+308,122800.015075684 278538.182495117 0 -1.79769e+308,122778.40667076 278516.452521098 0 -1.79769e+308,122776.622680664 278514.658508301 0 -1.79769e+308,122771.520679931 278510.690321743 0 -1.79769e+308,122768.942696082 278508.685292328 0 -1.79769e+308,122763.110745895 278504.157953583 0 -1.79769e+308,122755.722290039 278514.718078613 0 -1.79769e+308,122753.487930884 278517.978811172 0 -1.79769e+308,122756.219482422 278520.210083008 0 -1.79769e+308,122749.581695557 278527.022216797 0 -1.79769e+308,122752.689858718 278529.257018641 0 -1.79769e+308,122779.962402344 278548.868347168 0 -1.79769e+308,122779.846384905 278548.999096837 0 -1.79769e+308,122735.851654053 278598.136489868 0 -1.79769e+308,122736.636105719 278598.89298374 0 -1.79769e+308,122783.451388192 278643.96549332 0 -1.79769e+308,122825.293273926 278684.246704102 0 -1.79769e+308,122859.602686258 278646.64579092 0 -1.79769e+308)))
    '''
    # s = gkq_find_info_custom('122859 278646,122869 278635, 122871 278638, 122859 278646')
    # print(s)
    # msg = gkq_custom_transformation_big([1, 2, '600'], '水', '河道')
    # print(msg)
    # s = sum_of_area()
    # s = kg_find_land('一类工业用地', '')
    # print(s)
    # s = kg_find_elements_rjl(4,10)
    # print(s)
    # s = kg_find_elements_ldl(0, 10)
    # print(s)
    # s = gkq_find_info_custom1('1')
    # print(s)
    # s = dl_search_road_info(117514, 276346)
    # s = gkq_find_info(106813.14432421184,278812.2142569655)
    # s = gkq_find_info(113850.49293056593, 270824.6366815064)
    # s = gkq_find_info_custom('116433.26752061576 281414.5202492552,116486.18429311595 281414.5202492552,116486.18429311595 281403.5135670346,116433.26752061576 281403.5135670346,116433.26752061576 281414.5202492552')
    # s = kg_find_elements_ldl(60, 70)
    # s = dy_find_info_custom('114246.43169079 274304.627395291,113634.68309079 274240.472595291,113611.75459079 274674.206295291,113601.78349079 274858.469995291,114202.25409079 274921.423395291,114246.43169079 274304.627395291')
    # s = gkq_find_info(118816.09705427944, 287153.42964271747)
    # s = kg_search_land_info(534892.4672422454, 4316697.275458975)
    # s = zj_areas_geom()
    s = xxg_find_info(524544.891276536, 4320727.24522591)
    print(s)