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
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        return gray
