from jenkins import Jenkins
from xmltodict import parse
from pprint import pprint


settings_file = 'settings.xml'


with (open(settings_file, 'r')) as file:
    settings_data = file.read()

settings = parse(settings_data)['jenkins_server']

server = Jenkins(
    settings['server_protocol'] + settings['server_ipaddress'] + ':' + settings['server_port'], 
    settings['username'], 
    settings['password']
    )
project_info = server.job_info(settings['project_name'])
pprint(project_info['healthReport'])
