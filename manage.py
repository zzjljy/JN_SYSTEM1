# 项目启动文件
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from JN_PL_system import create_app, db


app = create_app('develop')

Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    # print(app.url_map)
    manager.run()
