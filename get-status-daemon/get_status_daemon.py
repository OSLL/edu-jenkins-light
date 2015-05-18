import time
import logging
import tempfile
from daemon import Daemon
from get_status import get_status

import sys
sys.path.append('../')
from config import PROJECT_STATUS_DATA_FILE as statusPath
from config import LOG_DIR as log_dir
from config import PID_DIR as pid_dir


class GetStatusDaemon(Daemon):
    def run(self):
        while True:
            with (open(statusPath, 'w')) as file:
                status = None

                try:
                    status = get_status()
                except Exception as inst:
                    logging.info(str(type(inst)) + ' ' + str(inst.args))

                if status is not None:
                    file.write(str(status[0]['score']))

            time.sleep(20)


if __name__ == '__main__':
    daemon = GetStatusDaemon(pid_dir + '/jlight_get_status_daemon.pid')
    logging.basicConfig(
        filename=log_dir + '/jlight_get_status_daemon.log',
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
