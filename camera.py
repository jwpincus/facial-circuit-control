import picamera
from time import sleep


class Camera(object):
    camera = picamera.Picamera()

    def __init__(self, filename):
        self.filename = filename

    def snap(self):
        camera.resolution = (800, 600)
        camera.start_preview()
        sleep(1)
        camera.capture(('./images/' self.filename +'.jpg') )
