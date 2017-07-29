from gpiozero import DistanceSensor

class Distance:
    def sense(self):
        ultrasonic = DistanceSensor(echo=24, trigger=17)
        print ultrasonic.distance
Distance().sense()
