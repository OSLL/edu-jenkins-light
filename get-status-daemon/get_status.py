import configparser
import os
import logging
from jenkins import Jenkins

import sys
sys.path.append('../')
from config import JENKINS_SERVER_CONFIG_FILE as configPath


def get_config():
    config = configparser.ConfigParser()

    if not os.path.exists(configPath):
        logging.info('File %s does not exist.' % configPath)
        return None

    config.read(configPath)

    if not (config.has_section('jenkins_server') and
            config.has_option('jenkins_server', 'server_protocol') and
            config.has_option('jenkins_server', 'server_ipaddress') and
            config.has_option('jenkins_server', 'server_port') and
            config.has_option('jenkins_server', 'project_name')):
        logging.info('Is not define one ore more jenkins settings in %s.' % configPath)
        return None

    return config['jenkins_server']


def get_project(server_url, project_name, username, password):
    server = Jenkins(server_url, username, password)

    if not server.job_exists(project_name):
        logging.info('Project %s does not exist.' % project_name)
        return None

    return server.job_info(project_name)


def get_status():
    settings = get_config()

    if settings is None:
        return None

    server_url = settings['server_protocol'] + settings['server_ipaddress'] + ':' + settings['server_port']
    project_name = settings['project_name']
    username = None
    password = None

    if (settings.__contains__('username') and
            settings.__contains__('password')):
        username = settings['username']
        password = settings['password']

    project = get_project(
        server_url,
        project_name,
        username,
        password
        )

    if project is None:
        return None

    return project['healthReport']

if __name__ == '__main__':
    get_status()
