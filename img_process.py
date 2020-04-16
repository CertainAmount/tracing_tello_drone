import numpy as np
import cv2
from skimage.color import rgb2gray
from PIL import Image
from StringIO import StringIO
from scipy import ndimage
import base64
import time

def get_coords(fpath):
    "Reads in a base64 encoded image, filters for red, and then calculates the center of the red"
    # convert the base64 encoded image a numpy array

    image = cv2.imread(fpath)
    result = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # create lower and upper bounds for red
    red_lower = np.array([155, 25, 0])
    red_upper = np.array([179, 255, 255])

    # perform the filtering. mask is another word for filter
    mask = cv2.inRange(image, red_lower, red_upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    # convert the image to grayscale, then calculate the center of the red (only remaining color)
    output_gray = rgb2gray(output)
    y, x = ndimage.center_of_mass(output_gray)

    cv2.imshow('image', result)
    cv2.waitKey(0)
    cv2.imshow('image', output_gray)
    cv2.waitKey(0)

    data = {
        "x": x,
        "y": y,
        "xmax": output_gray.shape[1],
        "ymax": output_gray.shape[0],
        "time": time.time()
    }
    return data