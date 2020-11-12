""" Modulul responsabil pentru extragerea datelor semnificative din text. """


class Bon:
    """ Determina detaliile semnificative din imagine. """
    def __init__(self):
        # TODO de primit text sau resuts?
        self.__firma = ""
        self.__cif = ""
        self.__preturi = []
        self.__pret_total = 0
        self.__data = ""
        
