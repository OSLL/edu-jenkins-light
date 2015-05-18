import os
import tempfile


WTF_CSRF_ENABLED = True
SECRET_KEY = 'my_secret_key'

WEBSERVER_ADDRESS = '0.0.0.0'
WEBSERVER_PORT = 5000
WEBSERVER_DEBUG_STATUS = True

PID_DIR = tempfile.gettempdir()
LOG_DIR = tempfile.gettempdir()
CONFIG_DIR = os.path.abspath('../')
DATA_DIR = os.path.abspath('../')

JENKINS_SERVER_CONFIG_FILE = CONFIG_DIR + '/jenkins-server.cfg'
PROJECT_STATUS_DATA_FILE = DATA_DIR + '/proj-status.data'

GET_STATUS_DAEMON_INTERVAL = 20
SET_LIGHT_DAEMON_INTERVAL = 150

RED_GPIO_ID = 17
YELLOW_GPIO_ID = 27 
GREEN_GPIO_ID = 22
SET_LIGHT_TIMER = 150