import json
from flask import Blueprint, jsonify, make_response
from JN_PL_system.utils.response_code import RET
from ..models import YJGKQ, DL, DLHDM, DY, GKQXZ, GX, KG, ZJ, YX, TB, FWGJ


tile = Blueprint('tile', __name__)


@tile.route('/JN/JNYX/MapServer/')
def get_jnyx_mapserver():
    s = '{"currentVersion":10.4,"serviceDescription":"","mapName":"图层","description":"","copyrightText":"","supportsDynamicLayers":false,"layers":[{"id":0,"name":"津南2000.tif","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0}],"tables":[],"spatialReference":{"wkid":4548,"latestWkid":4548},"singleFusedMapCache":true,"tileInfo":{"rows":256,"cols":256,"dpi":96,"format":"JPEG","compressionQuality":75,"origin":{"x":450000,"y":4500000},"spatialReference":{"wkid":4548,"latestWkid":4548},"lods":[{"level":0,"resolution":66.1459656252646,"scale":250000},{"level":1,"resolution":33.0729828126323,"scale":125000},{"level":2,"resolution":16.933367200067735,"scale":64000},{"level":3,"resolution":8.466683600033868,"scale":32000},{"level":4,"resolution":4.233341800016934,"scale":16000},{"level":5,"resolution":2.116670900008467,"scale":8000},{"level":6,"resolution":1.0583354500042335,"scale":4000},{"level":7,"resolution":0.5291677250021167,"scale":2000}]},"initialExtent":{"xmin":515553.2078085329,"ymin":4290961.276294501,"xmax":550832.0112841823,"ymax":4337169.591435156,"spatialReference":{"wkid":4548,"latestWkid":4548}},"fullExtent":{"xmin":517225.96390916087,"ymin":4299813.985908369,"xmax":549297.6034324785,"ymax":4328317.039779668,"spatialReference":{"wkid":4548,"latestWkid":4548}},"minScale":250000,"maxScale":2000,"units":"esriMeters","supportedImageFormatTypes":"PNG32,PNG24,PNG,JPG,DIB,TIFF,EMF,PS,PDF,GIF,SVG,SVGZ,BMP","documentInfo":{"Title":"","Author":"","Comments":"","Subject":"","Category":"","AntialiasingMode":"None","TextAntialiasingMode":"Force","Keywords":""},"capabilities":"Map,Query,Data","supportedQueryFormats":"JSON, AMF, geoJSON","exportTilesAllowed":false,"maxRecordCount":1000,"maxImageHeight":4096,"maxImageWidth":4096,"tileServers":"","supportedExtensions":"KmlServer"}'
    return jsonify(json.loads(s))


@tile.route('/JN/JNZJ/MapServer/')
def get_jnzj_mapserver():
    info = '{"currentVersion":10.4,"serviceDescription":"","mapName":"图层","description":"","copyrightText":"","supportsDynamicLayers":false,"layers":[{"id":0,"name":"津南镇界注记350000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[1],"minScale":350000,"maxScale":250001},{"id":1,"name":"默认","parentLayerId":0,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":2,"name":"津南镇界注记250000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[3],"minScale":250000,"maxScale":200001},{"id":3,"name":"默认","parentLayerId":2,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":4,"name":"津南镇界注记150000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[5],"minScale":150000,"maxScale":100001},{"id":5,"name":"默认","parentLayerId":4,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":6,"name":"津南镇界注记200000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[7],"minScale":200000,"maxScale":150001},{"id":7,"name":"默认","parentLayerId":6,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":8,"name":"津南镇界注记100000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[9],"minScale":100000,"maxScale":80001},{"id":9,"name":"默认","parentLayerId":8,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":10,"name":"津南镇界注记80000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[11],"minScale":80000,"maxScale":60001},{"id":11,"name":"默认","parentLayerId":10,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":12,"name":"津南镇界注记60000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[13],"minScale":60000,"maxScale":40001},{"id":13,"name":"默认","parentLayerId":12,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":14,"name":"津南镇界注记40000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[15],"minScale":40000,"maxScale":30001},{"id":15,"name":"默认","parentLayerId":14,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":16,"name":"津南镇界注记30000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[17],"minScale":30000,"maxScale":20001},{"id":17,"name":"默认","parentLayerId":16,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":18,"name":"津南镇界注记20000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[19],"minScale":20000,"maxScale":10001},{"id":19,"name":"默认","parentLayerId":18,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":20,"name":"津南镇界注记8000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[21],"minScale":10000,"maxScale":8000},{"id":21,"name":"默认","parentLayerId":20,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":22,"name":"津南镇界注记4000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[23],"minScale":7999,"maxScale":4000},{"id":23,"name":"默认","parentLayerId":22,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":24,"name":"津南镇界注记2000","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":[25],"minScale":3999,"maxScale":2000},{"id":25,"name":"默认","parentLayerId":24,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":26,"name":"镇界1","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":500000,"maxScale":150001},{"id":27,"name":"镇界1","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":150000,"maxScale":8001},{"id":28,"name":"镇界1","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":8000,"maxScale":2000}],"tables":[],"spatialReference":{"wkid":32650,"latestWkid":32650},"singleFusedMapCache":true,"tileInfo":{"rows":256,"cols":256,"dpi":96,"format":"PNG32","compressionQuality":0,"origin":{"x":0,"y":480000},"spatialReference":{"wkid":32650,"latestWkid":32650},"lods":[{"level":0,"resolution":132.2919312505292,"scale":500000.00000000006},{"level":1,"resolution":66.1459656252646,"scale":250000.00000000003},{"level":2,"resolution":33.0729828126323,"scale":125000.00000000001},{"level":3,"resolution":16.933367200067735,"scale":64000},{"level":4,"resolution":8.466683600033868,"scale":32000},{"level":5,"resolution":4.233341800016934,"scale":16000},{"level":6,"resolution":2.116670900008467,"scale":8000},{"level":7,"resolution":1.0583354500042335,"scale":4000},{"level":8,"resolution":0.5291677250021167,"scale":2000}]},"initialExtent":{"xmin":105642.72482931444,"ymin":274367.6293933934,"xmax":123555.0523206361,"ymax":289104.9505347023,"spatialReference":{"wkid":32650,"latestWkid":32650}},"fullExtent":{"xmin":101592.327057,"ymin":268631.36424,"xmax":130901.09097800001,"ymax":294567.08761000005,"spatialReference":{"wkid":32650,"latestWkid":32650}},"minScale":500000.00000000006,"maxScale":2000,"units":"esriMeters","supportedImageFormatTypes":"PNG32,PNG24,PNG,JPG,DIB,TIFF,EMF,PS,PDF,GIF,SVG,SVGZ,BMP","documentInfo":{"Title":"","Author":"","Comments":"","Subject":"","Category":"","AntialiasingMode":"None","TextAntialiasingMode":"Force","Keywords":""},"capabilities":"Map,Query,Data","supportedQueryFormats":"JSON, AMF, geoJSON","exportTilesAllowed":false,"maxRecordCount":1000,"maxImageHeight":4096,"maxImageWidth":4096,"tileServers":"","supportedExtensions":"KmlServer"}'
    return jsonify(json.loads(info))


@tile.route('/JN/JNDL/MapServer/')
def get_jndl_mapserver():
    info = '{"currentVersion":10.4,"serviceDescription":"","mapName":"图层","description":"","copyrightText":"","supportsDynamicLayers":false,"layers":[{"id":0,"name":"dl","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0}],"tables":[],"spatialReference":{"wkid":32650,"latestWkid":32650},"singleFusedMapCache":true,"tileInfo":{"rows":256,"cols":256,"dpi":96,"format":"PNG32","compressionQuality":0,"origin":{"x":0,"y":480000},"spatialReference":{"wkid":32650,"latestWkid":32650},"lods":[{"level":0,"resolution":132.2919312505292,"scale":500000.00000000006},{"level":1,"resolution":66.1459656252646,"scale":250000.00000000003},{"level":2,"resolution":33.0729828126323,"scale":125000.00000000001},{"level":3,"resolution":16.933367200067735,"scale":64000},{"level":4,"resolution":8.466683600033868,"scale":32000},{"level":5,"resolution":4.233341800016934,"scale":16000},{"level":6,"resolution":2.116670900008467,"scale":8000},{"level":7,"resolution":1.0583354500042335,"scale":4000},{"level":8,"resolution":0.5291677250021167,"scale":2000},{"level":9,"resolution":0.26458386250105836,"scale":1000}]},"initialExtent":{"xmin":119484.52713972479,"ymin":276645.7220492722,"xmax":121055.49382332482,"ymax":278269.60550537234,"spatialReference":{"wkid":32650,"latestWkid":32650}},"fullExtent":{"xmin":117112.19567871094,"ymin":274626.58349609375,"xmax":121920.5423449105,"ymax":279322.4063374013,"spatialReference":{"wkid":32650,"latestWkid":32650}},"minScale":500000.00000000006,"maxScale":2000,"units":"esriMeters","supportedImageFormatTypes":"PNG32,PNG24,PNG,JPG,DIB,TIFF,EMF,PS,PDF,GIF,SVG,SVGZ,BMP","documentInfo":{"Title":"","Author":"","Comments":"","Subject":"","Category":"","AntialiasingMode":"None","TextAntialiasingMode":"Force","Keywords":""},"capabilities":"Map,Query,Data","supportedQueryFormats":"JSON, AMF, geoJSON","exportTilesAllowed":false,"maxRecordCount":1000,"maxImageHeight":4096,"maxImageWidth":4096,"tileServers":"","supportedExtensions":"KmlServer"}'
    return jsonify(json.loads(info))


@tile.route('/JN/JNKG/MapServer/')
def get_jnkg_mapserver():
    info = '{"currentVersion":10.4,"serviceDescription":"","mapName":"图层","description":"","copyrightText":"","supportsDynamicLayers":false,"layers":[{"id":0,"name":"津南控规","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0}],"tables":[],"spatialReference":{"wkid":4548,"latestWkid":4548},"singleFusedMapCache":true,"tileInfo":{"rows":256,"cols":256,"dpi":96,"format":"PNG32","compressionQuality":0,"origin":{"x":450000,"y":4500000},"spatialReference":{"wkid":4548,"latestWkid":4548},"lods":[{"level":0,"resolution":66.1459656252646,"scale":250000},{"level":1,"resolution":33.0729828126323,"scale":125000},{"level":2,"resolution":16.933367200067735,"scale":64000},{"level":3,"resolution":8.466683600033868,"scale":32000},{"level":4,"resolution":4.233341800016934,"scale":16000},{"level":5,"resolution":2.116670900008467,"scale":8000},{"level":6,"resolution":1.0583354500042335,"scale":4000},{"level":7,"resolution":0.5291677250021167,"scale":2000}]},"initialExtent":{"xmin":520949.6879218029,"ymin":4301757.9643392945,"xmax":549265.5886124297,"ymax":4327431.550080307,"spatialReference":{"wkid":4548,"latestWkid":4548}},"fullExtent":{"xmin":522236.77431683143,"ymin":4302924.945509341,"xmax":547978.5022174012,"ymax":4326264.568910261,"spatialReference":{"wkid":4548,"latestWkid":4548}},"minScale":250000,"maxScale":2000,"units":"esriMeters","supportedImageFormatTypes":"PNG32,PNG24,PNG,JPG,DIB,TIFF,EMF,PS,PDF,GIF,SVG,SVGZ,BMP","documentInfo":{"Title":"","Author":"","Comments":"","Subject":"","Category":"","AntialiasingMode":"None","TextAntialiasingMode":"Force","Keywords":""},"capabilities":"Map,Query,Data","supportedQueryFormats":"JSON, AMF, geoJSON","exportTilesAllowed":false,"maxRecordCount":1000,"maxImageHeight":4096,"maxImageWidth":4096,"tileServers":"","supportedExtensions":""}'
    return jsonify(json.loads(info))


@ tile.route('/JN/JNYJGKQ/MapServer/')
def get_yjgkq_mapserver():
    info = '{"currentVersion":10.4,"serviceDescription":"","mapName":"图层","description":"","copyrightText":"","supportsDynamicLayers":false,"layers":[{"id":0,"name":"dl","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0}],"tables":[],"spatialReference":{"wkid":32650,"latestWkid":32650},"singleFusedMapCache":true,"tileInfo":{"rows":256,"cols":256,"dpi":96,"format":"PNG32","compressionQuality":0,"origin":{"x":0,"y":480000},"spatialReference":{"wkid":32650,"latestWkid":32650},"lods":[{"level":0,"resolution":132.2919312505292,"scale":500000.00000000006},{"level":1,"resolution":66.1459656252646,"scale":250000.00000000003},{"level":2,"resolution":33.0729828126323,"scale":125000.00000000001},{"level":3,"resolution":16.933367200067735,"scale":64000},{"level":4,"resolution":8.466683600033868,"scale":32000},{"level":5,"resolution":4.233341800016934,"scale":16000},{"level":6,"resolution":2.116670900008467,"scale":8000},{"level":7,"resolution":1.0583354500042335,"scale":4000},{"level":8,"resolution":0.5291677250021167,"scale":2000},{"level":9,"resolution":0.26458386250105836,"scale":1000}]},"initialExtent":{"xmin":104088.53373718262,"ymin":267465.59414367675,"xmax":132175.47108459473,"ymax":293099.00284118654,"spatialReference":{"wkid":32650,"latestWkid":32650}},"fullExtent":{"xmin":105365.21270751953,"ymin":268630.74908447266,"xmax":130898.79211425781,"ymax":291933.8479003906,"spatialReference":{"wkid":32650,"latestWkid":32650}},"minScale":500000.00000000006,"maxScale":2000,"units":"esriMeters","supportedImageFormatTypes":"PNG32,PNG24,PNG,JPG,DIB,TIFF,EMF,PS,PDF,GIF,SVG,SVGZ,BMP","documentInfo":{"Title":"","Author":"","Comments":"","Subject":"","Category":"","AntialiasingMode":"None","TextAntialiasingMode":"Force","Keywords":""},"capabilities":"Map,Query,Data","supportedQueryFormats":"JSON, AMF, geoJSON","exportTilesAllowed":false,"maxRecordCount":1000,"maxImageHeight":4096,"maxImageWidth":4096,"tileServers":"","supportedExtensions":"KmlServer"}'
    return jsonify(json.loads(info))


@ tile.route('/JN/JNDY/MapServer/')
def get_dy_mapserver():
    info = '{"currentVersion":10.4,"serviceDescription":"","mapName":"图层","description":"","copyrightText":"","supportsDynamicLayers":false,"layers":[{"id":0,"name":"dl","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0}],"tables":[],"spatialReference":{"wkid":32650,"latestWkid":32650},"singleFusedMapCache":true,"tileInfo":{"rows":256,"cols":256,"dpi":96,"format":"PNG32","compressionQuality":0,"origin":{"x":0,"y":480000},"spatialReference":{"wkid":32650,"latestWkid":32650},"lods":[{"level":0,"resolution":132.2919312505292,"scale":500000.00000000006},{"level":1,"resolution":66.1459656252646,"scale":250000.00000000003},{"level":2,"resolution":33.0729828126323,"scale":125000.00000000001},{"level":3,"resolution":16.933367200067735,"scale":64000},{"level":4,"resolution":8.466683600033868,"scale":32000},{"level":5,"resolution":4.233341800016934,"scale":16000},{"level":6,"resolution":2.116670900008467,"scale":8000},{"level":7,"resolution":1.0583354500042335,"scale":4000},{"level":8,"resolution":0.5291677250021167,"scale":2000}]},"initialExtent":{"xmin":107657.07015630748,"ymin":281432.208071329,"xmax":120224.80362510774,"ymax":286379.9263000988,"spatialReference":{"wkid":32650,"latestWkid":32650}},"fullExtent":{"xmin":104871.83910823558,"ymin":270394.10159529134,"xmax":130868.15409079017,"ymax":293932.2971931844,"spatialReference":{"wkid":32650,"latestWkid":32650}},"minScale":500000.00000000006,"maxScale":2000,"units":"esriMeters","supportedImageFormatTypes":"PNG32,PNG24,PNG,JPG,DIB,TIFF,EMF,PS,PDF,GIF,SVG,SVGZ,BMP","documentInfo":{"Title":"","Author":"","Comments":"","Subject":"","Category":"","AntialiasingMode":"Best","TextAntialiasingMode":"None","Keywords":""},"capabilities":"Map,Query,Data","supportedQueryFormats":"JSON, AMF, geoJSON","exportTilesAllowed":false,"maxRecordCount":1000,"maxImageHeight":4096,"maxImageWidth":4096,"tileServers":"","supportedExtensions":"KmlServer"}'
    return jsonify(json.loads(info))


@ tile.route('/JN/JNTB/MapServer/')
def get_tb_mapserver():
    info = '{"currentVersion":10.4,"serviceDescription":"","mapName":"图层","description":"","copyrightText":"","supportsDynamicLayers":false,"layers":[{"id":0,"name":"地类图斑0506","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0}],"tables":[],"spatialReference":{"wkid":4548,"latestWkid":4548},"singleFusedMapCache":true,"tileInfo":{"rows":256,"cols":256,"dpi":96,"format":"PNG32","compressionQuality":0,"origin":{"x":0,"y":480000},"spatialReference":{"wkid":4548,"latestWkid":4548},"lods":[{"level":0,"resolution":132.2919312505292,"scale":500000},{"level":1,"resolution":66.1459656252646,"scale":250000},{"level":2,"resolution":33.0729828126323,"scale":125000},{"level":3,"resolution":16.933367200067735,"scale":64000},{"level":4,"resolution":8.466683600033868,"scale":32000},{"level":5,"resolution":4.233341800016934,"scale":16000},{"level":6,"resolution":2.116670900008467,"scale":8000},{"level":7,"resolution":1.0583354500042335,"scale":4000},{"level":8,"resolution":0.5291677250021167,"scale":2000},{"level":9,"resolution":0.26458386250105836,"scale":1000}]},"initialExtent":{"xmin":105042.93331125034,"ymin":271616.6324187075,"xmax":137493.43493002566,"ymax":300171.81624875416,"spatialReference":{"wkid":4548,"latestWkid":4548}},"fullExtent":{"xmin":101391.82414721622,"ymin":268609.9588623792,"xmax":130892.28016428469,"ymax":294569.21688969433,"spatialReference":{"wkid":4548,"latestWkid":4548}},"minScale":500000,"maxScale":2000,"units":"esriMeters","supportedImageFormatTypes":"PNG32,PNG24,PNG,JPG,DIB,TIFF,EMF,PS,PDF,GIF,SVG,SVGZ,BMP","documentInfo":{"Title":"","Author":"","Comments":"","Subject":"","Category":"","AntialiasingMode":"None","TextAntialiasingMode":"Force","Keywords":""},"capabilities":"Map,Query,Data","supportedQueryFormats":"JSON, AMF, geoJSON","exportTilesAllowed":false,"maxRecordCount":1000,"maxImageHeight":4096,"maxImageWidth":4096,"tileServers":"","supportedExtensions":"KmlServer"}'
    return jsonify(json.loads(info))


@ tile.route('/JN/JNFWGJ/MapServer/')
def get_fwgj_mapserver():
    info = '{"currentVersion":10.4,"serviceDescription":"","mapName":"图层","description":"","copyrightText":"","supportsDynamicLayers":false,"layers":[{"id":0,"name":"公建","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":1,"name":"房屋","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":2,"name":"车位","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0},{"id":3,"name":"地界","parentLayerId":-1,"defaultVisibility":true,"subLayerIds":null,"minScale":0,"maxScale":0}],"tables":[],"spatialReference":{"wkid":4548,"latestWkid":4548},"singleFusedMapCache":true,"tileInfo":{"rows":256,"cols":256,"dpi":96,"format":"PNG32","compressionQuality":0,"origin":{"x":450000,"y":4500000},"spatialReference":{"wkid":4548,"latestWkid":4548},"lods":[{"level":0,"resolution":66.1459656252646,"scale":250000},{"level":1,"resolution":33.0729828126323,"scale":125000},{"level":2,"resolution":16.933367200067735,"scale":64000},{"level":3,"resolution":8.466683600033868,"scale":32000},{"level":4,"resolution":4.233341800016934,"scale":16000},{"level":5,"resolution":2.116670900008467,"scale":8000},{"level":6,"resolution":1.0583354500042335,"scale":4000},{"level":7,"resolution":0.5291677250021167,"scale":2000}]},"initialExtent":{"xmin":522900.8453929988,"ymin":4315656.3874322185,"xmax":537995.9662906898,"ymax":4325995.240710441,"spatialReference":{"wkid":4548,"latestWkid":4548}},"fullExtent":{"xmin":523586.9872519847,"ymin":4316126.3353085015,"xmax":537309.8244317038,"ymax":4325525.292834158,"spatialReference":{"wkid":4548,"latestWkid":4548}},"minScale":250000,"maxScale":2000,"units":"esriMeters","supportedImageFormatTypes":"PNG32,PNG24,PNG,JPG,DIB,TIFF,EMF,PS,PDF,GIF,SVG,SVGZ,BMP","documentInfo":{"Title":"","Author":"","Comments":"","Subject":"","Category":"","AntialiasingMode":"None","TextAntialiasingMode":"Force","Keywords":""},"capabilities":"Map,Query,Data","supportedQueryFormats":"JSON, AMF, geoJSON","exportTilesAllowed":false,"maxRecordCount":1000,"maxImageHeight":4096,"maxImageWidth":4096,"tileServers":"","supportedExtensions":"KmlServer"}'
    return jsonify(json.loads(info))


@tile.route('/JN/JNYX/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jnyx_tile(x, y, z):
    '''
    请求津南影像瓦片数据,
    png图片
    :param x:
    :param y:
    :param z:
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=4103, errmsg='参数错误')
    try:
        dl_tile = YX.objects(x=x, y=y, z=z).first()
        if dl_tile != None:
            image = dl_tile['image']
        # print(image)
            response = make_response(image)
            response.headers['Content-Type'] = 'image/png'
            return response
        else:
            return jsonify(errorno=RET.PARAMERR, errmsg='瓦片参数错误')
    except Exception as e:
        print(e)
        return jsonify(errorno=4001, errmsg='查询数据库错误')


@tile.route('/JN/JNDL/MapServer/tile/<int:z>/<int:x>/<int:y>', methods=['GET'])
def get_jndl_tile(x, y, z):
    '''
    请求津南道路瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = DL.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNDLHDM/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jndlhdm_tile(x, y, z):
    '''
    请求津南道路横断面瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = DLHDM.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNDY/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jndy_tile(x, y, z):
    '''
    请求津南单元瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = DY.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNGKQXZ/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jngkqxz_tile(x, y, z):
    '''
    请求津南管控区现状瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = GKQXZ.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNGX/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jngx_tile(x, y, z):
    '''
    请求津南管管线瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = GX.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNKG/MapServer/tile/<int:z>/<int:x>/<int:y>', methods=['GET'])
def get_jnkg_tile(x, y, z):
    '''
    请求津南控规瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = KG.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNYJGKQ/MapServer/tile/<int:z>/<int:x>/<int:y>', methods=['GET'])
def get_jnyjgkq_tile(x, y, z):
    '''
    请求津南一级管控区瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        dl_tile = YJGKQ.objects(x=x, y=y, z=z).first()
        image = dl_tile['image']
        # print(image)
        response = make_response(image)
        response.headers['Content-Type'] = 'image/png'
        return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNZJ/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jnzj_tile(x, y, z):
    '''
    请求津南镇界瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        zj_tile = ZJ.objects(x=x, y=y, z=z).first()
        if zj_tile == None:
            return jsonify(errorno=RET.PARAMERR, errmsg='瓦片参数错误')
        else:
            image = zj_tile['image']
            response = make_response(image)
            response.headers['Content-Type'] = 'image/png'
            return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')


@tile.route('/JN/JNTB/MapServer/tile/<int:z>/<int:x>/<int:y>/', methods=['GET'])
def get_jntb_tile(x, y, z):
    '''
    请求津南图斑瓦片数据
    png图片
    :param x:
    :param y:
    :param z:level
    :return:
    '''
    if not(x, y, z):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        tb_tile = TB.objects(x=x, y=y, z=z).first()
        if tb_tile == None:
            return jsonify(errorno=RET.PARAMERR, errmsg='瓦片参数错误')
        else:
            image = tb_tile['image']
            response = make_response(image)
            response.headers['Content-Type'] = 'image/png'
            return response
    except Exception as e:
        print(e)
        return jsonify(errorno=RET.DBERR, errmsg='查询数据库错误')