from gpiozero import DistanceSensor

class Distance:
    ultrasonic = DistanceSensor(echo=24, trigger=17)
    def sense(self):
        print ultrasonic.distance
Distance().sense()
