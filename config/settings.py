########
HANDLER_TYPE_DICT={
    "agent":"src.engine.agent.AgentHandler",
    "salt":"src.engine.salt.SaltHandler",
    "ssh":"src.engine.ssh.SSHHandler",
}
HANDLER_TYPE="agent"

#########
SERVER_INFO_DICT={
    "basic":"src.plugins.basic.Basic",
    "cpu":"src.plugins.cpu.Cpu",
    "disk":"src.plugins.disk.Disk",
    "mem":"src.plugins.memory.Mem",
    "net":"src.plugins.network.Net",
    "board":"src.plugins.broad.MainBoard"
}

##############
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

#######
ASSET_API = "http://127.0.0.1:8000/server/"

###########
LOG_FILE_PATH = os.path.join(BASEDIR,'log','dev.log')
###########

CERT_FILE_PATH =os.path.join(BASEDIR,'config','cert')

############
URL_AUTH_KEY="helloworld"

PUB_KEY = b'LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tCk1JR0pBb0dCQUtDTkVnRSswSlNXdzZ4RlI3eGRoZDZ2cXprUDFyTnFYQzlDVUpjSlRuMzZkNnBoWVYwTkVOK2UKdjE3N0ZRMlhVdml1WFVkc3Z0ajR1djlDNXp4ZEh5R2F5V0JmdUsvRTdDT2d5TUFLeE9vRi9waVRJazRvT1NiNwpqdFN3djhKb2xpaW03alZNNC9XQURDOFBDMjh4U2pNVnpaMG9FcHJubnJOTEthV0lZYnI5QWdNQkFBRT0KLS0tLS1FTkQgUlNBIFBVQkxJQyBLRVktLS0tLQo='


