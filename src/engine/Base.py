from config import settings
class BaseClass(object):
    def __init__(self):
        self.asset_api = settings.ASSET_API

    def cmd(self,command, hostname=None):
        raise NotImplementedError('cmd must be implemented')

    def handler(self):
        raise NotImplementedError("handler method must be existed ")