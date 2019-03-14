from app.utils.logger import get_logger
from app.mongodb_database.mongodb_manager import MongodbManager

log = get_logger()


class RemarkManager:
    @staticmethod
    def save_remark_result(data):
        """
        :param data:{"user_name":"" ,
                     "task_name":"" ,
                     "image_url":"" ,
                     "object_list":[],
                     "point_list":[],
                     "pulgin_list":[].
                     "tag_list":[]}
        :return:
        """

        user_name = data["user_name"]
        log.info(f"{RemarkManager.__name__}:{RemarkManager.save_remark_result.__name__}{user_name}尝试保存标注结果")
        try:
            MongodbManager.save_remark_result_to_db(data)
        except Exception as e:
            log.error(
                f"{RemarkManager.__name__}:{RemarkManager.save_remark_result.__name__}{user_name}"
                f"尝试保存标注结果失败，错误信息{str(e)}")
            raise Exception(f"尝试保存标注结果失败，错误信息{str(e)}")

    @staticmethod
    def get_remark_result(data):
        """
        :param data: {"task_name":"xxx", "image_name":"1.jpg"}
        :return:
        """
        task_name = data["task_name"]
        try:
            log.info(f"{RemarkManager.__name__}:{RemarkManager.get_remark_result.__name__}{task_name}尝试获取标注结果")
            result = MongodbManager.get_remark_result_by_task(data)
            current_task = MongodbManager.get_task_by_task_name(task_name)
            result = result._data
            return {"task_name": data["task_name"],
                    "image_url": data["image_name"],
                    "user_name": current_task["user_name"],
                    "task_type": current_task["task_type"],
                    "points_list":  result["points_list"] if result.get("points_list") else [],
                    "attribute_list": result["attribute_list"] if result.get("attribute_list") else [],
                    "object_list": result["object_list"] if result.get("object_list") else [],
                    "pulgin_list": result["pulgin_list"] if result.get("pulgin_list") else [],
                    }
        except Exception as e:
            log.error(
                f"{RemarkManager.__name__}:{__name__}{task_name}"
                f"尝试获取标注结果失败，错误信息{str(e)}")
            raise Exception(f"尝试获取标注结果失败，错误信息{str(e)}")

    @staticmethod
    def submit_property_result(data):
        user_name = data["user_name"]
        task_name = data["task_name"]
        task_statu = data["task_statu"]
        try:
            MongodbManager.submit_property_result(user_name, task_name, task_statu)
        except Exception as e:
            log.error(f"{__name__}:{RemarkManager.__name__}:{RemarkManager.submit_property_result.__name__}:"
                      f"尝试提交标注结果失败，错误信息{str(e)}")
            raise Exception(f"{str(e)}")
