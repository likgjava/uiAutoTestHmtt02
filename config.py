import logging.handlers
import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 初始化日志配置
def init_log_config():
    # 创建日志器对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建处理器对象
    sh = logging.StreamHandler()
    log_file = BASE_DIR + "/log/hmtt.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_file, when="midnight",
                                                   interval=1, backupCount=7, encoding="UTF-8")

    # 创建格式化器对象
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    # 把格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把处理器中添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)
