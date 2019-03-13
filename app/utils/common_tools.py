import json
from functools import wraps
from flask import make_response
from app.utils.logger import get_logger

log = get_logger()


def user_describer(func):  # 装饰器，将返回异常信息封装成{"error_code": 0, "result": "success", "message": "OK"}的形式
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            role = func(*args, **kwargs)
        except Exception as e:
            final_dict = {"error_code": 1, "result": "failed", "message": str(e), "role": 0}
            final_data = json.dumps(final_dict)
        else:
            final_dict = {"error_code": 0, "result": "success", "message": "OK", "role": role}
            log.info(f"用户登录成功，身份是{role}")
            final_data = json.dumps(final_dict)
        response = make_response(final_data)
        response.headers["Content-Type"] = "application/json"
        return response
    return wrapper


def task_describer(func):  # 装饰器，将返回异常信息封装成{"error_code": 0, "result": "success", "message": "OK"}的形式
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # result:
            # {"task_name": "xxx", "task_type": "xxx", "task_available_count_by_type": 20, "task_create_date": "xxxxx"}
            result = func(*args, **kwargs)
        except Exception as e:
            result = []
            final_dict = {"tasks": result, "error_code": 1, "result": "failed", "message": str(e)}
            final_data = json.dumps(final_dict)
        else:
            final_dict = {"tasks": result, "error_code": 0, "result": "success", "message": "OK"}
            final_data = json.dumps(final_dict)
        response = make_response(final_data)
        response.headers["Content-Type"] = "application/json"
        return response
    return wrapper


def img_describer(func):  # 装饰器，将返回异常信息封装成{"error_code": 0, "result": "success", "message": "OK"}的形式
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # result:
            # {"task_name": "xxx", "task_type": "xxx", "task_available_count_by_type": 20, "task_create_date": "xxxxx"}
            result = func(*args, **kwargs)
        except Exception as e:
            result = []
            final_dict = {"img_data": result, "error_code": 1, "result": "failed", "message": str(e)}
            final_data = json.dumps(final_dict)
        else:
            final_dict = {"img_data": result, "error_code": 0, "result": "success", "message": "ok"}
            final_data = json.dumps(final_dict)
        response = make_response(final_data)
        response.headers["Content-Type"] = "application/json"
        return response
    return wrapper


def common_describer(func):  # 装饰器，将返回异常信息封装成{"error_code": 0, "result": "success", "message": "OK"}的形式
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            final_dict = {"error_code": 1, "result": "failed", "message": str(e)}
            final_data = json.dumps(final_dict)
        else:
            final_dict = {"error_code": 0, "result": "success", "message": "ok"}
            final_data = json.dumps(final_dict)
        response = make_response(final_data)
        response.headers["Content-Type"] = "application/json"
        return response
    return wrapper


def user_login_describer(func):  # 装饰器，将返回异常信息封装成{"error_code": 0, "result": "success", "message": "OK"}的形式
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            final_dict = {"error_code": 1, "result": "failed", "message": str(e), "role": 0}
            final_data = json.dumps(final_dict)
        else:
            final_dict = {"error_code": 0, "result": "success", "message": "OK", "role": 0}
            final_data = json.dumps(final_dict)
        response = make_response(final_data)
        response.headers["Content-Type"] = "application/json"
        return response
    return wrapper


def remark_describer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # result:
            # {"task_name": "xxx", "task_type": "xxx", "task_available_count_by_type": 20, "task_create_date": "xxxxx"}
            result = func(*args, **kwargs)
        except Exception as e:
            result = {}
            final_dict = {"remark_data": result, "error_code": 1, "result": "failed", "message": str(e)}
            final_data = json.dumps(final_dict)
        else:
            final_dict = {"remark_data": result, "error_code": 0, "result": "success", "message": "OK"}
            final_data = json.dumps(final_dict)
        response = make_response(final_data)
        response.headers["Content-Type"] = "application/json"
        return response
    return wrapper
