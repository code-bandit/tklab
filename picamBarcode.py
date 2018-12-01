from time import sleep
from picamera import PiCamera
from io import BytesIO
from pyzbar.pyzbar import decode
from PIL import Image

class BarCode:
    def __init__(self):
        camera = PiCamera()
    def read():
        for i in range(30):
            stream = BytesIO()
            camera.capture(stream, format="jpg")
            stream.seek(0)
            image = Image.open(stream)
            decoded_image = decode(image)
            if decoded_image:
                return decoded_image
                break
            sleep(1)
        return -1
    def close():
        camera.close()
        del(camera)

BarCode bar()
result = bar.read()
print(result)
bar.close()