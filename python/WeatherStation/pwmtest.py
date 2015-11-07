__author__ = 'psk'
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
_lightcontrolPwm =  GPIO.PWM(18, 50) #Pin 18 for backlight control and using default 50 hz
_lightcontrolPwm.start(10)
time.sleep(2)

try:
    while True:
        n=0
        print "PWM increase..."

        while n<100:
            _lightcontrolPwm.ChangeDutyCycle(n)
            time.sleep(0.1)
            n= n+1
        print "PWM decrease....."

        while n>0:
            _lightcontrolPwm.ChangeDutyCycle(n)
            time.sleep(0.1)
            n= n-1

finally:
    _lightcontrolPwm.stop()
    GPIO.cleanup()



