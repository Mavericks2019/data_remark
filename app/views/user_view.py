from flask import Blueprint, request
from app.controller.user_manager import UserManager
from app.utils.common_tools import user_describer, common_describer
from app.utils.logger import get_logger

user_views = Blueprint("user_views", __name__)
log = get_logger()


@user_views.route("/api/login", methods=["POST"])  # 用户登陆
@user_describer
def user_login():
    data = request.json
    log.info(f"{user_login.__name__}用户登录")
    return UserManager.user_login(data)


@user_views.route("/registry", methods=["POST"])  # 用户注册
@common_describer
def user_registry():
    data = request.json
    log.info(f"{user_registry.__name__}, 用户注册, 信息:{data}")
    UserManager.user_regester(data)
