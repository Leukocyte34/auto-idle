import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname((os.path.abspath(__file__))))

def findClickPositions(needle_img_path, fightscreen_img, threshold = 0.5, debug_mode=None):
    needle_img = cv.imread(needle_img_path,  cv.IMREAD_UNCHANGED)

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(fightscreen_img, needle_img, method)

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), (needle_w), (needle_h)]
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

    points = []

    if len(rectangles):

        line_color = (0,255,0)
        line_type = cv.LINE_4
        marker_color = (255 ,0 ,255)
        marker_type = cv.MARKER_CROSS

        for x, y, w, h in rectangles:
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            points.append((center_x, center_y))

            if debug_mode == 'rectangles':

                top_left = x, y
                bottom_right = (x + w), (y + h)

                cv.rectangle(fightscreen_img, (int(top_left[0]), int(top_left[1])), (int(bottom_right[0]), int(bottom_right[1])),line_color,line_type)

            elif debug_mode == 'points':
                cv.drawMarker(fightscreen_img, center_x, center_y, marker_color, marker_type)


    if debug_mode:
        cv.imshow('Matches', fightscreen_img)
        #cv.waitKey()

    return points
'''
points = findClickPositions('Next mob arrow.jpg',
                            'C:\\Users\\gianp\\Documents\\Python Learning projects\\IdleSkilling Bot\\Images\\Fighting Screen2.png',
                            debug_mode='rectangles')
points = findClickPositions('Next mob arrow.jpg',
                            'C:\\Users\\gianp\\Documents\\Python Learning projects\\IdleSkilling Bot\\Images\\Fighting Screen2.png',
                            debug_mode='points')
print(points)
print('Done.')
'''
