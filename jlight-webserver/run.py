#!/usr/bin/python3
from app import app
from config import WEBSERVER_ADDRESS, WEBSERVER_PORT, WEBSERVER_DEBUG_STATUS

app.run(host=WEBSERVER_ADDRESS, port=WEBSERVER_PORT, debug=WEBSERVER_DEBUG_STATUS)
