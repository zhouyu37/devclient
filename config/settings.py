########
HANDLER_TYPE_DICT={
    "agent":"src.engine.agent.AgentHandler",
    "salt":"src.engine.salt.SaltHandler",
    "ssh":"src.engine.ssh.SSHHandler",
}
HANDLER_TYPE="agent"

#########
SERVER_INFO_DICT={
    "disk":"src.plugins.disk.Disk",
    "mem":"src.plugins.memory.Mem",
    "net":"src.plugins.network.Net"
}

##############
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True


