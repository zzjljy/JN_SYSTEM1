# 项目启动文件
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from JN_PL_system import create_app, db
import os

app = create_app('develop')
if __name__ == '__main__':
    Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    app.run(host='0.0.0.0')


# if __name__ == '__main__':
    # print(app.url_map)
    # manager.run()
    # app.run(host='0.0.0.0')
