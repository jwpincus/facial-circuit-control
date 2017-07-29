import RPi.GPIO as GPIO
import time import sleep

class DistanceSensor:
    GPIO.setmode(GPIO.BCM)
    TRIG = 20
    ECHO = 21
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    def measure(self):
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        GPIO.cleanup()
        distance = round(distance, 2)
        return distance

distance = DistanceSensor()

while True:
    distance.measure
    sleep(1)
