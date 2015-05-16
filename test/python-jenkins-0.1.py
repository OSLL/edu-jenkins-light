from jenkins import Jenkins
from pprint import pprint
import configparser
import os
import tempfile

config = configparser.ConfigParser()
config.read('config.cfg')

settings = config['jenkins_server']

server = Jenkins(
    settings['server_protocol'] + settings['server_ipaddress'] + ':' + settings['server_port'],
    settings['username'],
    settings['password']
    )
project_info = server.job_info(settings['project_name'])
pprint(project_info['healthReport'])
