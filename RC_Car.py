import RPi.GPIO as GPIO
from time import sleep
import pygame

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

p.ChangeDutyCycle(100)
q.ChangeDutyCycle(100)

def init():
    win = pygame.display.set_mode((100,100))
def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput [myKey]:
        ans = True
    pygame.display.update()

    return ans

def main():
    if getKey('a'):
        print('Left')
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        sleep(0.1)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
    elif getKey('d'):
        print('Right')
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

    elif getKey('s'):
        print('Backward')
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in1,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
    elif getKey('w'):
        print('Forward')
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        sleep(0.1)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
    else:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
if __name__ == '__main__':
    init()
    while True:
        main()