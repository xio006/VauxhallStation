import cv2 as cv
import filters
import numpy as np
import sys
import glob
import multiprocessing


def display_img(img):
    """Display image and wait for enter key to close the window"""
    cv.imshow("Display Window",img)
    cv.waitKey(0)

def read_and_resize_to_min_height(directory):
    imgs = []
    imgpaths = []
    heights = []

    """Step 1: get the minimum height from all images"""
    for _imgpath in glob.glob(directory):
        _src = cv.imread(_imgpath)
        height, width, channels = _src.shape 
        heights.append(height)
        imgs.append(_src)
        imgpaths.append(_imgpath)
    min_height = min(heights)

    """Step 2: resize all images to the same height proportionally 
               then get the minimum width of all images after the resize"""
    widths = []
    for i,_img in enumerate(imgs):
        height = _img.shape[0]
        resize_perc = float(min_height)/float(height)
        imgs[i] = cv.resize(_img,(0,0),fx=resize_perc,fy=resize_perc)
        width = imgs[i].shape[1]
        widths.append(width)

    """Step 3: resize all images to the same width (the min width) from the center of the image
               write the resulting image to a file"""
    min_width = min(widths)
    for i,_img in enumerate(imgs):
        width = _img.shape[1]
        height = _img.shape[0]
        x = int(float(width - min_width)/2)
        _res = _img[0:height,x:(min_width+x)]
        imgs[i] = _res
        cv.imwrite(imgpaths[i].replace("_chopped","_cropped"),imgs[i])

directory = "./pic/demo_photo_std1_chopped/*.png"
read_and_resize_to_min_height(directory)

