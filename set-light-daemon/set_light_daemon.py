import time
import logging
from daemon import Daemon
from set_light import set_light

import sys
sys.path.append('../')
from config import PROJECT_STATUS_DATA_FILE as proj_status_file
from config import LOG_DIR as log_dir
from config import PID_DIR as pid_dir


class SetLightDaemon(Daemon):
    def run(self):
        while True:
            set_light()


if __name__ == '__main__':
    daemon = SetLightDaemon(pid_dir + '/jlight_set_light_daemon.pid')
    logging.basicConfig(
        filename=log_dir + '/jlight_set_light_daemon.log',
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S'
    )

    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            logging.info('Daemon start.')
            daemon.start()
        elif 'stop' == sys.argv[1]:
            logging.info('Daemon stop.')
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            logging.info('Daemon restart.')
            daemon.restart()
        else:
            print ('Unknown command.')
            sys.exit(2)
        sys.exit(0)
    else:
        print ('usage: %s start|stop|restart' % sys.argv[0])
        sys.exit(2)
