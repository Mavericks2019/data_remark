import datetime
from app.mongodb_database.mongodb_connector import User, Task, LabelResult
from app.utils.logger import get_logger
from app.utils.constants import TaskStatu

log = get_logger()


class MongodbManager:
    @staticmethod
    def get_current_user(user_name):  # 根据用户名返回该用户所有信息
        try:
            echo_user = User.objects(user_name=user_name)
            return echo_user
        except Exception as e:
            log.error(
                f"{MongodbManager.__name__}:{MongodbManager.get_current_user.__name__},"
                f"从mongodb获取用户名出错，将返回空的用户名, 错误信息:{e}")
            return []

    @staticmethod
    def save_user_to_db(user_info_dict):  # 将用户信息存入数据库
        try:
            u = User(user_info_dict["user_name"], user_info_dict["password"], user_info_dict["full_name"],
                     user_info_dict["email"], user_info_dict["team"], user_info_dict["identity_number"],
                     user_info_dict["phone"], user_info_dict["bank_name"], user_info_dict["bank_card_number"],
                     user_info_dict["bank_location"], user_type=0)
            u.save()
        except Exception as e:
            f"{MongodbManager.__name__}:{MongodbManager.get_current_user.__name__},"
            f"将用户存入数据库时发生错误, 错误信息:{e}"

    @staticmethod
    def user_login(data):  # 比较密码是否与传入的用户名一致，进行登录
        current_user = data["user_name"]
        echo_user = User.objects(user_name=data["user_name"])
        if len(echo_user) == 0:
            log.error(f"{MongodbManager.__name__}:{MongodbManager.user_login.__name__},用户:{current_user}不存在")
            raise Exception("用户名不存在")
        elif echo_user[0].password != data["password"]:
            log.error(f"{MongodbManager.__name__}:{MongodbManager.user_login.__name__},用户{current_user}密码错误")
            raise Exception("用户名或密码错误")
        else:
            log.info("用户:{}登录成功".format(data["user_name"]))
            return echo_user[0].user_type

    @staticmethod
    def get_task_to_label(user):  # 获取所有未被领取的任务

        try:
            task_list = Task.objects(task_status="new")
            log.info(f"{MongodbManager.__name__}:{MongodbManager.get_task_to_label.__name__},"
                     f"{user}成功获取未领取任务列表,共{len(task_list)}个任务")
            return task_list
        except Exception as e:
            log.error(f"{MongodbManager.__name__}:{MongodbManager.get_task_to_label.__name__},"
                      f"{user}在获取未领取任务时出错,错误信息:{str(e)}")
            raise Exception(f"{user}在读取任务时出错,错误信息:{str(e)}")

    @staticmethod
    def get_labled_tasks(user):  # 获取所有已被该用户被领取的任务
        try:
            task_list = Task.objects(user_name=user)
            log.info(f"{MongodbManager.__name__}:{MongodbManager.get_labled_tasks.__name__},"
                     f"{user}成功获取未领取任务列表,共{len(task_list)}个任务")
            return task_list
        except Exception as e:
            log.error(f"{MongodbManager.__name__}:{MongodbManager.get_labled_tasks.__name__},"
                      f"{user}在获取已领取任务时出错,错误信息:{str(e)}")
            raise Exception(f"{user}在读取任务时出错,错误信息:{str(e)}")

    @staticmethod
    def get_image_list_by_task(task):
        try:
            task_list = Task.objects(task_name=task)
            if len(task_list) == 0:
                log.error(f"{MongodbManager.__name__}:{MongodbManager.get_image_list_by_task.__name__},"
                          f"任务名{task}出错数据库中没有该任务")
                raise Exception(f"任务名{task}出错数据库中没有该任务")
            else:
                return task_list
        except Exception as e:
            log.error(f"获取图片数据时出错,错误信息:{str(e)}")
            raise Exception(f"获取图片数据时出错,错误信息:{str(e)}")

    @staticmethod
    def save_remark_result_to_db(data):
        """
        :param data:{"user_name":"" ,
                     "task_name":"" ,
                     "image_url":"" ,
                     "object_list":[],
                     "point_list":[],
                     "pulgin_list":[].
                     "attribute_list":[]}
        :return:
        """
        result_task_image_list = LabelResult.objects(task_name=data["task_name"], image_url=data["image_url"])
        if len(result_task_image_list) == 0:
            if data.get("attribute_list"):
                remark_result = LabelResult(task_name=data["task_name"], task_type=data["task_type"],
                                            user_name=data["user_name"], image_url=data["image_url"],
                                            points_list=data["points_list"], object_list=data["object_list"],
                                            pulgin_list=data["pulgin_list"], attribute_list=data["attribute_list"])
                log.info(f"{MongodbManager.__name__}:{MongodbManager.save_remark_result_to_db.__name__},"
                         f"获取数据成功尝试将数据存入数据库")
                remark_result.save()
            if not data.get("attribute_list"):
                remark_result = LabelResult(task_name=data["task_name"], task_type=data["task_type"],
                                            user_name=data["user_name"], image_url=data["image_url"],
                                            points_list=data["points_list"], object_list=data["object_list"],
                                            pulgin_list=data["pulgin_list"])
                log.info(f"{MongodbManager.__name__}:{MongodbManager.save_remark_result_to_db.__name__},"
                         f"获取数据成功尝试将数据存入数据库")
                remark_result.save()
        else:
            current_result = result_task_image_list[0]
            current_result.points_list = data["points_list"]
            current_result.object_list = data["object_list"]
            current_result.pulgin_list = data["pulgin_list"]
            current_result.attribute_list = data["attribute_list"]
            current_result.save()
        MongodbManager.update_task_date(data["task_name"])

    @staticmethod
    def get_remark_result_by_task(data):
        """

        :param data: {"task_name":"xxx", "image_name":"1.jpg"}
        :return:
        """
        result_list = LabelResult.objects(task_name=data["task_name"], image_url=data["image_name"])
        if len(result_list) > 1:
            log.error(f"{MongodbManager.__name__}:{MongodbManager.get_remark_result_by_task.__name__},"
                      f"同一任务有重名文件，请检查数据库")
            raise Exception("同一任务有重名文件，请检查数据库")
        else:
            return result_list[0]

    @staticmethod
    def gain_tasks(user, task):  # 校验并更新数据库中的数据
        task_user_list = Task.objects(task_name=task)
        user_task_list = Task.objects(user_name=user)
        current_task = task_user_list[0]
        user_task_type_list = [item["task_type"] for item in user_task_list]
        if MongodbManager.check_user(current_task, user_task_type_list, current_task["task_type"]):
            current_task.user_name = user
            current_task.task_status = TaskStatu.in_progress
            current_task.task_assigned_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S")
            current_task.save()
        log.info(f"{MongodbManager.__name__}:{MongodbManager.gain_tasks.__name__}领取任务成功")

    @staticmethod
    def check_user(task_object, user_task_type_list, task_type):
        if task_object.user_name:
            log.error(f"{MongodbManager.__name__}:{MongodbManager.check_user.__name__}出错，该任务已被领取,")
            raise Exception("该任务已被领取")
        elif task_type in user_task_type_list:
            log.error(f"{MongodbManager.__name__}:{MongodbManager.check_user.__name__}出错，已领取该类型任务")
            raise Exception(f"已领取类型为{task_type}的任务")
        else:
            return True

    @staticmethod
    def get_history_task_by_month(user, current_month):
        try:
            task_list_by_user = Task.objects(user_name=user)
            task_list = MongodbManager.get_task_of_current_month(task_list_by_user, current_month)
            return task_list
        except Exception as e:
            log.error(f"{MongodbManager.__name__}:{MongodbManager.get_history_task_by_month.__name__},"
                      f"用户{user}获取{current_month}月的任务出错，错误信息{str(e)}")
            raise Exception(str(e))

    @staticmethod
    def get_task_of_current_month(task_list, current_month):
        return list(filter(lambda x: x["task_assigned_date"].split("-")[1] == current_month, task_list))

    @staticmethod
    def give_up_task(user, task):  # todo 加入任务状态校验，不能放弃审核中的任务
        current_task = Task.objects(task_name=task)[0]
        if current_task["user_name"] != user:
            raise Exception(f"{task}任务不属于{user},请检查数据库")
        else:
            current_task.user_name = ""
            current_task.task_status = "new"
            current_task.task_assigned_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            current_task.save()
            MongodbManager.clear_label_result(task, user)

    @staticmethod
    def clear_label_result(task, user):
        try:
            label_result = LabelResult.objects(task_name=task, user_name=user)
            label_result.delete()
        except Exception as e:
            log.error(f"{MongodbManager.__name__}:{MongodbManager.clear_label_result.__name__}"
                      f",清除标注结果出错，错误信息{str(e)}")
            raise Exception(f",清除标注结果出错，错误信息{str(e)}")

    @staticmethod
    def get_task_check_pending():
        try:
            # task_list = Task.objects(Q(task_status=TaskStatu.in_review) | Q(task_status=TaskStatu.very_fine) | Q(
            #     task_status=TaskStatu.roll_back))
            task_list = Task.objects(task_status=TaskStatu.complete)
            return task_list
        except Exception as e:
            log.error(f"{MongodbManager.__name__}:{MongodbManager.get_task_check_pending.__name__}"
                      f",审核员获取数据出错，错误信息{str(e)}")
            raise Exception(f",清除标注结果出错，错误信息{str(e)}")

    @staticmethod
    def update_task_date(task_name):
        task = Task.objects(task_name=task_name)[0]
        task.task_assigned_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task.save()

    @staticmethod
    def submit_property_result(user_name, task_name, task_statu):
        task = Task.objects(task_name=task_name)[0]
        current_user_type = User.objects(user_name=user_name)[0]["user_type"]
        task.task_status = task_statu
        task.assessor_name = user_name if current_user_type == 1 else ""
        MongodbManager.update_task_date(task_name)
        task.save()
