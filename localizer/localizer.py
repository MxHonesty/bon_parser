""" Modul responsabil pentru implementarea clasei Localizer. """
import cv2
import numpy as np
import imutils
from skimage.filters import threshold_local
from PIL import Image


class Localizer:
    """ Clasa care se ocupa cu procesarea imaginii. 
        https://github.com/muratlutfigoncu. """
    @staticmethod
    def localize_image(img):
        """ Clasa proceseaza imaginea data. 
            Date de intrare: Image img.
            Dade de iesire: Image. """
        #img = Localizer.scale_image(img)  # scalam imaginea
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale
        #gray = Localizer.remove_noise_and_smooth(gray)
        #cv2.imshow('image',img)
        #k = cv2.waitKey(0)
        return gray

    @staticmethod
    def scale_image(img):
        """ Aduce imaginea la dimensiunile ideale. 
            Date de intrare: imaginea initiala.
            Date de iesire: imaginea scalata. """
        img = Image.fromarray(img)
        length_x = img.height  
        width_y = img.width
        factor = min(1, float(1024.0 / length_x))
        size = int(factor * length_x), int(factor * width_y)
        img = np.asarray(img)
        img_resized = cv2.resize(img, size, Image.ANTIALIAS)
        return img_resized

    @staticmethod
    def remove_noise_and_smooth(img):
        """ Elimina noise din imagine. 
            Date de intrare: img.
            Date de iesire: imaginea preprocesata. """
        filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 41)
        kernel = np.ones((1, 1), np.uint8)
        opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        or_image = cv2.bitwise_or(img, closing)
        return or_image
