import pywt
import cv2 as cv
import numpy as np

def w2d(img, mode='haar', level=1):
    imArray = img
    
    imArray = cv.cvtColor(imArray, cv.COLOR_RGB2GRAY)
    imArray = np.float32(imArray)
    
    imArray /= 255
    coeffs = pywt.wavedec2(imArray, mode, level)
    
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0
    
    imArray_H = pywt.waverec2(coeffs_H, mode)
    imArray_H *= 255
    imArray_H = np.uint8(imArray_H)
    
    return imArray_H