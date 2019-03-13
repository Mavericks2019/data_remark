from mongoengine import connect
from app.utils.constants import TableNames, MONGO_IP, MONGO_PORT


class MongoConnection:
    @staticmethod
    def init_connections():  # 初始化mongo数据库连接
        connect(TableNames.data_remark, host=MONGO_IP, port=MONGO_PORT)
