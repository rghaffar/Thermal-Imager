# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
(h, w) = (None, None) 
# allow the camera to warmup
time.sleep(0.1)
writer = None 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
 
        # show the frame
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        # Crest writer on first loop
        if writer is None:
            (h, w) = image.shape[:2]
            writer = cv2.VideoWriter("test.avi", fourcc, 5,(w, h), True)
            zeros = np.zeros((h, w), dtype="uint8")
        #record and show stream
        writer.write(image)
	# clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break