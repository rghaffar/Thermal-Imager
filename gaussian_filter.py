# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 15:45:15 2018

@author: Rasa
"""

import matplotlib
import numpy
import scipy
from scipy import ndimage
from scipy import signal
import Module1_getimagedata as imgdata

def gaussian(im, sigma):
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.imread.html
    im = scipy.misc.imread(im, False, 'L') 
    im = im.astype('float')
    img = scipy.ndimage.filters.gaussian_filter(im, sigma, order=0, output=None, mode='reflect', cval=0.0, truncate=4.0)
    scipy.misc.imsave('gaussian.jpg', img)
    return(img)
    
gaussian(imgdata.get_image.image_path,2)