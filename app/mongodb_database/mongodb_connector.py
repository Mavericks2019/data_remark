from mongoengine import StringField, IntField, ListField, connect
from mongoengine.document import Document

mongodb_connection = connect("data_remark", host="192.168.5.93", port=27017)


class User(Document):  # user库
    user_name = StringField(unique=True)
    password = StringField()
    full_name = StringField()
    email = StringField()
    team = StringField()
    identity_number = StringField()
    phone = StringField()
    bank_name = StringField()
    bank_card_number = StringField()
    bank_location = StringField()
    user_type = IntField()


class Task(Document):  # task库
    task_name = StringField(unique=True)  # 任务名
    task_type = StringField()  # 任务类型，point68或point39等
    task_assigned_date = StringField()
    task_image_number = IntField()
    task_resigned_count = IntField()  # 打回次数
    task_status = StringField()  # New(新);in progress(正在标注)(被打回);complete;in_review(正在审核);very_fine(完成)
    user_name = StringField()  # 获取当前任务的用户名
    task_available_count_by_type = IntField()  # 任务剩余量
    task_created_date = StringField()
    img_data = ListField()  # 图片文件名组成的数组
    assessor_name = StringField()  # 审核员名字


class LabelResult(Document):  # 标注结果库
    task_name = StringField()
    task_type = StringField()
    user_name = StringField()
    image_url = StringField()
    points_list = ListField()  # 标注像素点位信息
    object_list = ListField()  # 方框信息
    pulgin_list = ListField()  # 特殊形状信息
    attribute_list = ListField()  # 标签列表


if __name__ == "__main__":
    t = Task(task_name="test10", user_name="jiannan.shi", task_labeld="to_label", task_type="test",
             task_assigned_date="2019-03-04", task_image_number=10, task_resigned_count=5, task_status=1,
             img_data=["1", "2", "3"], task_created_date="2019-03-04", task_available_count_by_type=2)
    t.save()
    task_list = Task.objects(task_name="test")
