import psycopg2


# 数据库初始连接信息
def db_connection():
    try:
        coon = psycopg2.connect(database="JN_SYSTEM", user="postgres", password='123456', host='localhost',
                                port='5432')
        cur = coon.cursor()
        print('connected successful!!')
    except Exception as e:
        print('数据库连接失败%s' % e)
    return coon, cur


def kg_relation_dy():
    '''
    将单元编号和控规地块关联起来
    ST_DWithin(geomA, geomB, buffer_meter)
    其中一种用法是是在缓冲范围内A是否在B范围内
    :return:
    '''
    coon, cur = db_connection()
    try:
        pass
        sql_dy = "select gid, text, geom from danyuan"
        cur.execute(sql_dy)
        result_dy = cur.fetchall()
        for item_dy in result_dy:
            sql_kg = "update kg set dy_text='%s' where ST_DWithin(geom, '%s', 1)" % (item_dy[1], item_dy[2])
            cur.execute(sql_kg)
        coon.commit()
    except Exception as e:
        print(e)
        print('关联失败')


def kg_relation_dy_forienkey():
    '''
    alter table public.kg add constraint FK_ID foreign key(dy_gid) REFERENCES public.danyuan(gid)
    将单元编号和控规地块关联起来
    ST_DWithin(geomA, geomB, buffer_meter)
    其中一种用法是是在缓冲范围内A是否在B范围内
    :return:
    '''
    coon, cur = db_connection()
    try:
        pass
        sql_dy = "select gid, text, geom from danyuan"
        cur.execute(sql_dy)
        result_dy = cur.fetchall()
        for item_dy in result_dy:
            sql_kg = "update kg set dy_gid='%s' where ST_DWithin(geom, '%s', 1)" % (item_dy[0], item_dy[2])
            cur.execute(sql_kg)
        coon.commit()
    except Exception as e:
        print(e)
        print('关联失败')


if __name__ == '__main__':
    # kg_relation_dy()
    # kg_relation_dy_forienkey()
    pass