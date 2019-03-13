import os
import platform


class TableNames:  # 表名
    user = "user"
    data_remark = "data_remark"


MONGO_IP = "192.168.5.93"  # mongodb 所在IP
MONGO_PORT = 27017  # mongodb 所在port

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")

SYSTEM_PORT = 8086
SYSTEM_IP = "192.168.11.68"

IMAGE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "img")
CURRENT_SYSYEM = platform.platform().split("-")[0]


class TaskStatu:
    new = "new"
    in_progress = "in_progress"
    in_review = "in_review"
    very_fine = "very_fine"
    roll_back = "roll_back"
    complete = "complete"
