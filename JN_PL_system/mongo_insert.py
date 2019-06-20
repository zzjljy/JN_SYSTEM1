from pymongo import MongoClient
from .models import DL, DLHDM, DY, GKQXZ, KG, YJGKQ, ZJ, GX, YX


client = MongoClient(host='127.0.0.1', port=27017)
database = client.JN_SYSTEM


def dl_insert():
    collection = database.DL
    results = collection.find()
    for item in results:
        DL(x=item['x'], y=item['y'], z=item['z'], image=item['image']).save()


def dlhdm_insert():
    collection = database.DLHDM
    results = collection.find()
    for item in results:
        DLHDM(x=item['x'], y=item['y'], z=item['z'], image=item['image']).save()


def dy_insert():
    collection = database.DY
    results = collection.find()
    for item in results:
        DY(x=item['x'], y=item['y'], z=item['z'], image=item['image']).save()


def gkqxz_insert():
    collection = database.GKQXZ
    results = collection.find()
    for item in results:
        GKQXZ(x=item['x'], y=item['y'], z=item['z'], image=item['image']).save()


def kg_insert():
    collection = database.KG0309
    results = collection.find()
    for item in results:
        KG(x=item['x'], y=item['y'], z=item['z'], image=item['image']).save()


def yjgkq_insert():
    collection = database.YJGKQ_0521
    results = collection.find()
    for item in results:
        YJGKQ(x=item['x'], y=item['y'], z=item['z'], image=item['image']).save()


def zj_insert():
    collection = database.ZJ
    results = collection.find()
    for item in results:
        ZJ(x=item['x'], y=item['y'], z=item['z'], image=item['image']).save()


def gx_insert():
    collection = database.GX
    results = collection.find()
    for item in results:
        GX(x=item['x'], y=item['y'], z=item['z'], image=item['image']).save()


def yx_insert():
    collection = database.YX
    results = collection.find()
    for item in results:
        YX(x=item['x'], y=item['y'], z=item['z'], image=item['image']).save()
