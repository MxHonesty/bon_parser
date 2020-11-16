""" Modulul principal. """
from Bon.bon import Bon
from excel.scriitor import Scriitor
from processor import Processor
from localizer.localizer import Localizer
import cv2
import os

def run():
    scriitor = Scriitor()
    pro = Processor()

    for filename in os.listdir("img"):
        img = cv2.imread("img\\{}".format(filename))  # Img instanta Image
        # TODO daca nu se gasesc produse prin metoda clasica incearca cu grayscale. 
        data = pro.get_data(img)
        if not data.get_completa():
            print("reincercare")
            img = Localizer.localize_image(img)  # Aplicam localizarea imaginii
            new_data = pro.get_data(img)
            data.umplere_date(new_data)
        try:
            bon = Bon(data.get_place(), data.get_receipt(), data.get_preturi(),
                      data.get_bunuri(), data.get_amount(), data.get_date())
            scriitor.scrie_bon(bon, filename.split(".")[0])
        except ValueError:
            print("Bonul nu este valid!")
        except IndexError:
            print("Nu poate fi inteleasa imaginea!")


run()
