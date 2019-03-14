import os
import random
import datetime
import shutil
from app.mongodb_database.mongodb_connector import Task, mongodb_connection
connection = mongodb_connection

path = os.path.abspath("D://test")
img_path = os.path.join(path, "1.jpg")

for i in range(10):
    task_name = f"test{i}"
    # 创建任务名文件夹
    task_dir = os.path.join(path, task_name)
    os.makedirs(task_dir)
    task_type = random.sample(["1", "2", "3"], 1)[0]
    task_assigned_date = "2019-03-14"
    task_image_number = 100
    task_resigned_count = 0
    task_status = "new"
    user_name = ""
    task_available_count_by_type = 100
    task_created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S")
    img_data = ["{a}".format(a=os.path.join(task_dir, f"{i}.jpg"))for i in range(task_image_number)]
    # 复制图片
    [shutil.copyfile(img_path, item) for item in img_data]
    assessor_name = ""
    t = Task(task_name=task_name, task_type=task_type, task_assigned_date=task_assigned_date,
            task_image_number=task_image_number, task_resigned_count=task_resigned_count, task_status=task_status,
             user_name=user_name, task_available_count_by_type=task_available_count_by_type,
             task_created_date=task_created_date, img_data=img_data, assessor_name=assessor_name)
    t.save()
