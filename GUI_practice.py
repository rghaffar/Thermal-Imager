# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 10:17:51 2018

@author: Rasa
"""

import tkinter as tk
import cv2   

def write_slogan():
    print("Tkinter is easy to use!")
    
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
            
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Stream Video",
                   command=stream)
slogan.pack(side=tk.LEFT)

root.mainloop()