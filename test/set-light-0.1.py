import RPIO
import time
import sys
sys.path.append('../')
from config import PROJECT_STATUS_DATA_FILE as proj_status_file

red = 17
yellow = 27
green = 22


def setup_lights():
    RPIO.setup(red, RPIO.OUT)
    RPIO.setup(yellow, RPIO.OUT)
    RPIO.setup(green, RPIO.OUT)


def set_status(red_status, yellow_status, green_status):
    RPIO.output(red, red_status)
    RPIO.output(yellow, yellow_status)
    RPIO.output(green, green_status)


def set_light():
    light = 'panic'
    setup_lights()
    timer = 5

    with (open(proj_status_file, 'r')) as file:
        data = file.read()

        if data.isnumeric():
            status = int(data)

            if (status < 0 or status > 100):
                pass
            elif status < 51:
                light = 'red'
            elif status < 80:
                light = 'yellow'
            elif status < 100:
                light = 'yellow-green'
            else:
                light = 'green'

    if light == 'panic':
        while timer > 0:
            timer -= 0.4
            set_status(True, True, True)
            time.sleep(0.2)
            set_status(False, False, False)
            time.sleep(0.2)

    elif light == 'red':
        set_status(True, False, False)
        time.sleep(timer)
    elif light == 'yellow':
        set_status(False, True, False)
        time.sleep(timer)
    elif light == 'yellow-green':
        set_status(False, True, True)
        time.sleep(timer)
    elif light == 'green':
        set_status(False, False, True)
        time.sleep(timer)

    RPIO.cleanup()

if __name__ == '__main__':
    set_light()
