import os
import logging
from app.utils.constants import LOG_PATH


def get_logger():
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)

    log = logging.getLogger(__name__)
    log.setLevel(level=logging.INFO)

    handler = logging.FileHandler(os.path.join(LOG_PATH, "data_remark_log.log"), encoding='utf-8')
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log


if __name__ == "__main__":
    logger = get_logger()
    logger.info("11")
