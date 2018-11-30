import cv2
from time import sleep
from pyzbar.pyzbar import decode
from PIL import Image

cam = cv2.VideoCapture(0)
#camera = PiCamera()

for i in range(30):
	val, img = cam.read()
	decoded_image = decode(img)
	if decoded_image:
		print((decoded_image[0].data))
	print("Decoding image" + str(i))
	cv2.imwrite('tklab/barcode/opencv'+str(i)+'.png', img)
	sleep(1)

del(cam)
