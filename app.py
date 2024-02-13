import RPi.GPIO as GPIO
import time
import sys
import tty
import termios

# Set up GPIO pins for PWM and direction
PWM_PIN = 18  # Replace with your PWM GPIO pin
DIR_PIN = 23  # Replace with your direction GPIO pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Set up PWM
pwm = GPIO.PWM(PWM_PIN, 1000)  # 1000 Hz frequency, you can adjust as needed
pwm.start(0)  # Start PWM with duty cycle 0

# Function to set motor direction
def set_direction(direction):
    GPIO.output(DIR_PIN, direction)

# Function to set motor speed
def set_speed(speed):
    pwm.ChangeDutyCycle(speed)

# Function to get keyboard input without waiting for Enter key
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Main loop to read keyboard inputs and control motors
try:
    while True:
        key = getch()

        if key == 'w':
            set_direction(GPIO.HIGH)  # Forward
            set_speed(50)  # Adjust speed as needed
        elif key == 's':
            set_direction(GPIO.LOW)  # Backward
            set_speed(50)  # Adjust speed as needed
        elif key == ' ':
            set_speed(0)  # Stop

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO on exit
    GPIO.cleanup()
