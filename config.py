import logging, os


class Config(object):
    """应用程序配置类"""
    # 开启调试模式
    DEBUG = True

    # logging等级
    LOGGING_LEVEL = logging.DEBUG

    # 配置flask-sqlalchemy使用的参数
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456@127.0.0.1/my_first_postgis'
    # 追踪数据库的修改行为，如果不设置会报警告，不影响代码的执行
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 显示sql语句
    # SQLALCHEMY_ECHO=True

    # 配置postgresql数据库
    POSTGRES_PORT = '5432'
    POSTGRES_HOST = 'localhost'
    POSTGRES_DB = 'JN_SYSTEM'
    POSTGRES_USER = 'postgres'
    POSTGRES_PASSWORD = '123456'
    # Mongo配置
    MONGODB_PORT = 27017
    MONGODB_HOST = "127.0.0.1"
    MONGODB_DB = "JN_SYSTEM"


class DevelopConfig(Config):
    """开发阶段下的配置"""
    LOGGING_LEVEL = logging.DEBUG


class TestConfig(Config):
    """单元测试配置"""
    LOGGIONG_LEVEL = logging.WARNING
    DEBUG = False
    # 配置postgresql数据库
    POSTGRES_PORT = '5432'
    POSTGRES_HOST = 'localhost'
    POSTGRES_DB = 'JN_SYSTEM'
    POSTGRES_USER = 'postgres'
    POSTGRES_PASSWORD = 'rhch83710086'
    # Mongo配置
    MONGODB_PORT = 27017
    MONGODB_HOST = "localhost"
    MONGODB_DB = "JN_SYSTEM"


class ProductionConfig(Config):
    """生产环境下的配置类"""
    LOGGIONG_LEVEL = logging.WARNING
    DEBUG = False


configs = {
    'default': Config,
    'develop': DevelopConfig,
    'unittest': TestConfig,
    'production': ProductionConfig,
}

if __name__ == '__main__':
    print(os.path.dirname(os.path.abspath(__file__)))
