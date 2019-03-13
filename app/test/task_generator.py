import random
import os
from app.mongodb_database.mongodb_connector import Task, mongodb_connection

connection = mongodb_connection
current_path = os.path.abspath(os.path.dirname(__file__))
img_path = os.path.join(os.path.dirname(os.path.dirname(current_path)), "img")
img_url = os.path.join(img_path, "1.jpg")

task_name_count = 100
task_name_list = [f"test{i}" for i in range(task_name_count)]
user_name = "jiannan.shi"
task_type = "test"
task_assigned_date = "2019-03-05"
task_image_number = 100
task_resigned_count = 5
task_status = [item[0] for item in
               [random.sample(["new", "in_progress", "complete", "in_review", "very_fine"], 1) for _ in
                range(task_name_count)]]
task_available_count_by_type = 100
task_created_date = "2019-03-05"
img_data = [img_url]
task_labeld = [item[0] for item in [random.sample(["to_label", "labeld"], 1) for _ in range(task_name_count)]]

for i in range(20):
    t = Task(task_name=task_name_list[i], user_name=user_name, task_type=task_type,
             task_assigned_date=task_assigned_date, task_image_number=task_image_number,
             task_resigned_count=task_resigned_count, task_status=task_status[i], img_data=img_data,
             task_created_date=task_created_date, task_available_count_by_type=task_available_count_by_type)
    t.save()
