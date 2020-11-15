""" Modul responsabil pentru implementarea clasei Localizer. """
import cv2
import numpy as np
import imutils
from skimage.filters import threshold_local


class Localizer:
    """ Clasa care se ocupa cu procesarea imaginii. 
        https://github.com/muratlutfigoncu. """
    @staticmethod
    def localize_image(img):
        """ Clasa proceseaza imaginea data. 
            Date de intrare: Image img.
            Dade de iesire: Image. """
    	# load the image
        ratio 	= img.shape[0] / 500.0
        orig 	= img.copy()


    	# convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    	# show the output images
        cv2.imshow("Original", 	imutils.resize(orig, 	height = 650))
        cv2.imshow("Output", 	imutils.resize(gray,	height = 650))

    	# Waits for a key insert to close images.
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        return gray
