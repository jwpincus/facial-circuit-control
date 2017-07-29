import RPi.GPIO as GPIO
from camera import Camera
import base64
import datetime
import requests
from IPython import embed
from time import sleep
from distance_sensor import DistanceSensor

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

buttonPin = 17
relayPin = 18


GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(relayPin, GPIO.OUT)


circuit = False # the program should initialize with the circuit off
GPIO.output(relayPin, circuit)
auth_url = 'http://re-cognizer.herokuapp.com/api/v1/authenticate'
base64_prefix = 'data:image/jpeg;base64,' # this is for the benefit of the API. Authentication works without this, but displaying the image in the log does not
sensor = DistanceSensor()
sensor.setup()

while True:
    distance = sensor.measure()
    if ((distance < 50.0) and not circuit):
        filename = str(datetime.datetime.now()) # create unique save name for file. At this point the device saves all files. Not sure if feature or bug
        Camera(filename).snap()
        with open('/home/pi/facial-circuit-control/images/' + filename + '.jpg', "rb") as image: # I guess this is how to do it in python?
            base64_image = base64.b64encode(image.read()) # encode the image as base64 string
        response = requests.post(auth_url, data={ "app_key" : "f94a4394871ce63524cd", "image": base64_prefix + base64_image})
        if (response.json()['authenticated']):
            circuit = True
            GPIO.output(relayPin, circuit)
    elif (GPIO.input(buttonPin) and circuit):
        circuit = False # set state for circuit
        GPIO.output(relayPin, circuit) # send state to physical circuit
        sleep(10) # give the user time to get their finger off the button and leave
    sleep(.5)
