from flask import Blueprint, request
from app.utils.common_tools import img_describer
from app.utils.logger import get_logger
from app.controller.image_manager import ImageManager


image_views = Blueprint("images_views", __name__)
log = get_logger()


@image_views.route("/get_img_by_task", methods=["POST"])
@img_describer
def get_images_by_task():
    data = request.json
    log.info(f"{get_images_by_task.__name__}尝试获取{data}任务的图片")
    return ImageManager.get_images(data)


@image_views.route("/api/download/<img_name>", methods=["GET", "POST"])
def download_images(img_name):
    response = ImageManager.download_images(img_name)
    return response
