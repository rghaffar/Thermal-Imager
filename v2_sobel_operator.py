# -*- coding: utf-8 -*-
"""
Sobel operator using scipy shortcut 
Created on Mon Apr  2 14:02:46 2018

@author: Rasa
"""
import matplotlib
import numpy
import scipy
from scipy import ndimage
from scipy import signal
import Module1_getimagedata as imgdata

#Questions for Giovanni: 1) data type - int32 vs float; 2) assert; 3) signal.convolve2d boundary

def sobel(im):
    verbose = True
    im = scipy.misc.imread(im, False, 'L') #https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.imread.html
    im = im.astype('int32')
    if verbose:
        print(str(im[0:10]))
        print(im.size)
        print(im.shape)
    dx = ndimage.sobel(im, 1)  # horizontal derivative
    dy = ndimage.sobel(im, 0)  # vertical derivative
    mag = numpy.hypot(dx, dy)  # magnitude
    mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)

    #matplotlib.pyplot.imshow(mag)
    scipy.misc.imsave('sobel.jpg', mag)
    
    return(mag)
    
def sobel_v2(im, k_size):
    im = scipy.misc.imread(im, False, 'RGB')
    im = im.astype('float')
    #width, height, c = im.shape
    #if c > 1:
    img = 0.2126 * im[:,:,0] + 0.7152 * im[:,:,1] + 0.0722 * im[:,:,2]
    #else:
    #    img = im

    assert(k_size == 3 or k_size == 5);

    if k_size == 3:
        kh = numpy.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype = numpy.float)
        kv = numpy.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype = numpy.float)
    else:
        kh = numpy.array([[-1, -2, 0, 2, 1], 
                   [-4, -8, 0, 8, 4], 
                   [-6, -12, 0, 12, 6],
                   [-4, -8, 0, 8, 4],
                   [-1, -2, 0, 2, 1]], dtype = numpy.float)
        kv = numpy.array([[1, 4, 6, 4, 1], 
                   [2, 8, 12, 8, 2],
                   [0, 0, 0, 0, 0], 
                   [-2, -8, -12, -8, -2],
                   [-1, -4, -6, -4, -1]], dtype = numpy.float)
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve2d.html
    gx = scipy.signal.convolve2d(img, kh, mode='same', boundary = 'symm', fillvalue=0)
    gy = scipy.signal.convolve2d(img, kv, mode='same', boundary = 'symm', fillvalue=0)

    g = numpy.hypot(gx,gy)
    g *= 255.0 / numpy.max(g)

    #matplotlib.pyplot.imshow(g)
    scipy.misc.imsave('sobel_v2.jpg', g)

    return(g)

sobel(imgdata.get_image.image_path)    
sobel_v2(imgdata.get_image.image_path,5)