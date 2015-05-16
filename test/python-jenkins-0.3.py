from jenkins import Jenkins
from pprint import pprint
import configparser
import os
import logging
import tempfile

NAME = 'python-jenkins-0.3.py'


def print_status_project():
    config = configparser.ConfigParser()
    configPath = os.path.dirname(os.path.realpath('__file__')) + '/config.cfg'

    if not os.path.exists(configPath):
        logging.info('File "config.cfg" does not exist. %s stopped.' % NAME)
        return

    config.read(configPath)

    if not (config.has_section('jenkins_server') and
            config.has_option('jenkins_server', 'server_protocol') and
            config.has_option('jenkins_server', 'server_ipaddress') and
            config.has_option('jenkins_server', 'server_port') and
            config.has_option('jenkins_server', 'project_name')):
        logging.info('Is not define one ore more jenkins settings in "config.cfg". %s stopped.' % NAME)
        return

    settings = config['jenkins_server']

    if not config.has_option('jenkins_server', 'username'):
        settings['username'] = 'None'

    if not config.has_option('jenkins_server', 'password'):
        settings['username'] = 'None'

    server = Jenkins(
        settings['server_protocol'] + settings['server_ipaddress'] + ':' + settings['server_port'],
        settings['username'],
        settings['password']
        )

    if not server.job_exists(settings['project_name']):
        logging.info('Project %s does not exist. %s stopped.' % (settings['project_name'], NAME))
        return

    project_info = server.job_info(settings['project_name'])
    pprint(project_info['healthReport'])


def main():
    logging.basicConfig(
        filename=tempfile.gettempdir() + '/python-jenkins-0.3.log',
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S'
    )
    logging.info('python-jenkins-0.3 start')

    try:
        print_status_project()
    except Exception as inst:
        logging.info(str(type(inst)) + ' ' + str(inst.args))


if __name__ == '__main__':
    main()
