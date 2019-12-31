from .Base import BaseClass
from src.plugins import get_server_info
class AgentHandler(BaseClass):
    def cmd(self,hostname,command):
        import subprocess
        return subprocess.check_output(command)
    def handler(self):
        info=get_server_info(self)
        print(info)