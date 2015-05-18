#!/usr/bin/python3
from app import app
import sys
import logging

sys.path.append('../')
from config import WEBSERVER_ADDRESS, WEBSERVER_PORT, WEBSERVER_DEBUG_STATUS
from config import LOG_DIR as log_dir

logging.basicConfig(
        filename=log_dir + '/jlight_webserver.log',
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S'
    )
app.run(host=WEBSERVER_ADDRESS, port=WEBSERVER_PORT, debug=WEBSERVER_DEBUG_STATUS)
