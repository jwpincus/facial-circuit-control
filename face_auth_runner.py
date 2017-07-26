import RPi.GPIO as GPIO
from camera import Camera
import base64
import datetime

GPIO.setmode(GPIO.BCM)

buttonPin = 17
GPIO.setup(buttonPin, GPIO.IN)

while True:
    if (GPIO.input(buttonPin)):
        filename = str(datetime.datetime.now())
        Camera(filename).snap()
        puts "image created"
        # send to api
        # if authorized, turn on ciruit
            # on button push disable circuit
