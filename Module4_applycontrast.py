# -*- coding: utf-8 -*-
"""
Module 4: Apply contrast to the selected channel

@author: Rasa
"""

import matplotlib
import numpy
import Module1_getimagedata as imgdata

        
def select_channel():
    channel_list = ['red','blue','green','b/w']
    channel = input('Please enter channel from the following options: red, blue, green, b/w ')
    if channel.lower() in channel_list:
        if channel == 'red':
            apply_contrast(imgdata.array.r,imgdata.matrix.r)
        if channel == 'green':
            apply_contrast(imgdata.array.g,imgdata.matrix.g)
        if channel == 'blue':
            apply_contrast(imgdata.array.b,imgdata.matrix.b)
        if channel == 'b/w':
            apply_contrast(imgdata.array.grey,imgdata.matrix.grey)
    else:
        print('Please enter valid channel option')
    return(select_channel.channel)

def apply_contrast(image_array,image_matrix):
        min_value = int(input('Select a lower threshold between 0-255: '))
        max_value = int(input('Select an upper threshold between 0-255: '))
        threshold_array = []
        for element in image_array:
            threshold_array.append(element)
        for element in range(0,len(threshold_array)):
            if threshold_array[element] <= min_value:
                threshold_array[element] = min_value
            elif threshold_array[element] >= max_value:
                threshold_array[element] = max_value
        
        threshold_array = numpy.array(threshold_array)
        width = imgdata.get_image.width
        height = imgdata.get_image.height       
        threshold_matrix = numpy.empty(shape=[width, height])
        j = 0
        k = 0
        for j in range(0,height): #goes through every row
            for i in range(0, width): #for each row, goes through every column
                threshold_matrix[i,j] = threshold_array[k]
                k += 1
        matplotlib.pyplot.figure(1)
        matplotlib.pyplot.subplot(121) # (131) = figure with 1 row, 3 columns, 1st position
        matplotlib.pyplot.imshow(image_matrix)
        matplotlib.pyplot.subplot(122)
        matplotlib.pyplot.imshow(threshold_matrix)
        
        
select_channel()