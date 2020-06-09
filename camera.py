import time
from base_camera import BaseCamera


class Camera(BaseCamera):
    """"Uma emulação de camera que fica mudando os frames 1 vez por segundo."""
    imgs = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    @staticmethod
    def frames():
        while True:
            time.sleep(1)
            yield Camera.imgs[int(time.time()) % 3]