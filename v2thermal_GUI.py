# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:18:25 2018

@author: Rasa
"""

import PIL
from PIL import Image, ImageTk
import tkinter as tk
import argparse
import datetime
import cv2
import os
 
class Application:
    def __init__(self, output_path = "./"):
        """ Initialize application which uses OpenCV + Tkinter. It displays
            a video stream in a Tkinter window and stores current snapshot on disk """
        self.vs = cv2.VideoCapture(0) # capture video frames, 0 is your default video camera
        self.output_path = output_path  # store output path
        self.current_image = None  # current image from the camera
 
        self.root = tk.Tk()  # initialize root window
        self.root.title("PyImageSearch PhotoBooth")  # set window title
        # self.destructor function gets fired when the window is closed
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.panel = tk.Label(self.root)  # initialize image panel
        self.panel.pack(padx=10, pady=10)
        self.root.config(cursor="arrow")
 
        # create a button, that when pressed, will take the current frame and save it to file
        btn = tk.Button(self.root, text="Snapshot!", command=self.take_snapshot)
        btn.pack(fill="both", expand=True, padx=10, pady=10)
 
        # start a self.video_loop that constantly pools the video sensor
        # for the most recently read frame
        self.video_loop()
     
 
    def video_loop(self):
        """ Get frame from the video stream and show it in Tkinter """
        ok, frame = self.vs.read()  # read frame from video stream
#        frame = cv2.resize(frame, (1500,1000))
        if ok:  # frame captured without any errors
            key = cv2.waitKey(1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            self.current_image = Image.fromarray(cv2image)  # convert image for PIL
            #self.current_image= self.current_image.resize([1280,1024],PIL.Image.ANTIALIAS)
            imgtk = PIL.ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter 
            self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector  
            self.panel.config(image=imgtk)  # show the image
            #self.root.attributes("-fullscreen",True)
        self.root.after(1, self.video_loop)  # call the same function after 30 milliseconds
 
    def take_snapshot(self):
        """ Take snapshot and save it to the file """
        ts = datetime.datetime.now() # grab the current timestamp
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))  # construct filename
        p = os.path.join(self.output_path, filename)  # construct output path
        self.current_image.save(p, "JPEG")  # save image as jpeg file
        print("[INFO] saved {}".format(filename))
 
    def destructor(self):
        """ Destroy the root object and release all resources """
        print("[INFO] closing...")
        self.root.destroy()
        self.vs.release()  # release web camera
        cv2.destroyAllWindows()  # it is not mandatory in this application
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", default="./",
    help="path to output directory to store snapshots (default: current folder")
args = vars(ap.parse_args())
 
# start the app
print("[INFO] starting...")
pba = Application(args["output"])
pba.root.mainloop()