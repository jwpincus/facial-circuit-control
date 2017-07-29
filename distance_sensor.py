from gpiozero import DistanceSensor

ultrasonic = DistanceSensor(echo=24, trigger=17)
while True:
        print ultrasonic.distance
