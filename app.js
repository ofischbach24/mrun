const rpio = require('rpio');
const keypress = require('keypress');

// Set up GPIO pins for PWM and direction
const PWM_PIN = 2;  // Replace with your PWM GPIO pin
const DIR_PIN = 12;  // Replace with your direction GPIO pin

rpio.init({ mapping: 'gpio' });

rpio.open(PWM_PIN, rpio.PWM);
rpio.open(DIR_PIN, rpio.OUTPUT, rpio.LOW);

// Function to set motor direction
function setDirection(direction) {
    rpio.write(DIR_PIN, direction);
}

// Function to set motor speed
function setSpeed(speed) {
    rpio.pwmSetData(PWM_PIN, speed);
}

// Initialize keypress library
keypress(process.stdin);

process.stdin.on('keypress', function (ch, key) {
    if (key && key.name === 'w') {
        console.log('Forward');
        setDirection(rpio.HIGH);  // Forward
        setSpeed(50);  // Adjust speed as needed
    } else if (key && key.name === 's') {
        console.log('Backward');
        setDirection(rpio.LOW);  // Backward
        setSpeed(50);  // Adjust speed as needed
    } else {
        console.log('Stop');
        setSpeed(0);  // Stop
    }
});

process.stdin.setRawMode(true);
process.stdin.resume();

// Cleanup GPIO on exit
process.on('SIGINT', function () {
    rpio.close(PWM_PIN);
    rpio.close(DIR_PIN);
    process.stdin.setRawMode(false);
    process.exit();
});
