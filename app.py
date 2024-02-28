import time
import smbus
import RPi.GPIO as GPIO

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Motor control pins
DIR_PIN = 7  # Updated DIR pin
PWM_PIN = 1  # Updated PWM pin

# I2C setup
bus = smbus.SMBus(1)  # Use 1 for Raspberry Pi 3B+

# I2C address of the MCP23017
MCP23017_I2C_ADDRESS = 0x18  # Replace with the correct address

# MCP23017 registers
IODIRA = 0x00
GPIOA = 0x12

# Configure MCP23017
bus.write_byte_data(MCP23017_I2C_ADDRESS, IODIRA, 0x00)  # Set all pins as outputs

# Setup motor control pins
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Example: Move the motor forward for 2 seconds
try:
    # Set the direction
    current_gpioa = bus.read_byte_data(MCP23017_I2C_ADDRESS, GPIOA)
    new_gpioa = current_gpioa | (1 << DIR_PIN)  # Set the bit corresponding to DIR_PIN
    bus.write_byte_data(MCP23017_I2C_ADDRESS, GPIOA, new_gpioa)

    # Set PWM
    pwm = GPIO.PWM(PWM_PIN, 1000)  # Frequency: 1000 Hz
    pwm.start(50)  # Duty cycle: 50%

    # Run the motor for 2 seconds
    time.sleep(2)

finally:
    # Cleanup
    pwm.stop()
    GPIO.cleanup()
