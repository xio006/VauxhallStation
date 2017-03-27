import cv2 as cv
import filters
import numpy as np
import sys
import glob
import multiprocessing


_src = cv.imread("./standard/circles-eight.jpg")
eight_pancakes = cv.resize(_src,(0,0),fx = 0.2, fy = 0.2)

_src = cv.imread("./demo-images/multiple3-cropped.jpg")
chain_tiles_1 = cv.resize(_src,(0,0),fx=0.5,fy=0.5)


def display_img(img):
    cv.imshow("Display Window",img)
    cv.waitKey(0)

#filters.recolorRC(chain_tiles_1,chain_tiles_1)
#filters.recolorRGV(chain_tiles_1,chain_tiles_1)
#filters.recolorCMV(chain_tiles_1,chain_tiles_1)
#CurveFilter = filters.BGRPortraCurveFilter()
#CurveFilter.apply(chain_tiles_1,chain_tiles_1)
#filters.strokeEdges(chain_tiles_1,chain_tiles_1,3,5)




display_img(chain_tiles_1)
