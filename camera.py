import picamera
from time import sleep

# this class works, but I have no idea why. Don't quite understand passing arguments and what object does.

class Camera(object):

    def __init__(self, filename):
        self.filename = filename

    def snap(self):
        camera = picamera.PiCamera()
        camera.resolution = (800, 600)
        camera.start_preview()
        sleep(.5)
        camera.capture(('/home/pi/facial-circuit-control/images/' + self.filename + '.jpg'), format='jpeg', resize=(400, 300), quality=60)
        camera.close()
