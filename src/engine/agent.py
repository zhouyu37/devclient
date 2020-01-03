from .Base import BaseClass
from config  import settings
from src.plugins import get_server_info
import requests
import os
import json
import time

from lib.auth import gen_sign
from lib.security import encrypt

class AgentHandler(BaseClass):
    def cmd(self,hostname,command):
        import subprocess
        return subprocess.check_output(command)
    def handler(self):
        info=get_server_info(self)
        print(info["mem"])
        if  not os.path.exists(settings.CERT_FILE_PATH):
            info['type'] = 'create'
        else:
            with open(settings.CERT_FILE_PATH,'r') as f:
                cert = f.read()
                if  cert == info['basic']['data']['hostname']:
                    info['type'] = 'update'
                else:
                    info['cert'] = cert
                    info['type'] = 'host_update'
        ctime = int(time.time() * 1000)
        r1 = requests.post(
            url=self.asset_api,
            params={"sign":gen_sign(ctime),"ctime":ctime},
            data=encrypt(json.dumps(info).encode("utf-8")),
            headers={
                'Content-Type': 'application/json'
            }
        )
        response = r1.json()
        print("text",response['data'])
        if response['status']:
            with open(settings.CERT_FILE_PATH, 'w') as f:
                f.write(response['data'])

