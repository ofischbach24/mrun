import time
from pimoroni_ioexpander import ioexpander
from ioexpander.motor import Motor, FAST_DECAY, SLOW_DECAY, NORMAL_DIR, REVERSED_DIR

ioe = ioexpander.SuperIOE()  # Replace IOE with SuperIOE for Nuvoton chip

# Motor control pins
DIR_PIN = 7  # Analog pin 7
PWM_PIN = 1  # PWM pin 1
motor = Motor(ioe, (DIR_PIN, PWM_PIN), direction=NORMAL_DIR, mode=SLOW_DECAY)

# Set calibration parameters
speed_scale = 1.0
zeropoint = 0.0
motor.speed_scale(speed_scale)
motor.zeropoint(zeropoint)

# Set duty cycle deadzone
deadzone = 0.05
motor.deadzone(deadzone)

# Set motor frequency
frequency = 25000  # 25 KHz
motor.frequency(frequency)

# Example: Control the motor
try:
    motor.start()  # Use start instead of enable

    # Set an initial duty cycle
    motor.duty(0.5)
    time.sleep(2)

    # Change the motor direction
    motor.direction(REVERSED_DIR)
    time.sleep(2)

    # Change the decay mode
    motor.decay_mode(FAST_DECAY)
    time.sleep(2)

finally:
    # Cleanup
    motor.stop()  # Use stop instead of disable
