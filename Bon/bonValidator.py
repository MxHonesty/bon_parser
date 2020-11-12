""" Modulul responsabil pentru implementarea clasie de validare pentru Bon. """


class ValidatorBon:
    """ Clasa de validare pentru Bon. """

    @staticmethod
    def validare_bon(bon):
        """ Metoda valideaza un bon.
            Date de intrare: instanta a clasei Bon.
            Date de iesire: True daca bonul este valid, False altfel. """
        cif = bon.get_cif()
        firma = bon.get_firma()
        data = bon.get_data()
        pret_total = bon.get_pret_total()
        lista_preturi = bon.get_preturi()
        
        lista_completa = True
        if len(lista_preturi) == 0:
            lista_completa = False
        for el in lista_preturi:
            if not ValidatorBon.este_string_valid(el):
                lista_completa = False
                break
                
        if ValidatorBon.este_string_valid(cif) and ValidatorBon.este_string_valid(firma)\
            and ValidatorBon.este_string_valid(data) and ValidatorBon.este_string_valid(pret_total)\
                and lista_completa:
            return True
        
        return False

    @staticmethod
    def este_string_valid(text):
        """ Determina daca valoarea data este un string nevid. 
            Returneaza True daca valoarea text este un string nevid,
            False altfel."""
        if isinstance(text, str):
            if text == "":
                return False
        else:
            return False
        return True
