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
        camera.capture(('./images/' + self.filename + '.jpg'), resize=(400, 300), quality=(60) )
        camera.stop_preview()
