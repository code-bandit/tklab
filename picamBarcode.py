import cv2
from time import sleep
from picamera import PiCamera
from io import BytesIO
from pyzbar.pyzbar import decode
from PIL import Image

#cam = cv2.VideoCapture(0)
camera = PiCamera()
for i in range(30):
	stream = BytesIO()
	camera.capture(stream, format="jpeg")
	stream.seek(0)
	image = Image.open(stream)
	decoded_image = decode(image)
	print(decoded_image)
	print("Decoding image" + str(i))
	sleep(1)

del(cam)
