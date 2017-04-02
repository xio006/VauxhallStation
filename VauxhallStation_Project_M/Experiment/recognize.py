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

def read_and_resize(img_path,resize_perc):
    """read image from image_path and resize proportionally by resize_perc
    resize perc takes a decimal number"""
    _src = cv.imread(img_path)
    res = cv.resize(_src,(0,0),fx=resize_perc,fy=resize_perc)
    return res

eight_pancakes = read_and_resize("./pic/standard/circles-eight.jpg",0.2)
chain_tiles_1 = read_and_resize("./pic/demo-images/multiple3.jpg",0.2)

gray = cv.cvtColor(chain_tiles_1, cv.COLOR_RGB2GRAY)
#gray = cv.bilateralFilter(gray, 11, 17, 17)
gray = cv.GaussianBlur(gray, (5, 5), 0)
_res = None
#threshold = cv.adaptiveThreshold(gray, 255, 1, 1, 11, 2)
edged = cv.Canny(gray, 10, 30, _res, 3, True)

display_img(edged)
(_,cnts, _) = cv.findContours(edged.copy(), mode = cv.RETR_LIST,  method = cv.CHAIN_APPROX_TC89_L1)
cnts = sorted(cnts, key = cv.contourArea, reverse = True)[:10]

cv.drawContours(chain_tiles_1,cnts,-1,(0,255,0),3)
display_img(chain_tiles_1)

