import logging, os


class Config(object):
    """应用程序配置类"""
    # 开启调试模式
    DEBUG = True

    # logging等级
    LOGGING_LEVEL = logging.DEBUG

    # 配置flask-sqlalchemy使用的参数
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456@127.0.0.1/my_first_postgis'
    # 追踪数据库的修改行为，如果不设置会报警告，不影响代码的执行
    SQLALCHEMY_TRACK_MODIFICATIONS = True
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


class UnitTestConfig(Config):
    """单元测试配置"""
    LOGGIONG_LEVEL = logging.DEBUG
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/ehome_test'


class ProductionConfig(Config):
    """生产环境下的配置类"""
    LOGGIONG_LEVEL = logging.WARNING
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456@127.0.0.1/my_first_postgis'
    # 配置postgresql数据库
    POSTGRES_PORT = '5432'
    POSTGRES_HOST = 'localhost'
    POSTGRES_DB = 'JN_SYSTEM'
    POSTGRES_USER = 'postgres'
    POSTGRES_PASSWORD = '123456'
    # Mongo配置
    MONGODB_PORT = 27017
    MONGODB_HOST = "192.168.18.9"
    MONGODB_DB = "JN_SYSTEM"


class DockerConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)
        # 将日志输出到stder
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.info)
        app.logger.addHandler(file_handler)


configs = {
    'default': Config,
    'develop': DevelopConfig,
    'unittest': UnitTestConfig,
    'production': ProductionConfig,
    'docker': DockerConfig,
}

if __name__ == '__main__':
    print(os.path.dirname(os.path.abspath(__file__)))
