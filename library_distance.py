from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=21, trigger=20)
while True:
    print('Distance: ', sensor.distance() * 100.0)
    sleep(1)
