#!/usr/bin/env python3

import RPi.GPIO as GPIO
from inputs import get_gamepad
import time

motor_pin1 = 17  # Change GPIO pin according to your setup
motor_pin2 = 18  # Change GPIO pin according to your setup

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)

def set_motor_direction(direction):
    if direction == 'forward':
        GPIO.output(motor_pin1, GPIO.HIGH)
        GPIO.output(motor_pin2, GPIO.LOW)
    elif direction == 'backward':
        GPIO.output(motor_pin1, GPIO.LOW)
        GPIO.output(motor_pin2, GPIO.HIGH)
    else:
        GPIO.output(motor_pin1, GPIO.LOW)
        GPIO.output(motor_pin2, GPIO.LOW)

try:
    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == 'Key':
                if event.ev_code == 'BTN_SOUTH' and event.ev_value == 1:
                    set_motor_direction('forward')
                elif event.ev_code == 'BTN_EAST' and event.ev_value == 1:
                    set_motor_direction('backward')
                elif event.ev_code == 'BTN_SOUTH' or event.ev_code == 'BTN_EAST':
                    set_motor_direction('stop')

        time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()
