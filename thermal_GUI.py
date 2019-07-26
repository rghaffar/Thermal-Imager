# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:01:55 2018

@author: Rasa
"""

import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

'''
#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Thermal Camera")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=800, height=600)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

def show_frame():
    ret, frame = cap.read()
    img = frame
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 



show_frame()  #Display 2
window.mainloop()  #Starts GUI
'''
root = Tk()

w = Canvas(root, width=500, height=300, bd = 10, bg = 'white')
w.grid(row = 0, column = 0, columnspan = 2)

b = tk.button(width = 10, height = 2, text = 'Button1')
b.grid(row = 1, column = 0)
b2 = tk.button(width = 10, height = 2, text = 'Button2')
b2.grid(row = 1,column = 1)

cv2.NamedWindow("camera",1)
capture = cv2.CaptureFromCAM(0)

while True:
    img = cv2.QueryFrame(capture)
    tk.canvas.create_image(0,0, image=img)
    if cv2.WaitKey(10) == 27:
        break

root.mainloop()