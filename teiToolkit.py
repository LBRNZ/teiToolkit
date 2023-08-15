import teiConverter
import teiCleaner
class teiToolkit(object):

    def __init__(self):
        inputInfo = "Welche Funktion soll aufgerufen werden? \n\n 1) tei Konverter. \n\n 2) tei Cleaner. \n\n Bitte Zahl eingeben und Enter druecken >>>>> "
        self.the_route = input(inputInfo)

        if self.the_route == '1':
                teiConverter.__init__(self)
        elif self.the_route == '2':
                teiCleaner.__init__(self)
        else: print("Fehlerhafte Eingabe")

teiToolkit();