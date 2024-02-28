import time
import RPi.GPIO as GPIO

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor control pins
DIR_PIN = 7  # Updated DIR pin
PWM_PIN = 1  # Updated PWM pin

# Setup motor control pins
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Example: Move the motor forward for 2 seconds
try:
    # Set the direction
    GPIO.output(DIR_PIN, GPIO.HIGH)  # Assuming HIGH is forward, LOW is reverse

    # Set PWM
    pwm = GPIO.PWM(PWM_PIN, 1000)  # Frequency: 1000 Hz
    pwm.start(50)  # Duty cycle: 50%

    # Run the motor for 2 seconds
    time.sleep(2)

finally:
    # Cleanup
    pwm.stop()
    GPIO.cleanup()
