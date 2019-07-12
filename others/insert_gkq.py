import psycopg2


coon = ''
cur = ''


# 数据库初始连接信息
def db_connection():
    try:
        global coon, cur
        coon = psycopg2.connect(database="JN_SYSTEM", user="postgres", password='123456', host='localhost',
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


def insert_to_yigkq(table_list):
    '''
    将各层的数据汇总
    :param table_list:
    :return:
    '''
    db_connection()
    for item_table in table_list:
        # input(item_table)
        sql = "select objectid_1, ydxz, ydlb, yddm, ydmc, shape_leng, shape_area, geom from %s" % item_table
        cur.execute(sql)
        results = cur.fetchall()
        i = 0
        for item in results:
            print(item)
            insert_sql = "insert into baoliucunzhuang(objectid_1, ydxz, ydlb, yddm, ydmc, shape_leng, shape_area,geom) values (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(insert_sql, [item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]])
        coon.commit()
        print(item_table, '插入完成')

    close()


def insert_gyq_to_gkq():
    db_connection()
    sql = "select objectid_1, objectid, ydxz, ydlb, yddm, ydmc, shape_leng, shape_area, geom from gongyequ"
    cur.execute(sql)
    results = cur.fetchall()
    i = 0
    for item in results:
        print(item)
        insert_sql = "insert into gkq(objectid_1,objectid, ydxz, ydlb, yddm, ydmc, shape_leng, shape_area,geom) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(insert_sql, [item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8]])
    coon.commit()

    close()


if __name__ == '__main__':
    table_list = [
        'gongyequ',
        'hedao',
        'huposhuiku',
        'jiaotongsheshi',
        'jibennongtian',
        'kengtanggouqu',
        'kezaolinquyu_nongyongdi',
        'kezaolinquyu_qingtuiyongdi_huangdikongdi',
        'qitashengtaiyongdi',
        'qitashengtaiyongdi_cunzhuanghe',
        'shizhengsheshi',
        'xianzhuanglindi',
        'xianzhuanglvdi',
        'xianzhuangshuiyu',
        'yibangengdi'
    ]
    # insert_to_yigkq(table_list)
    insert_gyq_to_gkq()
    pass
