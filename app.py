import time
import RPi.GPIO as GPIO

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins connected to the GPIO expander for PWM and DIR
pwm_pin = 1  # Replace with the actual PWM pin number on the GPIO expander
dir_pin = 7  # Replace with the actual DIR pin number on the GPIO expander

# Set up GPIO pins
try:
    GPIO.setup(pwm_pin, GPIO.OUT)
    GPIO.setup(dir_pin, GPIO.OUT)

    # Create PWM object with a frequency of 1000 Hz
    pwm = GPIO.PWM(pwm_pin, 1000)

    # Function to control the motor direction and speed
    def control_motor(direction, speed):
        GPIO.output(dir_pin, direction)  # Set motor direction
        pwm.start(speed)  # Start PWM with specified duty cycle (0 to 100)

    # Example usage
    try:
        while True:
            # Move the motor forward at 50% speed
            control_motor(GPIO.HIGH, 50)
            time.sleep(2)

            # Move the motor backward at 75% speed
            control_motor(GPIO.LOW, 75)
            time.sleep(2)

    except KeyboardInterrupt:
        pass

finally:
    # Clean up GPIO on exit
    GPIO.cleanup()
