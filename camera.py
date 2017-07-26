import picamera
from time import sleep


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
