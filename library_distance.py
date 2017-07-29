from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=21, trigger=20)
while True:
    print('Distance: ', sensor.distance())
    sleep(1)
