import logging


class Logger(object):
    def __init__(self):
        file_handler = logging.FileHandler("log.log",'a',encoding='utf-8')
        file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s-%(name)s-%(levelname)s-%(module)s: %(message)s"))

        self.logger=logging.Logger('root',level=logging.INFO)
        self.logger.addHandler(file_handler)

    def info(self,msg):
        self.logger.info(msg)
    def error(self,msg):
        self.logger.error(msg)

logger=Logger()
logger.info("1222")
logger.error("1222")