import RPi.GPIO as GPIO
from time import sleep
from tkinter import *

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

running = False
root = Tk()

def start_Fmotor(event):
    global running
    print("starting motor...")
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    running = True

def start_Bmotor(event):
    global running
    print("starting motor...")
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in1,GPIO.HIGH)
    running = True

def start_Lmotor(event):
    global running
    print("starting motor...")
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    running = True

def start_Rmotor(event):
    global running
    print("starting motor...")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    running = True

def stop_motor(event):
    global running
    running = False
    print("stopping motor...")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

buttonF = Button(root, text ="forward")
buttonF.pack(side='top')
buttonF.bind('<ButtonPress-1>',start_Fmotor)
buttonF.bind('<ButtonRelease-1>',stop_motor)

buttonB = Button(root, text ="Backward")
buttonB.pack(side='bottom')
buttonB.bind('<ButtonPress-1>',start_Bmotor)
buttonB.bind('<ButtonRelease-1>',stop_motor)

buttonL = Button(root, text ="Left")
buttonL.pack(side='left')
buttonL.bind('<ButtonPress-1>',start_Lmotor)
buttonL.bind('<ButtonRelease-1>',stop_motor)

buttonR = Button(root, text ="Right")
buttonR.pack(side='right')
buttonR.bind('<ButtonPress-1>',start_Rmotor)
buttonR.bind('<ButtonRelease-1>',stop_motor)

root.mainloop()