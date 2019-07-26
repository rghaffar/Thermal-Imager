# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:41:32 2018

@author: Rasa
"""

import cv2
import os

def stream():
    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    stream.cap = cv2.VideoCapture(0)
    stream.cap.frame_width = int(stream.cap.get(3))
    stream.frame_height = int(stream.cap.get(4))
 
    # Check if camera opened successfully
    if (stream.cap.isOpened()== False): 
        print("Error opening video stream or file")
  
    # Read until video is completed
    while(stream.cap.isOpened()):
        # Capture frame-by-frame
        ret, stream.frame = stream.cap.read()
        if ret == True:  
            # Increase size of frame by 4x
            #stream.frame = cv2.resize(stream.frame,(800,600))
            # Display the resulting frame
            cv2.imshow('Frame', stream.frame)
            
            # Press Q on keyboard to  exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                # When loop is exited, release the video capture and close all frames
                stream.cap.release()
                cv2.destroyAllWindows()
                
'''
def video():
    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = int(stream.cap.get(3))
    frame_height = int(stream.cap.get(4))
    i = 0
    while os.path.exists('video%s.avi' %i):
        i += 1
    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter('video%s.avi' %i,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
    # Write the frame into the file 'output.avi'
    
    out.write(stream.frame)
    if 0xFF == ord('s'):
        # release video write objects  
        out.release() 
'''       
stream()
 
