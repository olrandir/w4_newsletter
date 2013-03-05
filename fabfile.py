from __future__ import with_statement
from fabric.api import *

env.use_ssh_config = True
env.hosts = ['ec2'] 
env.forward_agent = True

def t():
	run("ls -la ~")