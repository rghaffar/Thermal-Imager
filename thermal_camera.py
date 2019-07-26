# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 17:24:02 2018

@author: Rasa
"""
import cv2
import os

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
  
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

i = 0
while os.path.exists('video%s.avi' %i):
    i += 1
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('video%s.avi' %i,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:  
    # Write the frame into the file 'output.avi'
    out.write(frame)
    #print(frame)
    # Increase size of frame by 4x
    frame = cv2.resize(frame,(800,600))
    # Display the resulting frame
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(25) & 0xFF == ord('s'):
        j = 0
        while os.path.exists('image%s.png' %j):
            j += 1
        cv2.imwrite('image%s.png' %j,frame)
    # Press Q on keyboard to  exit
    elif cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
  # Break the loop
  else: 
    break

# When everything done, release the video capture and video write objects
cap.release()
out.release() 
 
# Closes all the frames
cv2.destroyAllWindows()