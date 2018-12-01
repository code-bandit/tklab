import cv2
from time import sleep
from picamera import PiCamera
from io import BytesIO
from pyzbar.pyzbar import decode
from PIL import Video

def FrameCapture(path): 
    vidObj = cv2.VideoCapture(path) 
    count = 0
    success = 1
  
    while success: 
        success, image = vidObj.read() 
		decoded_image = decode(image)
		if decoded_image:
			print(str(count) + " " + decoded_image)
			return 1
		count += 1

if __name__ == '__main__': 
    FrameCapture("home\\pi\\Desktop\\tklab\\barcode\\opencv\\openCV.mp4") 

#cam = cv2.VideoCapture(0)
camera = PiCamera()
stream = BytesIO()
camera.start_recording("home/pi/Desktop/tklab/barcode/opencv/test.h264")
camera.wait_recording(1)
camera.stop_recording()
d = FrameCapture("home/pi/Desktop/tklab/barcode/opencv/test.h264")
# image = Image.open(stream)
# decoded_image = decode(image)
print(d)

del(camera)
