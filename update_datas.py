import psycopg2


coon = ''
cur = ''


# 数据库初始连接信息
def db_connection():
    try:
        global coon, cur
        coon = psycopg2.connect(database="my_first_postgis", user="postgres", password='123456', host='localhost',
                                port='5432')
        cur = coon.cursor()
        print('connected successful!!')
    except Exception as e:
        print('数据库连接失败%s' % e)


def close():
    '''
    定义关闭数据库的连接
    :return:
    '''
    cur.close()
    coon.close()
    print('database has been closed!!')


def update_kg():
    '''
    控规地块的更改，将坐标提取出来以文本方式存储
    :return:
    '''
    db_connection()
    try:
        sql = "select ST_AsText(geom), is_change, gid from kg1"
        cur.execute(sql)
        results = cur.fetchall()
        length = len(results)
        for i in range(length):
            item_points = results[i][0]
            is_change = results[i][1]
            gid = results[i][2]
            if not is_change or is_change == '':
                sql = "update kg1 set geom_text='%s', is_change=True where gid='%s'" % (item_points, gid)
                cur.execute(sql)
                coon.commit()
                print('gid为%s的插入成功' % gid)
            else:
                print('gid为%s的geom_text数据已经存在' % gid)
    except Exception as e:
        print('查询失败%s' % e)
    close()


def update_dl():
    '''
    道路中心线信息的修改，提取道路点坐标转换为文本格式
    :return:
    '''
    db_connection()
    try:
        sql = "select ST_AsText(geom), is_change, gid from dlzxx"
        cur.execute(sql)
        results = cur.fetchall()
        length = len(results)
        for i in range(length):
            item_points = results[i][0]
            is_change = results[i][1]
            gid = results[i][2]
            if not is_change or is_change == '':
                sql = "update dlzxx set geom_text='%s', is_change=True where gid='%s'" % (item_points, gid)
                cur.execute(sql)
                coon.commit()
                print('gid为%s的插入成功' % gid)
            else:
                print('gid为%s的geom_text数据已经存在' % gid)
    except Exception as e:
        print('查询失败%s' % e)
    close()


def update_yjgkq():
    '''
    一级管控区信息的修改，提取道路点坐标转换为文本格式
    :return:
    '''
    db_connection()
    try:
        sql = "select ST_AsText(geom), is_change, gid from yjgkq"
        cur.execute(sql)
        results = cur.fetchall()
        length = len(results)
        for i in range(length):
            item_points = results[i][0]
            is_change = results[i][1]
            gid = results[i][2]
            if not is_change or is_change == '':
                sql = "update yjgkq set geom_text='%s', is_change=True where gid='%s'" % (item_points, gid)
                cur.execute(sql)
                coon.commit()
                print('gid为%s的插入成功' % gid)
            else:
                print('gid为%s的geom_text数据已经存在' % gid)
    except Exception as e:
        print('查询失败%s' % e)
    close()


def kg():
    '''
    一级管控区信息的修改，提取道路点坐标转换为文本格式
    :return:
    '''
    db_connection()
    try:
        sql = "select *, ST_AsText(geom), geom_text from yjgkq order by gid asc"
        cur.execute(sql)
        results = cur.fetchall()
        for item in results:
            print(item)
    except Exception as e:
        print('查询失败%s' % e)
    close()


if __name__ == '__main__':
    # update_kg()
    # update_dl()
    # update_yjgkq()
    kg()