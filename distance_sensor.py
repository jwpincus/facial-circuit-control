import RPi.GPIO as GPIO
import time

class DistanceSensor:
    """
    @flowerChildParameter { ref = "echo_pin", type = "int" }
    @flowerChildParameter { ref = "trigger_pin", type = "int" }
    """
    def __init__(self, echo_pin = 21, trigger_pin = 20):
        self.GPIO_TRIGGER = trigger_pin
        self.GPIO_ECHO = echo_pin

    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def stop(self):
        return

    def measure(self):
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
        StartTime = time.time()
        StopTime = time.time()
        timeoutStart = time.time()
        while GPIO.input(self.GPIO_ECHO) == 0 and (time.time() - timeoutStart) < 3:
            StartTime = time.time()
        while GPIO.input(self.GPIO_ECHO) == 1 and (time.time() - timeoutStart) < 3:
            StopTime = time.time()
            TimeElapsed = StopTime - StartTime
            distance = (TimeElapsed * 34300) / 2
        print distance
        return distance

        def loop(self):
            return
