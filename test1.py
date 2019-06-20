# from JN_PL_system import py_connection
# s = {
#     'gid': [1, 2],
#     'ydxz': '保留村庄',
#     'ydlb': '保留村庄1'
# }
# gid = s.get('gid')
# ydxz = s.get('ydxz')
# ydlb = s.get('ydlb')
# res = py_connection.gkq_custom_transformation_big(gid, ydxz, ydlb)
# print(res)
# from pymongo import MongoClient
# MONGODB_PORT = 27017
# MONGODB_HOST = "127.0.0.1"
# MONGODB_DB = "JN_SYSTEM"
# MONGODB_USERNAME = "dbuser"
# MONGODB_PASSWORD = "dbpasswd"
# client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
# db = client.JN_SYSTEM
# con = db.DL
# result = con.find()
# for item in result:
#     print(item)
