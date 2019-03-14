import datetime
from app.utils.logger import get_logger
from app.mongodb_database.mongodb_manager import MongodbManager
log = get_logger()


class TaskManager:
    @staticmethod
    def get_tasks(data):  # 根据报文信息获取任务(未领取)
        try:
            user = data["user_name"]
            task_to_lable_list = MongodbManager.get_task_to_label(user)
            return [{"task_name": item["task_name"],
                     "task_type": item["task_type"],
                     "task_available_count_by_type": item["task_available_count_by_type"],
                     "task_create_date": item["task_created_date"]} for item in task_to_lable_list]
        except Exception as e:
            raise Exception(f"{TaskManager.__name__}:{TaskManager.get_tasks.__name__},{str(e)}")

    @staticmethod
    def get_labled_tasks(data):  # 根据报文信息获取任务(已领取)
        try:
            user = data["user_name"]
            task_labled_current_list = MongodbManager.get_labled_tasks(user)
            return [
                {
                    "task_name": item["task_name"],
                    "task_type": item["task_type"],
                    "task_assigned_date": item["task_assigned_date"],
                    "task_image_number": item["task_image_number"],
                    "task_reassigned_count": item["task_resigned_count"],
                    "task_status":1 if item["task_status"] == "very_fine" else 0
                }
                for item in task_labled_current_list
            ]
        except Exception as e:
            raise Exception(f"{TaskManager.__name__}:{TaskManager.get_labled_tasks.__name__},{str(e)}")

    @staticmethod
    def gain_tasks(data):
        user = data["user_name"]
        task = data["task_name"]
        try:
            MongodbManager.gain_tasks(user, task)
        except Exception as e:
            log.error(
                f"{TaskManager.__name__}:{TaskManager.get_labled_tasks.__name__},"
                f"用户{user}从更新{task}任务数据出现问题, 错误信息:{str(e)}")
            raise Exception(str(e))

    @staticmethod
    def get_history_task_by_month(data):
        user = data["user_name"]
        log.info(f"{TaskManager.get_history_task_by_month.__name__}用户:{user}尝试查询当月信息")
        current_month = datetime.datetime.now().strftime("%m")
        return [{
                "id": item.id.__str__(),  # id
                "task_assigned_date": item["task_assigned_date"],  # 最后一次更新时间
                "task_name":item["task_name"],  # 任务名称
                "task_status": item["task_status"]  # 任务状态
                }for item in MongodbManager.get_history_task_by_month(user, current_month)]

    @staticmethod
    def give_up_task(data):
        user = data["user_name"]
        task = data["task_name"]
        log.info(f"{TaskManager.give_up_task.__name__}用户:{user}尝试查询放弃{task}")
        try:
            MongodbManager.give_up_task(user, task)
        except Exception as e:
            log.error(f"{TaskManager.give_up_task.__name__}用户:{user}尝试查询放弃{task},错误信息{str(e)}")
            raise Exception(str(e))

    @staticmethod
    def get_task_check_pending(data):
        user = data["user_name"]
        log.info(f"{TaskManager.get_task_check_pending.__name__}用户:{user}尝试获取所有待审核任务")
        try:
            task_list = MongodbManager.get_task_check_pending()
            return [{
                "user_name": item["user_name"],  # id
                "task_name": item["task_name"],  # 最后一次更新时间
                "task_status":item["task_status"],  # 任务状态
                "task_resigned_count": item["task_resigned_count"],  # 任务打回次数
                "task_created_date": item["task_created_date"]  # 任务创建时间
                }for item in task_list]
        except Exception as e:
            log.error(f"{TaskManager.give_up_task.__name__}用户:{user}尝试查询所有待审核任务失败，错误信息:{str(e)}")
            raise Exception(str(e))

    @staticmethod
    def get_task_type_details(data):
        """
        :param data: {"task_type": "xxx"}
        :return:
        """
        task_type = data["task_type"]
        log.info(f"{__name__}:{TaskManager.__name__}:{TaskManager.get_task_type_details.__name__}获取任务配置")
        try:
            task_config = MongodbManager.get_task_type_details(task_type)
            return {"task_type": task_config["task_type"],
                    "task_label_content": task_config["task_label_content"],
                    "image_attribute": task_config["image_attribute"],
                    "content_attribute": task_config["content_attribute"]}
        except Exception as e:
            log.error(f"{__name__}:{TaskManager.__name__}:{TaskManager.get_task_type_details.__name__}"
                        f"获取任务配置失败，错误信息：{str(e)}")
            raise Exception(f"获取任务配置失败，错误信息：{str(e)}")
