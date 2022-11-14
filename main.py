import cv2 as cv
import os
from windowcapture import WindowCapture
from time import time
from vision import findClickPositions

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture('Idle Skilling')

loop_time = time()
while(True):

    screenshot = wincap.get_screenshot()
    #cv.imshow('Computer Vision', screenshot)
    findClickPositions('Next mob arrow.jpg', screenshot, 0.5,'rectangles')
    print('FPS {}'.format(1/(time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
