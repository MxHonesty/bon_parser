""" Modul de test pentru data. """
from data import Data

def test():
    """ Functia principala de test. """
    data = Data(["214"], ["24/02/2020"], ["RO123123"], ["Bucuresti"], ["2,5", "2,6"], ["Cola", "Dorna"])
    assert Data.is_empty([""]) 
    assert Data.is_empty([])
    assert not Data.is_empty(["215"])
    assert data.get_completa()

test()
