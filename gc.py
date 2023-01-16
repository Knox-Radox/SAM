import RPi.GPIO as GPIO
import time
from ROS import *
import sys
import signal
GPIO.setmode(GPIO.BCM)

TRIG = 6
ECHO = 5

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
#try:
while True:
    echo_state = 0

    GPIO.output(TRIG, False)
#    print ("Waiting For Sensor To Settle")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while echo_state == 0:
        echo_state = GPIO.input(ECHO)
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

#    print ("Distance:",distance,"cm")

#except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
#    print("Cleaning up!")
#    gpio.cleanup()
    print(distance)
    fwd()
#    print(distance)
    if distance < 20:
        p.ChangeDutyCycle(100)
        q.ChangeDutyCycle(100)

        low()
        sleep(0.5)
        lturn()
        sleep(1)
        low()
        sleep(0.5)
        ld = distance
        print("left distance is", ld)
        lnorm()
        sleep(0.5)
        rturn()
        sleep(1)
        rd = distance
        print("right distance is", rd)
        if ld > rd:
            continue
        else:
            lturn()
            sleep(0.5)
            continue