from flask import Blueprint, current_app, make_response, render_template
from .mongo_insert import yjgkq_insert_new, kg_insert_new, yx_insert_new

html = Blueprint('html', __name__)


# @html.route("/<regex('.*'):file_name>")
# def html_file(file_name):
#     """
#     前端请求许返回静态页面
#     默认页面
#     :param file_name:
#     :return:
#     """
#     if not file_name:
#         file_name = 'index.html'
#
#     response = make_response(current_app.send_static_file(file_name))
#     return response


@html.route('/')
def index():
    # tb_insert()
    # kg_insert_new()
    # yx_insert_new()
    # yjgkq_insert_new()
    return render_template('index.html')




