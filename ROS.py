import RPi.GPIO as GPIO
from time import sleep


in1 = 24
in2 = 23
en = 25
enb = 22
in3 = 17
in4 = 27
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(en,100)
q=GPIO.PWM(enb,100)

GPIO.setwarnings(False)

p.start(100)
q.start(100)

p.ChangeDutyCycle(40)
q.ChangeDutyCycle(40)

def lft():
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)

def rgt():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def fwd():
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)

def bcd():
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in1,GPIO.HIGH)

def low():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
