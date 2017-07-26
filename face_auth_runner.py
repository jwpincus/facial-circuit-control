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
        with open('./images/' + filename + '.jpg', "rb") as image:
            base64image = base64.b64encode(image.read())
            print base64image
        # send to api
        # if authorized, turn on ciruit
            # on button push disable circuit
