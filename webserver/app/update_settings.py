import sys
import logging
import os
import configparser
from config import JENKINS_SERVER_CONFIG_FILE as configPath


def save_settings(form):
    config = configparser.ConfigParser()
    config.add_section('jenkins_server')

    config.set('jenkins_server', 'server_protocol', form.server_protocol.data)
    config.set('jenkins_server', 'server_ipaddress', form.server_ipaddress.data)
    config.set('jenkins_server', 'server_port', form.server_port.data)
    config.set('jenkins_server', 'project_name', form.project_name.data)
    config.set('jenkins_server', 'username', form.username.data)
    config.set('jenkins_server', 'password', form.password.data)

    with (open(configPath, 'w')) as configFile:
        config.write(configFile)


def load_settings(form):
    config = configparser.ConfigParser()

    if not os.path.exists(configPath):
        logging.info('File %s does not exist.' % configPath)
        return

    config.read(configPath)

    if not (config.has_section('jenkins_server') and
            config.has_option('jenkins_server', 'server_protocol') and
            config.has_option('jenkins_server', 'server_ipaddress') and
            config.has_option('jenkins_server', 'server_port') and
            config.has_option('jenkins_server', 'project_name')):
        logging.info('Is not define one ore more jenkins settings in %s.' % configPath)
        return

    settings = config['jenkins_server']

    form.server_protocol.process_data(settings['server_protocol'])
    form.server_ipaddress.process_data(settings['server_ipaddress'])
    form.server_port.process_data(settings['server_port'])
    form.project_name.process_data(settings['project_name'])
    form.username.process_data('')
    form.password.process_data('')
