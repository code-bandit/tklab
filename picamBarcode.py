from time import sleep
from picamera import PiCamera
from io import BytesIO
from pyzbar.pyzbar import decode
from PIL import Image

class BarCode:
    def __init__(self):
	pass

    def read(self):
 	camera = PiCamera()
        for i in range(30):
            stream = BytesIO()
            camera.capture(stream, format="jpeg")
            stream.seek(0)
            image = Image.open(stream)
            decoded_image = decode(image)
	    print(decoded_image)
            if decoded_image:
                return decoded_image
                break
            sleep(1)
        camera.close()
        del(camera)
        return -1

bar=BarCode()
result = bar.read()
print(result)