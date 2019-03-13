from flask import make_response, send_from_directory
from functools import reduce
from app.utils.logger import get_logger
from app.utils.constants import CURRENT_SYSYEM
from app.mongodb_database.mongodb_manager import MongodbManager


log = get_logger()


class ImageManager:
    @staticmethod
    def get_images(data):
        task_name = data["task_name"]
        task_list = MongodbManager.get_image_list_by_task(task_name)
        return task_list[0]["img_data"]

    @staticmethod
    def download_images(img_name):
        log.info(f"下载图片:{img_name}")

        if CURRENT_SYSYEM == "Windows":
            path_list = img_name.split("\\")
            image_name = path_list.pop()
            image_path = reduce(lambda x, y: x + y, [item+"\\" for item in path_list])

        elif CURRENT_SYSYEM == "Linux":
            path_list = img_name.split("/")
            image_name = path_list.pop()
            image_path = reduce(lambda x, y: x + y, [item+"/" for item in path_list])
        else:
            raise Exception("unknown system")
        response = make_response(send_from_directory(image_path, image_name, as_attachment=True))
        response.headers["Content-Disposition"] = f"attachment; filename={img_name}"
        return response
