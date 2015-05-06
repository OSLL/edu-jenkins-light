import sys
import time
from daemon import Daemon
from get_status import get_status


class GetStatusDaemon(Daemon):
    def run(self):
        while True:
            with (open ('/home/work/project/proj/status.data', 'w')) as file:
                file.write (str (get_status ()[0]['score']))
            time.sleep(10)

if __name__ == '__main__':
    daemon = GetStatusDaemon('/tmp/jlight-get-status-daemon.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print ('Unknown command')
            sys.exit(2)
        sys.exit(0)
    else:
        print ('usage: %s start|stop|restart' % sys.argv[0])
        sys.exit(2)
