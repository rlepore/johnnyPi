"""
Test script that will help us ensure that our motors can move forwards,
backwards and stop.
"""

import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)

# Add a name to the GPIO pins that we are using for the motors.  We are naming
# them according to the L293D chip for clarity.
motor_1A = 24
motor_1B = 23
motor_1E = 25

motor_2A = 9
motor_2B = 10
motor_2E = 11

# Let python know that our motors pins are going to be output pins not input.
GPIO.setup(motor_1A, GPIO.OUT)
GPIO.setup(motor_1B, GPIO.OUT)
GPIO.setup(motor_1E, GPIO.OUT)

GPIO.setup(motor_2A, GPIO.OUT)
GPIO.setup(motor_2B, GPIO.OUT)
GPIO.setup(motor_2E, GPIO.OUT)


def move_forwards():
    """
    Tell the L293D chip what pins should do the forwards movement.
    """
    print "Going Forwards....."
    GPIO.output(motor_1A, GPIO.HIGH)
    GPIO.output(motor_1B, GPIO.LOW)
    GPIO.output(motor_1E, GPIO.HIGH)

    GPIO.output(motor_2A, GPIO.HIGH)
    GPIO.output(motor_2B, GPIO.LOW)
    GPIO.output(motor_2E, GPIO.HIGH)


def move_backwards():
    """
    Tell the L293D chip what pins should do the backwards movement.
    """
    print "Going Backwards....."
    GPIO.output(motor_1A, GPIO.LOW)
    GPIO.output(motor_1B, GPIO.HIGH)
    GPIO.output(motor_1E, GPIO.HIGH)

    GPIO.output(motor_2A, GPIO.LOW)
    GPIO.output(motor_2B, GPIO.HIGH)
    GPIO.output(motor_2E, GPIO.HIGH)


def go_to_sleep(seconds=2):
    """
    Put the process to sleep for the number of seconds provided.  Defaulting
    to 2 seconds.
    """
    print "Sleeping for 2 seconds...."
    sleep(seconds)


def stop_motors():
    """
    Tell the L293D which pins to stop.
    """
    print "Stoping the motors...."
    GPIO.output(motor_1E, GPIO.LOW)
    GPIO.output(motor_2E, GPIO.LOW)


def clean_up():
    GPIO.cleanup()


if __name__ == "__main__":
    """
    Main function that will just run the test.  The test is very simple and
    will just move the motors forward, sleep, backwards, sleep then stop and
    clean up before shutting down.  This will simply just let us know if our
    motors are working the way we expect them to.
    """
    move_forwards()
    go_to_sleep()
    move_backwards()
    go_to_sleep()
    stop_motors()
    clean_up()
