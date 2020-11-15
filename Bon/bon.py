""" Modulul responsabil pentru extragerea datelor semnificative din text. """


class Bon:
    """ Determina detaliile semnificative din imagine. """
    def __init__(self, firma, cif, preturi, bunuri, pret_total, data):
        """ Constructor primeste firma, cif, pret_total, data ca string,
            preturi ca lista de string-uri."""
        self.__firma = firma
        self.__cif = cif
        self.__preturi = self.__formatare_lista_produse(preturi)
        self.__bunuri = bunuri
        self.__pret_total = self.__formatare_pret(pret_total)
        self.__data = self.__formatare_data(data)
        print(bunuri)
        
    def __formatare_data(self, data):
        """ Formateaza data in functie de modul in care este scrisa. """
        if "data:" in data:
            data = data[5:]
            data = data.replace(" ", "")
            data = data[:10]
        return data
        
    def __formatare_lista_produse(self, lista):
        """ Formatarea listei de produse. 
            Date de intrare: lista de produse. """
        new_list = []
        for el in lista:
            if "=" in el:
                el = el.split("=")[0]
            new_list.append(el)
        return new_list
        
    def __formatare_pret(self, total):
        if "total lei " in total:
            total = total[10:]
            total = total.replace(" ", "")
        if "total " in total:
            total = total[6:]
            total = total.replace(" ", "")
        if "le!" in total:
            total = total.replace("le!", "")
        return total
    
    def get_bunuri(self):
        """ Returneaza lista de bunuri. """
        return self.__bunuri
            
    def get_firma(self):
        """ Returneaza numele firmei. """
        return self.__firma
        
    def get_cif(self):
        """ Returneaza cif-ul. """
        return self.__cif
        
    def get_preturi(self):
        """ Returneaza lista de preturi. """
        return self.__preturi
    
    def get_pret_total(self):
        """ Returneaza pretul total. """
        return self.__pret_total
        
    def get_data(self):
        """ Returneaza data. """
        return self.__data
        
    def __str__(self):
        return str(self.__firma) + " " + str(self.__cif) + " " + str(self.__pret_total) + " " + str(self.__data)
