# -*- coding: utf-8 -*-
"""
Module 5: Apply image-smoothing filters
Created on Fri Mar 30 10:10:14 2018

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
            mean_filter(imgdata.matrix.r)
        if channel == 'green':
            mean_filter(imgdata.matrix.g)
        if channel == 'blue':
            mean_filter(imgdata.matrix.b)
        if channel == 'b/w':
            mean_filter(imgdata.matrix.grey)
    else:
        print('Please enter valid channel option')
    return(select_channel.channel)


#Mean filtering using n x n kernels - spot reduction
def mean_filter(image_matrix):    
    verbose = False
    grid_size = int(input('Select a kernel size (odd number > 2): '))
    
    if grid_size < 2 or grid_size % 2 == 0:
        print("Invalid grid size")
        return
    
    width = imgdata.get_image.width
    height = imgdata.get_image.height 
    filtered_image_matrix = numpy.empty(shape=[width, height])
    for j in range(0,height): #goes through every row
        for i in range(0, width): #for each row, goes through every column
            filtered_image_matrix[i,j] = image_matrix[i,j]   
    
    for j in range(0+(int(grid_size/2)), height-(int(grid_size/2))):
        for i in range(0+(int(grid_size/2)), width-(int(grid_size/2))):
            sum = 0
            for x in range(i-(int(grid_size/2)),i+(int(grid_size/2))+1):
                for y in range(j-(int(grid_size/2)),j+(int(grid_size/2))+1):
                    if verbose:
                        print(str(x) + ', ' + str(y))
                    if x >= 0 and y >= 0:
                        sum = sum + filtered_image_matrix[x,y]
            filtered_image_matrix[i,j] = sum/(grid_size*grid_size) #Indented by one tab
            if verbose:
                print('---')
        
    matplotlib.pyplot.figure(1)
    matplotlib.pyplot.subplot(121) # (131) = figure with 1 row, 3 columns, 1st position
    matplotlib.pyplot.imshow(image_matrix)
    matplotlib.pyplot.subplot(122)
    matplotlib.pyplot.imshow(filtered_image_matrix)
    
select_channel()