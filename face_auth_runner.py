import RPi.GPIO as GPIO
from camera import Camera
import base64
import datetime
import requests

GPIO.setmode(GPIO.BCM)

buttonPin = 17
GPIO.setup(buttonPin, GPIO.IN)
auth_url = 'http://re-cognizer.herokuapp.com/api/v1/authenticate'

while True:
    if (GPIO.input(buttonPin)):
        filename = str(datetime.datetime.now())
        Camera(filename).snap()
        with open('./images/' + filename + '.jpg', "rb") as image:
            base64image = base64.b64encode(image.read())
        response = requests.post(auth_url, data={ "app_key" : "f94a4394871ce63524cd", "image": base64image})
        image = false
        print response.text


        # send to api
        # if authorized, turn on ciruit
            # on button push disable circuit
