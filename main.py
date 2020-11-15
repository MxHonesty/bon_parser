""" Modulul principal. """
from Bon.bon import Bon
from excel.scriitor import Scriitor
from processor import Processor
import os

def run():
    scriitor = Scriitor()
    pro = Processor()

    for filename in os.listdir("img"):
        data = pro.get_data("img\\{}".format(filename))
        try:
            bon = Bon(data["Place"][0], data["Receipt Number"][0], data["Preturi"],
                    data["Bunuri"], data["Amount"][0], data["Date"][0])
            scriitor.scrie_bon(bon, filename.split(".")[0])
        except ValueError:
            print("Bonul nu este valid!")
        except IndexError:
            print("Nu poate fi inteleasa imaginea!")


run()
