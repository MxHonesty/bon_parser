""" Modul responsabil pentru implementarea clasei Localizer. """
import pytesseract as pt
import cv2


class Localizer:
    """ Clasa care se ocupa cu obtinerea textului din imaginea data. """
    def __init__(self, img):
        """img - imaginea: cv2.imread(path)"""
        pt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        self.__results = pt.image_to_data(img, output_type=pt.Output.DICT)
        self.__text_results = pt.image_to_string(img, output_type=pt.Output.DICT)
        self.__min_confidence = 0  # increderea minima in rezultat.
        self.__medie_confidence = self.__determina_media_confidence()

    def set_min_confidence(self, new_min):
        """ Setter pentru atributul __min_confidence. """
        self.__min_confidence = new_min

    def get_min_confidence(self):
        """ Getter pentru atributul __min_confidence. """
        return self.__min_confidence

    def get_medie_confidence(self):
        """ Getter pentru atributul _medie_confidence. """
        return self.__medie_confidence

    def get_text(self):
        """ Metoda returneaza textul care a fost determinat cu un scor de confidence
            mai mare decat __min_confidence. """
        text_complet = ""
        rez_dict = self.__results
        for i in range(0, len(rez_dict["text"])):
            text = rez_dict["text"][i]
            conf = int(rez_dict["conf"][i])
            if conf >= self.__min_confidence:
                text_complet += text + " "
        return text_complet

    def get_results(self):
        return self.__text_results

    def __determina_media_confidence(self):
        """ Functia determina scorul de confidence mediu pentru textul dat.
            Date de intrare: results, rezultatul metodei image_to_data.
            Date de iesire: media ca float. """
        media = 0
        nr = 0
        for el in self.__results['conf']:
            media += int(el)
            nr += 1
        media /= nr
        return media


img = cv2.imread("bon2.jpg")
loc = Localizer(img)
loc.set_min_confidence(50)
text = loc.get_text()
print(text)

print("===========================")
print(loc.get_medie_confidence())
results = loc.get_results()
print("===============")
print(results)
