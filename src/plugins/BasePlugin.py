from config import settings
class BasePluginClass(object):
    def __init__(self):
        self.debug = settings.DEBUG
        self.base_dir = settings.BASEDIR

    def get_os(self,handler,hostname):
        return "linux"

    def process(self,handler,hostname):
        os=self.get_os(handler,hostname)
        if os == "linux":
            return self.linux(handler,hostname)
        else:
            return self.win(handler,hostname)

    def win(self,handler,hostname):
        raise NotImplementedError("run method must be existed ")

    def linux(self,handler,hostname):
        raise NotImplementedError("run method must be existed ")