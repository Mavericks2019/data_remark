from app.utils.logger import get_logger
from app.mongodb_database.mongodb_manager import MongodbManager
log = get_logger()


class UserManager:

    @staticmethod
    def user_regester(data):
        current_user = data["user_name"]
        echo_user = MongodbManager.get_current_user(current_user)
        if len(echo_user) > 0:
            log.error(f"{UserManager.__name__}:{UserManager.user_regester.__name__},用户{current_user}已经存在")
            raise Exception("用户名已存在")
        MongodbManager.save_user_to_db(data)
        log.info(f"{UserManager.__name__}:{UserManager.user_regester.__name__},用户:{current_user} 注册成功")

    @staticmethod
    def user_login(data):
        user_type = MongodbManager.user_login(data)
        current_user = data["user_name"]
        log.info(f"{UserManager.__name__}:{UserManager.user_login.__name__},用户{current_user}登录成功, 类型为{user_type}")
        return user_type
