""" Modul responsabil pentru implementarea clasei Data. """

class Data:
    """ Clasa care stocheaza infromatiile extrase dintr-o imagine. """
    def __init__(self, amount, date, receipt, place, preturi, bunuri):
        """ Constructorul primeste cate o lista pentru fiecare membru.
            Completa este True daca toate campurile au cel putin cate o valoare. """
        self.__amount = Data.__parse_data(amount)
        self.__date = date
        self.__receipt = Data.__parse_data(receipt)
        self.__place = [Data.__parse_data(place)[0]]
        self.__preturi = Data.__parse_data(preturi)
        self.__bunuri = Data.__parse_data(bunuri)
        self.__completa = self.__este_valid()

    def get_amount(self):
        if Data.is_empty(self.__amount): 
            return ""
        return self.__amount[0]

    def get_date(self):
        print(self.__date)
        if Data.is_empty(self.__amount): 
            return ""
        return self.__date[0]

    def get_receipt(self):
        if Data.is_empty(self.__amount): 
            return ""
        return self.__receipt[0]

    def get_place(self):
        print(self.__place[0])
        if Data.is_empty(self.__amount): 
            return ""
        return self.__place[0]

    def get_preturi(self):
        if Data.is_empty(self.__amount): 
            return [""]
        return self.__preturi

    def get_bunuri(self):
        if Data.is_empty(self.__amount): 
            return [""]
        return self.__bunuri

    def get_completa(self):
        return self.__completa
        
    def print_data(self):
        print(self.__amount)
        print(self.__place)
        print(self.__receipt)
        print(self.__bunuri)
        print(self.__preturi)

    def umplere_date(self, new_data):
        """ Completeaza campurile goale cu cele din new_data.
            Date de intrare: instanta Data new_data. """
        if Data.is_empty(self.__amount):
            self.__amount = Data.__parse_data([new_data.get_amount()])
        if Data.is_empty(self.__date):
            self.__date = Data.__parse_data([new_data.get_date()])
        if Data.is_empty(self.__receipt):
            self.__receipt = Data.__parse_data([new_data.get_receipt()])
        if Data.is_empty(self.__place):
            self.__place = Data.__parse_data([new_data.get_place()])
        if Data.is_empty(self.__preturi):
            self.__preturi = new_data.get_preturi()
        if Data.is_empty(self.__bunuri):
            self.__bunuri = Data.__parse_data(new_data.get_bunuri())
        self.__completa = self.__este_valid()


    def __este_valid(self):
        """ Functia determina daca campurile au cel putin cate o valore. """
        valid = True
        if Data.is_empty(self.__amount):
            valid = False
        if Data.is_empty(self.__date):
            valid = False
        if Data.is_empty(self.__receipt):
            valid = False
        if Data.is_empty(self.__place):
            valid = False
        if Data.is_empty(self.__preturi):
            valid = False
        if Data.is_empty(self.__bunuri):
            valid = False
        return valid

    @staticmethod
    def is_empty(field):
        """ Determina daca un camp este gol.
            Date de iesire: True daca este gol. False Altfel. """
        return field is None or (len(field) == 1 and field[0] == "") or len(field) == 0

    @staticmethod
    def __parse_data(list):
        """ Editeaza lista transmisa eliminand un set de caractere. """
        for poz, el in enumerate(list):
            el = el.replace("@", "")
            el = el.replace("-", "")
            el = el.replace("|", "")
            el = el.replace("_", "")
            el = el.replace("©", "")
            el = el.replace("\"", "")
            el = el.replace("-", "")
            el = el.replace("`", "")
            list[poz] = el
        return list
