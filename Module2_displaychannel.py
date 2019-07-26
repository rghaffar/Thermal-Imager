# -*- coding: utf-8 -*-
"""
Module 2: Display image for selected channel, saves image channel in greyscale

@author: Rasa
"""

import matplotlib
import scipy.misc
import Module1_getimagedata as imgdata


def display_channel(image_matrix):
    matplotlib.pyplot.imshow(image_matrix)
    scipy.misc.toimage(image_matrix).save('channel_output.jpg') #saves in b/w palette
    #matplotlib.pyplot.savefig('test_out_rchannel' + '.jpg')
        
    
def select_channel():
    channel_list = ['red','blue','green','b/w']
    channel = input('Please enter channel from the following options: red, blue, green, b/w ')
    if channel.lower() in channel_list:
        if channel == 'red':
            display_channel(imgdata.matrix.r)
        if channel == 'green':
            display_channel(imgdata.matrix.g)
        if channel == 'blue':
            display_channel(imgdata.matrix.b)
        if channel == 'grey':
            display_channel(imgdata.matrix.grey)            
    else:
        print('Please enter valid channel option')
    return(channel)
    
select_channel()