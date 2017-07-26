import RPi.GPIO as GPIO
from camera import Camera
import base64
import datetime
import requests
from IPython import embed
from time import sleep

GPIO.setmode(GPIO.BCM)

buttonPin = 17
GPIO.setup(buttonPin, GPIO.IN)
relayPin = 18
GPIO.setup(relayPin, GPIO.OUT)

circuit = False
auth_url = 'http://re-cognizer.herokuapp.com/api/v1/authenticate'
base64_prefix = 'data:image/jpeg;base64,'

while True:
    if (GPIO.input(buttonPin) and not circuit):
        filename = str(datetime.datetime.now())
        Camera(filename).snap()
        with open('./images/' + filename + '.jpg', "rb") as image:
            base64_image = base64.b64encode(image.read())
        response = requests.post(auth_url, data={ "app_key" : "f94a4394871ce63524cd", "image": base64_prefix + base64_image})
        print response.text
        if (response.json()['authenticated']):
            circuit = True
            GPIO.output(relayPin, circuit)
    elif (GPIO.input(buttonPin) and circuit):
        circuit = False
        GPIO.output(relayPin, circuit)
        sleep(2)
        # if authorized, turn on ciruit
            # on button push disable circuit
