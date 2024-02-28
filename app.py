import time
import RPi.GPIO as GPIO
from smbus import SMBus
from pimoroni-ioexpander import ioexpander

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor control pins
DIR_PIN = 7  # Updated DIR pin
PWM_PIN = 1  # Updated PWM pin

# Setup motor control pins
GPIO.setup(PWM_PIN, GPIO.OUT)

# I2C setup
i2c_bus = SMBus(1)

# Create IO Expander object
expander = ioexpander.IOE(i2c_bus)

# Example: Oscillate the motor using PWM and Pimoroni IO Expander
try:
    pwm = GPIO.PWM(PWM_PIN, 1000)  # Frequency: 1000 Hz
    pwm.start(50)  # Initial duty cycle: 50%

    # Oscillate for 10 seconds
    for _ in range(5):  # Oscillate 5 times
        # Forward
        expander.output(DIR_PIN, True)  # Set direction forward
        time.sleep(2)

        # Reverse
        expander.output(DIR_PIN, False)  # Set direction reverse
        time.sleep(2)

finally:
    # Cleanup
    pwm.stop()
    GPIO.cleanup()
