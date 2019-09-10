from pymongo import MongoClient
from .models import DL, DLHDM, DY, GKQXZ, KG, YJGKQ, ZJ, GX, YX, DLHDM_IMG, TB, FWGJ


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


def dlhdm_img_insert():
    collection = database.DLHDM_image
    results = collection.find()
    for item in results:
        DLHDM_IMG(image_objectid=item['image_objectid'], image=item['image_content']).save()


def tb_insert():
    collection = database.TB
    results = collection.find()
    for item in results:
        TB(x=item['x'], y=item['y'], z=item['z'], image=item['image']).save()


def kg_insert_new():
    # -*- coding: ascii -*-
    import os
    import struct
    from pymongo import MongoClient
    # dblocation=r'C:\Users\95768\Desktop\tjdmapt.db'#'H:\\Project\\AndroidProject\\WAMap\\tjdmapb.sqlitedb'
    agscachedir = r'C:\Users\95768\Desktop\111\JN_JNKG0809\tuceng\_alllayers'
    class structtype:
        pass

    bundleinfo = structtype()
    dirstru = os.walk(agscachedir)
    for diritem in dirstru:
        print(diritem)
        if len(diritem[2]) > 0:
            for dirfile in diritem[2]:
                if os.path.splitext(dirfile)[1] == '.bundle':
                    filename = os.path.join(diritem[0], dirfile)
                    bundlefn = os.path.split(filename)
                    print(bundlefn)
                    level = (os.path.split(bundlefn[0])[1])[1:]
                    # level = string.atoi(level, 10)
                    level = int(level)
                    print(level)
                    # print(bundlefn[1])
                    ri = bundlefn[1].find('R')
                    ci = bundlefn[1].find('C')
                    fnNoext = os.path.splitext(bundlefn[1])[0]
                    # print(fnNoext)
                    startrow = int(fnNoext[ri + 1:ci], 16)
                    startcol = int(fnNoext[ci + 1:], 16)
                    print(int(fnNoext[ri + 1:ci]), int(fnNoext[ci + 1:]))
                    print(startcol, startrow)
                    file = open(filename, 'rb')
                    tilecount = 16384
                    bundlxpos = [0] * tilecount
                    bundlecon = file.read(64 + tilecount * 8)
                    (bundleinfo.version, bundleinfo.numRecords, bundleinfo.maxRecordSize, bundleinfo.filePointerSize,
                     bundleinfo.freeSpace, bundleinfo.fileSize, bundleinfo.userHeaderPos, bundleinfo.u,
                     bundleinfo.MinRow,
                     bundleinfo.MaxRow, bundleinfo.MinCol, bundleinfo.MaxCol) = struct.unpack('Iiiiqqqiiiii',
                                                                                              bundlecon[:60])
                    tileoffsetsize_con = bundlecon[64:64 + tilecount * 8]
                    for i in range(tilecount):
                        index103 = i
                        # python3???????//
                        index10 = 128 * (i % 128) + (i // 128)
                        (xpos, xlen) = struct.unpack('ii', tileoffsetsize_con[i * 8:(i + 1) * 8])
                        if xpos - 4 > 0:
                            bundlxpos[index10] = xpos - 4
                        else:
                            bundlxpos[index10] = 64 + 8 * i + 4
                    if int(level) <= 8:
                        # dict_list = []
                        for i in range(128):
                            for j in range(128):
                                irow = startrow + j
                                icol = startcol + i
                                index = 128 * i + j
                                # ??????????????
                                file.seek(bundlxpos[index])
                                tilelen, = struct.unpack('i', file.read(4))
                                # print tilelen, bundlxpos
                                if tilelen > 0:
                                    binaryTile = file.read(tilelen)
                                    item_data = {}
                                    item_data["x"] = irow
                                    item_data["y"] = icol
                                    item_data["z"] = level
                                    item_data["image"] = binaryTile
                                    try:
                                        KG(x=irow, y=icol, z=level, image=binaryTile).save()

                                    except Exception as e:
                                        print(e)
                                        print(int(fnNoext[ri + 1:ci]), int(fnNoext[ci + 1:]))
                                        print(irow, icol, level)
                                        img = open('image.png', 'wb')
                                        img.write(binaryTile)
                                        img.close()
                                        err_info = open('./err_info.txt', 'a')
                                        err_info.write(str(item_data))
                                        err_info.write('\n')
                                        err_info.close()
                                        input('continue,,,,,,,,')
                        file.close()


def yx_insert_new():
    # -*- coding: ascii -*-
    import os
    import struct
    from pymongo import MongoClient
    # dblocation=r'C:\Users\95768\Desktop\tjdmapt.db'#'H:\\Project\\AndroidProject\\WAMap\\tjdmapb.sqlitedb'
    agscachedir = r'C:\Users\95768\Desktop\111\JN_JNDY0827\tuceng\_alllayers'
    class structtype:
        pass

    bundleinfo = structtype()
    dirstru = os.walk(agscachedir)
    for diritem in dirstru:
        print(diritem)
        if len(diritem[2]) > 0:
            for dirfile in diritem[2]:
                if os.path.splitext(dirfile)[1] == '.bundle':
                    filename = os.path.join(diritem[0], dirfile)
                    bundlefn = os.path.split(filename)
                    print(bundlefn)
                    level = (os.path.split(bundlefn[0])[1])[1:]
                    # level = string.atoi(level, 10)
                    level = int(level)
                    print(level)
                    # print(bundlefn[1])
                    ri = bundlefn[1].find('R')
                    ci = bundlefn[1].find('C')
                    fnNoext = os.path.splitext(bundlefn[1])[0]
                    # print(fnNoext)
                    startrow = int(fnNoext[ri + 1:ci], 16)
                    startcol = int(fnNoext[ci + 1:], 16)
                    print(int(fnNoext[ri + 1:ci]), int(fnNoext[ci + 1:]))
                    print(startcol, startrow)
                    file = open(filename, 'rb')
                    tilecount = 16384
                    bundlxpos = [0] * tilecount
                    bundlecon = file.read(64 + tilecount * 8)
                    (bundleinfo.version, bundleinfo.numRecords, bundleinfo.maxRecordSize, bundleinfo.filePointerSize,
                     bundleinfo.freeSpace, bundleinfo.fileSize, bundleinfo.userHeaderPos, bundleinfo.u,
                     bundleinfo.MinRow,
                     bundleinfo.MaxRow, bundleinfo.MinCol, bundleinfo.MaxCol) = struct.unpack('Iiiiqqqiiiii',
                                                                                              bundlecon[:60])
                    tileoffsetsize_con = bundlecon[64:64 + tilecount * 8]
                    for i in range(tilecount):
                        index103 = i
                        # python3???????//
                        index10 = 128 * (i % 128) + (i // 128)
                        (xpos, xlen) = struct.unpack('ii', tileoffsetsize_con[i * 8:(i + 1) * 8])
                        if xpos - 4 > 0:
                            bundlxpos[index10] = xpos - 4
                        else:
                            bundlxpos[index10] = 64 + 8 * i + 4
                    if int(level) <= 8:
                        # dict_list = []
                        for i in range(128):
                            for j in range(128):
                                irow = startrow + j
                                icol = startcol + i
                                index = 128 * i + j
                                # ??????????????
                                file.seek(bundlxpos[index])
                                tilelen, = struct.unpack('i', file.read(4))
                                # print tilelen, bundlxpos
                                if tilelen > 0:
                                    binaryTile = file.read(tilelen)
                                    item_data = {}
                                    item_data["x"] = irow
                                    item_data["y"] = icol
                                    item_data["z"] = level
                                    item_data["image"] = binaryTile
                                    try:
                                        DL(x=irow, y=icol, z=level, image=binaryTile).save()

                                    except Exception as e:
                                        print(e)
                                        print(int(fnNoext[ri + 1:ci]), int(fnNoext[ci + 1:]))
                                        print(irow, icol, level)
                                        img = open('image.png', 'wb')
                                        img.write(binaryTile)
                                        img.close()
                                        err_info = open('./err_info.txt', 'a')
                                        err_info.write(str(item_data))
                                        err_info.write('\n')
                                        err_info.close()
                                        input('continue,,,,,,,,')
                        file.close()


def yjgkq_insert_new():
    # -*- coding: ascii -*-
    import os
    import struct
    from pymongo import MongoClient
    # dblocation=r'C:\Users\95768\Desktop\tjdmapt.db'#'H:\\Project\\AndroidProject\\WAMap\\tjdmapb.sqlitedb'
    agscachedir = r'C:\Users\95768\Desktop\111\JN_JNYX0909\tuceng\_alllayers'
    class structtype:
        pass

    bundleinfo = structtype()
    dirstru = os.walk(agscachedir)
    for diritem in dirstru:
        print(diritem)
        if len(diritem[2]) > 0:
            for dirfile in diritem[2]:
                if os.path.splitext(dirfile)[1] == '.bundle':
                    filename = os.path.join(diritem[0], dirfile)
                    bundlefn = os.path.split(filename)
                    print(bundlefn)
                    level = (os.path.split(bundlefn[0])[1])[1:]
                    # level = string.atoi(level, 10)
                    level = int(level)
                    print(level)
                    # print(bundlefn[1])
                    ri = bundlefn[1].find('R')
                    ci = bundlefn[1].find('C')
                    fnNoext = os.path.splitext(bundlefn[1])[0]
                    # print(fnNoext)
                    startrow = int(fnNoext[ri + 1:ci], 16)
                    startcol = int(fnNoext[ci + 1:], 16)
                    print(int(fnNoext[ri + 1:ci]), int(fnNoext[ci + 1:]))
                    print(startcol, startrow)
                    file = open(filename, 'rb')
                    tilecount = 16384
                    bundlxpos = [0] * tilecount
                    bundlecon = file.read(64 + tilecount * 8)
                    (bundleinfo.version, bundleinfo.numRecords, bundleinfo.maxRecordSize, bundleinfo.filePointerSize,
                     bundleinfo.freeSpace, bundleinfo.fileSize, bundleinfo.userHeaderPos, bundleinfo.u,
                     bundleinfo.MinRow,
                     bundleinfo.MaxRow, bundleinfo.MinCol, bundleinfo.MaxCol) = struct.unpack('Iiiiqqqiiiii',
                                                                                              bundlecon[:60])
                    tileoffsetsize_con = bundlecon[64:64 + tilecount * 8]
                    for i in range(tilecount):
                        index103 = i
                        # python3???????//
                        index10 = 128 * (i % 128) + (i // 128)
                        (xpos, xlen) = struct.unpack('ii', tileoffsetsize_con[i * 8:(i + 1) * 8])
                        if xpos - 4 > 0:
                            bundlxpos[index10] = xpos - 4
                        else:
                            bundlxpos[index10] = 64 + 8 * i + 4
                    if int(level) <= 8:
                        # dict_list = []
                        for i in range(128):
                            for j in range(128):
                                irow = startrow + j
                                icol = startcol + i
                                index = 128 * i + j
                                # ??????????????
                                file.seek(bundlxpos[index])
                                tilelen, = struct.unpack('i', file.read(4))
                                # print tilelen, bundlxpos
                                if tilelen > 0:
                                    binaryTile = file.read(tilelen)
                                    item_data = {}
                                    item_data["x"] = irow
                                    item_data["y"] = icol
                                    item_data["z"] = level
                                    item_data["image"] = binaryTile
                                    try:
                                        YX(x=irow, y=icol, z=level, image=binaryTile).save()

                                    except Exception as e:
                                        print(e)
                                        print(int(fnNoext[ri + 1:ci]), int(fnNoext[ci + 1:]))
                                        print(irow, icol, level)
                                        img = open('image.png', 'wb')
                                        img.write(binaryTile)
                                        img.close()
                                        err_info = open('./err_info.txt', 'a')
                                        err_info.write(str(item_data))
                                        err_info.write('\n')
                                        err_info.close()
                                        input('continue,,,,,,,,')
                        file.close()

