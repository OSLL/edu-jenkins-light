from jenkins import Jenkins
from pprint import pprint
import configparser
import os
import logging
import tempfile


def print_status_project():
    config = configparser.ConfigParser()
    config.read('confg.cfg')

    settings = config['jenkins_server']

    server = Jenkins(
        settings['server_protocol'] + settings['server_ipaddress'] + ':' + settings['server_port'],
        settings['username'],
        settings['password']
        )
    project_info = server.job_info(settings['project_name'])
    pprint(project_info['healthReport'])

if __name__ == '__main__':
    logging.basicConfig(
        filename=tempfile.gettempdir() + '/python-jenkins-0.2.log',
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S'
    )
    logging.info('python-jenkins-0.2 start')

    try:
        print_status_project()
    except Exception as inst:
        logging.info(str(type(inst)) + ' ' + str(inst.args))
