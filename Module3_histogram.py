# -*- coding: utf-8 -*-
"""
Module 3: Display histogram and apply contrast/thresholds for selected channel

@author: Rasa
"""

import matplotlib
import numpy
import Module1_getimagedata as imgdata

        
def select_channel():
    channel_list = ['red','blue','green','b/w']
    channel = input('Please enter channel from the following options: red, blue, green, b/w ')
    if channel.lower() in channel_list:
        response_list = ['yes','no','y','n']
        response = input('Would you like to view a histogram? (yes/no): ')
        if response.lower() in response_list:
            if channel == 'red':
                display_histogram(imgdata.matrix.r)
            if channel == 'green':
                display_histogram(imgdata.matrix.g)
            if channel == 'blue':
                display_histogram(imgdata.matrix.b)
            if channel == 'b/w':
                display_histogram(imgdata.matrix.grey)                
        else:
            print('Please enter a valid response') 
    else:
        print('Please enter valid channel option')
    return(channel)
    
def display_histogram(image_matrix):
    bins = numpy.linspace(1,255,num=256)
    matplotlib.pyplot.hist(image_matrix, bins)
    
select_channel()

        