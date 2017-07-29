from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(21, 20)
while True:
    print('Distance: ', sensor.distance * 100)
    sleep(1)
