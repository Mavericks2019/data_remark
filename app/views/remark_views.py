from flask import Blueprint, request
from app.utils.common_tools import common_describer,remark_describer
from app.utils.logger import get_logger
from app.controller.remark_manager import RemarkManager


remark_views = Blueprint("remark_views", __name__)
log = get_logger()


@remark_views.route("/property/save", methods=["POST"])  # 保存/刷新任务结果
@common_describer
def save_property_result():
    data = request.json
    RemarkManager.save_remark_result(data)


@remark_views.route("/property/get", methods=["POST"])
@remark_describer
def get_property_result():
    data = request.json
    return RemarkManager.get_remark_result(data)


@remark_views.route("/property/submit", methods=["POST"])
@common_describer
def submit_property_result():
    data = request.json
    RemarkManager.submit_property_result(data)
