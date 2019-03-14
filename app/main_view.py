from flask import Flask
from app.utils.mongodb_connections import MongoConnection
from app.utils.logger import get_logger
from app.utils.constants import SYSTEM_PORT
from app.views.user_view import user_views
from app.views.task_view import task_views
from app.views.image_view import image_views
from app.views.remark_views import remark_views

main_app = Flask(__name__)
main_app.register_blueprint(user_views)  # 注册蓝图
main_app.register_blueprint(task_views)
main_app.register_blueprint(image_views)
main_app.register_blueprint(remark_views)
log = get_logger()

if __name__ == "__main__":
    log.info("系统启动")
    connection = MongoConnection.init_connections()  # mongo数据库连接
    main_app.run(host='0.0.0.0', port=SYSTEM_PORT)
