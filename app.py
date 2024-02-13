#!/usr/bin/env python3

import RPi.GPIO as GPIO
from inputs import get_key
import time

motor_pin1 = 17  # Change GPIO pin according to your setup
motor_pin2 = 18  # Change GPIO pin according to your setup

GPIO.setmode(GPIO.BCM)
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
        events = get_key()
        for event in events:
            if event.ev_type == 'Key':
                if event.ev_code == 'BTN_A' and event.ev_value == 1:
                    set_motor_direction('forward')
                elif event.ev_code == 'BTN_B' and event.ev_value == 1:
                    set_motor_direction('backward')
                elif event.ev_code == 'BTN_A' or event.ev_code == 'BTN_B':
                    set_motor_direction('stop')

        time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()
