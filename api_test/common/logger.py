#coding:utf-8
import logging,time
import os

#日志目路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path),'logs')

#--------------日志目录不存在就创建
if not os.path.exists(log_path):
    os.mkdir(log_path)

class Log():
    def __init__(self):
        #文件命名
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%y.%m.%d'))
        self.logger = logging.getLogger() #初始化
        self.logger.setLevel(logging.DEBUG)#设置文件等级

        #定义handler的输出格式（formatter）
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self,level,message):
        #本地FileHandler (继承自StreamHandler。将日志信息输出到磁盘文件上)
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)#给logger添加handler

        #StreamHandler,控制台输出
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter) #给handler添加formatter
        self.logger.addHandler(ch)#给logger添加handler

        if level == 'info': #重要信息
            self.logger.info(message)
        elif level == 'debug': #debug级输出
            self.logger.debug(message)
        elif level == 'warning': #warning级输出，与warn相同，警告信息
            self.logger.warning(message)
        elif level == 'error': #error级输出，错误信息
            self.logger.error(message)
        self.logger.removeHandler(ch)#移除一些日志处理器（所有日志展示单条）
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
            self.__console('debug', message)

    def info(self, message):
            self.__console('info', message)

    def warning(self, message):
            self.__console('warning', message)

    def error(self, message):
            self.__console('error', message)

if __name__ == "__main__":
    log = Log()
    log.info("---测试开始----")
    log.info("操作步骤1,2,3")
    log.warning("----测试结束----")