import RPIO
import time
import logging

import sys
sys.path.append('../')
from config import PROJECT_STATUS_DATA_FILE as proj_status_file
from config import SET_LIGHT_TIMER as timer_for_sleep
from config import RED_GPIO_ID as red
from config import YELLOW_GPIO_ID as yellow
from config import GREEN_GPIO_ID as green



def setup_lights():
    RPIO.setup(red, RPIO.OUT)
    RPIO.setup(yellow, RPIO.OUT)
    RPIO.setup(green, RPIO.OUT)


def set_status(red_status, yellow_status, green_status):
    RPIO.output(red, red_status)
    RPIO.output(yellow, yellow_status)
    RPIO.output(green, green_status)


def read_status():
    light = 'panic'
    
    #read status
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
    #clear status
    with (open(proj_status_file, 'w')) as file:
        pass

    return light


def set_light():
    try:
         timer = timer_for_sleep
         light = read_status()
    except Exception as inst:
        logging.info(str(type(inst)) + ' ' + str(inst.args))

    setup_lights()
    
    logging.info('Light is %s.' % light)
    if light == 'panic':
        timer = 10
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
