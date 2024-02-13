#include <iostream>
#include <thread>
#include <libevdev.h>
#include <libevdev/libevdev-uinput.h>
#include <pigpio.h>

// GPIO pins for PWM and direction
#define PWM_PIN 18  // Replace with your PWM GPIO pin
#define DIR_PIN 23  // Replace with your direction GPIO pin

// PWM frequency and range
#define PWM_FREQUENCY 1000
#define PWM_RANGE 255

// Motor speed
#define MOTOR_SPEED 100

// Function to initialize GPIO
void initializeGPIO() {
    if (gpioInitialise() < 0) {
        std::cerr << "Failed to initialize GPIO" << std::endl;
        std::exit(EXIT_FAILURE);
    }

    // Set up PWM
    gpioSetMode(PWM_PIN, PI_OUTPUT);
    gpioSetPWMfrequency(PWM_PIN, PWM_FREQUENCY);
    gpioSetPWMrange(PWM_PIN, PWM_RANGE);

    // Set up direction pin
    gpioSetMode(DIR_PIN, PI_OUTPUT);
}

// Function to control motor direction
void setDirection(bool forward) {
    gpioWrite(DIR_PIN, forward ? PI_HIGH : PI_LOW);
}

// Function to control motor speed
void setSpeed(int speed) {
    gpioPWM(PWM_PIN, speed);
}

int main() {
    // Initialize GPIO
    initializeGPIO();

    // Create a virtual input device for keyboard emulation
    int uinput_fd = libevdev_uinput_create_from_device(libevdev_uinput_open(),
                                                       LIBEVDEV_UINPUT_OPEN_MANAGED);

    if (uinput_fd < 0) {
        std::cerr << "Failed to create virtual input device" << std::endl;
        std::exit(EXIT_FAILURE);
    }

    // Main loop to read keyboard inputs and control motors
    while (1) {
        struct input_event ev;
        ssize_t n = read(uinput_fd, &ev, sizeof(ev));

        if (n == sizeof(ev) && ev.type == EV_KEY && ev.value == 1) {
            switch (ev.code) {
                case KEY_W:
                    std::cout << "Forward" << std::endl;
                    setDirection(true);  // Forward
                    setSpeed(MOTOR_SPEED);  // Adjust speed as needed
                    break;
                case KEY_S:
                    std::cout << "Backward" << std::endl;
                    setDirection(false);  // Backward
                    setSpeed(MOTOR_SPEED);  // Adjust speed as needed
                    break;
                default:
                    std::cout << "Stop" << std::endl;
                    setSpeed(0);  // Stop
            }
        }

        std::this_thread::sleep_for(std::chrono::milliseconds(100));  // Adjust sleep time if needed
    }

    // Cleanup
    libevdev_uinput_destroy(uinput_fd);
    gpioTerminate();

    return 0;
}
