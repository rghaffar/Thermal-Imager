
"""
Module 1: 
    Opens image and saves image data to text file
    Creates R,G,B, and greyscale arrays and matrices

@author: Rasa
"""
from PIL import Image # PIL = python image library
import numpy

def get_image(): #returns image data, including list of pixel data, image size, and image mode
    get_image.image_path = input("What is your file name? ") + '.jpg'
    #PIL function that opens and reads image
    get_image.image = Image.open(get_image.image_path, 'r') 
    #Nestled list of pixel values (e.g. [(0,1,0)],(0,2,1),(1,3,2)]) 
    get_image.pixel_values = list(get_image.image.getdata())
    #PIL function that obtains pixel width and height
    get_image.width, get_image.height = get_image.image.size 
    get_image.image_size = get_image.width*get_image.height
    get_image.mode = get_image.image.mode
    
    #write image data to new text file
    line1 = "Image size: " + str(get_image.image_size) 
    line2 = "Image width: " + str(get_image.width) 
    line3 = "Image height: " + str(get_image.height)
    line4 = "Image mode: " + str(get_image.mode) 
    imgdata = open("image_data",'w')
    imgdata.write(line1 + '\n')
    imgdata.write(line2 + '\n')
    imgdata.write(line3 + '\n')
    imgdata.write(line4)
    imgdata.close()
    
    return(get_image.pixel_values,get_image.width,get_image.height,get_image.image_size, get_image.image_path)
    
def flatten_image(): # Flattens nestled list of pixel values
    get_image()
    verbose = False 
    flatten_image.flatten_pixels = []
    sublist = 0
    item = 0
    for sublist in get_image.pixel_values:
        for item in sublist:
            flatten_image.flatten_pixels.append(item)
    if verbose:
        print("Flattened array: " + str(flatten_image.flatten_pixels[0:12]))
    return(flatten_image.flatten_pixels)

def array(): #Creates 1D arrays for each channel (R,G,B, greyscale)
    verbose = False
    flatten_image()
    array.r = flatten_image.flatten_pixels[0:len(flatten_image.flatten_pixels):3] # [start:end:increment]
    array.g = flatten_image.flatten_pixels[1:len(flatten_image.flatten_pixels):3]
    array.b = flatten_image.flatten_pixels[2:len(flatten_image.flatten_pixels):3]
    
    #Convert list into numpy array in order to perform operations and convert into matrix
    array.r = numpy.array(array.r) 
    array.g = numpy.array(array.g)
    array.b = numpy.array(array.b)
    
    #Convert values into greyscale
    red_to_grey = array.r*0.2126
    green_to_grey = array.g*0.7152
    blue_to_grey = array.b*0.0722
    array.grey = red_to_grey + green_to_grey + blue_to_grey
    if verbose:
        print ("Greyscale array test: " + str(array.grey[0:4]))
    #Save to CSV test
    numpy.savetxt("redarray.csv", array.r, delimiter=",")
    return(array.r, array.g, array.b, array.grey)
    
def matrix(): #Creates 2D matrices for each channel (R,G,B, greyscale)
    #initialize matrix
    matrix.r = numpy.empty(shape=[get_image.width, get_image.height]) 
    matrix.g = numpy.empty(shape=[get_image.width, get_image.height])
    matrix.b = numpy.empty(shape=[get_image.width, get_image.height])
    matrix.grey = numpy.empty(shape=[get_image.width, get_image.height])
    
    j = 0
    k = 0
    for j in range(0,get_image.height): #goes through every row
        for i in range(0, get_image.width): #for each row, goes through every column
            matrix.r[i, j] = array.r[k] #for each [row,column] value, inserts index k from initial array
            matrix.g[i, j] = array.g[k]
            matrix.b[i, j] = array.b[k]
            matrix.g[i,j] = array.grey[k]
            k += 1
    #Save to CSV test
    numpy.savetxt("redmatrix.csv", matrix.r, delimiter=",")
    return(matrix.r, matrix.b, matrix.g, matrix.grey)
    
array()
matrix()
    


