from . import db


class BaseModel(object):
    '''
    所有模型基类
    '''
    x = db.IntField()
    y = db.IntField()
    z = db.IntField()
    image = db.BinaryField()


# 影像
class YX(BaseModel, db.Document):
    __doc__ = 'JN_YX'


# 道路
class DL(BaseModel, db.Document):
    __doc__ = 'JN_DL'


# 道路横断面
class DLHDM(BaseModel, db.Document):
    __doc__ = 'JN_DLHDM'


# 单元
class DY(BaseModel, db.Document):
    __doc__ = 'JN_DY'


class GKQXZ(BaseModel, db.Document):
    __doc__ = 'JN_GKQXZ'


class GX(BaseModel, db.Document):
    __doc__ = 'JN_GX'


class KG(BaseModel, db.Document):
    __doc__ = 'JN_KG'


class YJGKQ(BaseModel, db.Document):
    __doc__ = 'JN_YJGKQ'


class ZJ(BaseModel, db.Document):
    __doc__ = 'JN_ZJ'


class DLHDM_IMG(db.Document):
    __doc__ = 'JN_DLHDM_IMG'
    image_objectid = db.IntField()
    image = db.BinaryField()
