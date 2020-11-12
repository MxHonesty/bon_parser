""" Modul responsabil cu implementarea clasei de Scriitor. """
from openpyxl import load_workbook
from Bon.bonValidator import ValidatorBon

class Scriitor:
    """ Clasa implementeaza functionalitatea de scriere in document excel. """
    def __init__(self):
        """ Initializeaza instanta a clasei Workbook pentru lucrul cu
            documentul excel. """
        self.__workbook = self.__load_template("model")
        self.__sheet = self.__workbook.active
        
        self.__pozitie_data = ["G4", "H4", "I4"]
        self.__pozitie_total = ["K7"]
        self.__pozitie_informatii = ["B2"]
        self.__pozitie_produse = ["C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16"]
        
    def __load_template(self, name):
        """ Obtine instanta a clasei Workbook pentru modelul de excel dat. """
        return load_workbook(filename="excel\\{}.xlsx".format(name))
    
    def __save_document(self, nume):
        """ Salveaza documentul in folderul curent folosind numele dat.
            Date de intrare: nume ca string. """
        self.__workbook.save(filename="documents\{}.xlsx".format(nume))

    def scrie_bon(self, bon, filename):
        """ Metoda creeza documentul aferent bonului dat. 
            Date de intrare: instanta valida a clasie bon. 
            Raises ValueError daca bonul nu este valid. """
        if ValidatorBon.validare_bon(bon):
            self.__scrie_pozitie(self.__pozitie_data[0], int(bon.get_data()[:2]))
            self.__scrie_pozitie(self.__pozitie_data[1], int(bon.get_data()[3:5]))
            self.__scrie_pozitie(self.__pozitie_data[2], int(bon.get_data()[6:]))
            self.__scrie_pozitie(self.__pozitie_informatii[0], "UNITATEA: {}\nCod fiscal: {}".format(bon.get_firma(),
                                                                                                     bon.get_cif()))
            self.__scrie_pozitie(self.__pozitie_total[0], float(bon.get_pret_total()))
            for poz_el, el in enumerate(bon.get_preturi()):
                self.__scrie_pozitie(self.__pozitie_produse[poz_el], el)
            self.__save_document(filename)
        else:
            raise ValueError("Bon invalid!")
            
    def __scrie_pozitie(self, pozitie, text):
        """ Functia scrie text pe pozitia pozitie din document.
            Cei doi paramentrii sunt primiti ca string-uri. """
        self.__sheet[pozitie] = text
        
    def test(self):
        """ Completeaza doua valori de test. """
        self.__sheet["A1"] = "Acesta"
        self.__sheet["B1"] = "este un"
        self.__sheet["C1"] = "TEST"

# DATA: zi: G4, luna: H4, Anul I4
# Total: K7
# Produse C[7-16]
