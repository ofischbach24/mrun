#include <iostream>
#include <wiringPi.h>
#include <wiringPiI2C.h>

// IO Expander I2C address
const int ioExpanderAddress = 0x18; // Replace with the actual address of your IO expander

// IO Expander pin for PWM
const int pwmPin = 1; // Replace with the actual PWM pin number on the IO expander

int main() {
    // Initialize WiringPi and IO Expander
    wiringPiSetup();
    int ioExpander = wiringPiI2CSetup(ioExpanderAddress);

    // Set PWM range (0 to 1023) - adjust as needed
    int pwmRange = 1023;

    // Set PWM frequency (Hz) - adjust as needed
    int pwmFrequency = 1000;

    // Initialize PWM
    wiringPiI2CWriteReg16(ioExpander, 0x12, pwmRange); // PWM range register
    wiringPiI2CWriteReg16(ioExpander, 0x10, pwmFrequency); // PWM frequency register

    // Main PWM loop
    while (true) {
        // Set PWM value (0 to pwmRange) - adjust as needed
        int pwmValue = 512;

        // Update PWM duty cycle
        wiringPiI2CWriteReg16(ioExpander, pwmPin, pwmValue);

        delay(1000); // Delay for 1 second (adjust as needed)
    }

    return 0;
}
