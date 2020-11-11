""" Modul responsabil cu implementarea clasei de Scriitor. """
from openpyxl import load_workbook


class Scriitor:
    """ Clasa implementeaza functionalitatea de scriere in document excel. """
    def __init__(self):
        """ Initializeaza instanta a clasei Workbook pentru lucrul cu
            documentul excel. """
        self.__workbook = self.__load_template("model")
        self.__sheet = self.__workbook.active
        
    def __load_template(self, name):
        """ Obtine instanta a clasei Workbook pentru modelul de excel dat. """
        return load_workbook(filename="{}.xlsx".format(name))
    
    def save_document(self, nume):
        """ Salveaza documentul in folderul curent folosind numele dat.
            Date de intrare: nume ca string. """
        self.__workbook.save(filename="{}.xlsx".format(nume))

    def test(self):
        """ Completeaza doua valori de test. """
        self.__sheet["A1"] = "Acesta"
        self.__sheet["B1"] = "este un"
        self.__sheet["C1"] = "TEST"


sc = Scriitor()
sc.test()
sc.save_document("test")
