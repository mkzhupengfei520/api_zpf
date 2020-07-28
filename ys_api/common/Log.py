import logging
from datetime import datetime
import threading
import os
from ys_api import readConfig


class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")
        # 创建结果文件，如果它不存在
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # 由localtime定义的测试结果文件名
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # 如果测试结果文件不存在，则创建它
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # 定义日志记录器
        self.logger = logging.getLogger()
        #定义日志级别
        self.logger.setLevel(logging.INFO)

        # 定义处理程序
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # 定义的格式化程序
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 定义的格式化程序
        handler.setFormatter(formatter)
        # 添加处理程序
        self.logger.addHandler(handler)
class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log
