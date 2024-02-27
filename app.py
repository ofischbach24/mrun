import time
from gpiozero import OutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from i2c import IoExpander
import RPi.GPIO as GPIO

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set up the PiGPIOFactory for I2C communication
i2c_factory = PiGPIOFactory()

# Define PWM and DIR pins connected to the GPIO expander
pwm_pin = 1  # Replace with the actual PWM pin number on the GPIO expander
dir_pin = 7  # Replace with the actual DIR pin number on the GPIO expander

# Set up the IoExpander with the proper I2C address
ioe = IoExpander(0x18, i2c_factory=i2c_factory)

# Create PWM and DigitalOutputDevice objects using gpiozero
pwm = OutputDevice(pwm_pin, pin_factory=ioe)
dir_motor = OutputDevice(dir_pin, pin_factory=ioe)

# Function to control the motor direction and speed
def control_motor(direction, speed):
    dir_motor.value = direction  # Set motor direction
    pwm.value = speed / 100.0  # Set PWM duty cycle (0 to 1)

# Example usage with input handling
try:
    while True:
        # Move the motor forward at 50% speed
        control_motor(1, 50)
        time.sleep(2)

        # Move the motor backward at 75% speed
        control_motor(0, 75)
        time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up GPIO on exit
    pwm.close()
    dir_motor.close()
    ioe.close()
