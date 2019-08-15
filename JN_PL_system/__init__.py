import logging
from flask import Flask
from config import Config, configs
from logging.handlers import RotatingFileHandler
from JN_PL_system.utils.commons import RegexConverter
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_compress import Compress

app = Flask(__name__)
CORS(app, resources=r'/*')
Compress(app)
app.config['MONGODB_SETTINGS'] = {
    'host': Config.MONGODB_HOST,
    'port': Config.MONGODB_PORT,
    'db': Config.MONGODB_DB
}
db = MongoEngine(app)


def setup_logging(level):
    logging.basicConfig(level=level)
    # 创建日志记录器，指明日志保存的路径，每个日志文件的最大大小，保存的日志文件个数上线
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式    日志等级  输入日志信息的文件名  行数  日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚刚创建的日志及录取设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    """创建flask应用app对象"""
    setup_logging(configs[config_name].LOGGING_LEVEL)

    # db = MongoEngine(app)

    # 从配置对象中为APP设置配置信息
    app.config.from_object(configs[config_name])

    # 数据库处理
    # db.init_app(app)

    # 为app中的url路由添加正则表达式匹配
    app.url_map.converters['regex'] = RegexConverter

    # 为app添加api蓝图应用
    from .JN_api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/jn_api/v1.0')

    # 控规
    from .JN_api_1_0.kg import kg
    app.register_blueprint(kg, url_prefix='/jn_api/v1.0')

    # 道路
    from .JN_api_1_0.dl import dl
    app.register_blueprint(dl, url_prefix='/jn_api/v1.0')

    # 一级管控区
    from .JN_api_1_0.yjgkq import gkq
    app.register_blueprint(gkq, url_prefix='/jn_api/v1.0')

    # 管线
    from .JN_api_1_0.gx import gx
    app.register_blueprint(gx, url_prefix='/jn_api/v1.0')

    # 为app添加返回静态html的蓝图应用
    from .index_page import html as html_blueprint
    app.register_blueprint(html_blueprint)

    # tile瓦片
    from .JN_api_1_0.tile import tile
    app.register_blueprint(tile, url_prefix='/jn_api/v1.0')

    # 单元
    from .JN_api_1_0.dy import dy
    app.register_blueprint(dy, url_prefix='/jn_api/v1.0')

    # 图斑
    from .JN_api_1_0.tb import tb
    app.register_blueprint(tb, url_prefix='/jn_api/v1.0')

    # 镇界
    from .JN_api_1_0.zj import zj
    app.register_blueprint(zj, url_prefix='/jn_api/v1.0')

    # 修详规
    from .JN_api_1_0.xxg import xxg
    app.register_blueprint(xxg, url_prefix='/jn_api/v1.0')
    return app
