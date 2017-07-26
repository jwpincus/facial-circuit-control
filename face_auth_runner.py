import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

buttonPin = 17
GPIO.setup(buttonPin, GPIO.IN)

while True:
    if (GPIO.input(buttonPin))
        print "Button push"
