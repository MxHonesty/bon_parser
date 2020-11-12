""" Modul de test pentru Bon si validator. """

from bon import Bon
from bonValidator import ValidatorBon

#def __init__(self, firma, cif, preturi, pret_total, data):
def test():
    b_bun = Bon("firma", "cif", ["213", "213"], "214,124", "24/02/2020")
    b_rau = Bon("", "salut", [], "123", "24/02")
    b_rau2 = Bon("firma", "cif", [], "214,124", "24/02/2020")
    
    assert ValidatorBon.validare_bon(b_bun)
    assert not ValidatorBon.validare_bon(b_rau)
    assert not ValidatorBon.validare_bon(b_rau2)


if __name__ == "__main__":
    test()
