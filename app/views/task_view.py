from flask import Blueprint, request
from app.utils.common_tools import task_describer,common_describer
from app.utils.logger import get_logger
from app.controller.task_manager import TaskManager

task_views = Blueprint("task_views", __name__)
log = get_logger()


@task_views.route("/get_tasks_to_label_by_user", methods=["POST"])
@task_describer
def get_tasks_to_label():  # 获取未领取任务
    data = request.json
    log.info(f"{get_tasks_to_label.__name__}用户:{data}尝试获取已领取任务")
    return TaskManager.get_tasks(data)


@task_views.route("/get_tasks_labeled_by_user", methods=["POST"])
@task_describer
def get_tasks_labeled_by_user():  # 获取用户已领取任务
    data = request.json
    user = data["user_name"]
    log.info(f"{get_tasks_labeled_by_user.__name__}用户:{user}尝试获取未领取任务")
    return TaskManager.get_labled_tasks(data)


@task_views.route("/gain_tasks", methods=["POST"])  # 领取任务接口
@common_describer
def gain_tasks():
    data = request.json
    user = data["user_name"]
    task = data["task_name"]
    log.info(f"{gain_tasks.__name__}用户:{user}尝试领取任务{task}")
    TaskManager.gain_tasks(data)
    return


@task_views.route("/get_history_task_by_month", methods=["POST"])
@task_describer
def get_history_task_by_month():
    data = request.json
    return TaskManager.get_history_task_by_month(data)


@task_views.route("/give_up_task", methods=["POST"])  # 标注员放弃任务
@common_describer
def give_up_task():
    data = request.json
    TaskManager.give_up_task(data)


@task_views.route("/get_task_check_pending", methods=["POST"])
@task_describer
def get_task_check_pending():
    data = request.json
    return TaskManager.get_task_check_pending(data)
