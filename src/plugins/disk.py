from .BasePlugin import BasePluginClass
class Disk(BasePluginClass):
    def win(self, handler, hostname):
        print "win disk"
    def linux(self,handler,hostname):
        return "linux disk1"

