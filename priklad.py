import pandas as pd

class Priklad:

    def __init__(self,zneni,vysledek,typ):
        self._zneni = zneni
        self._vysledek = vysledek
        self._uspesnost = "zatím nic"
        self._typ = typ


    @property 
    def zneni(self):
        return self._zneni


    @zneni.setter
    def zneni(self, value):
        self._zneni = value

    @property 
    def vysledek(self):
        return self._vysledek


    @vysledek.setter
    def vysledek(self, value):
        self._vysledek = value
    
    @property 
    def uspesnost(self):
        return self._uspesnost


    @uspesnost.setter
    def uspesnost(self, value):
        self._uspesnost = value

    @property 
    def typ(self):
        return self._typ


    @typ.setter
    def typ(self, value):
        self._typ = value

    def vypis_a_zkontroluj(self):
        self._uspesnost = "správně" if input(self._zneni + " \nzadej vysledek: ") == str(self._vysledek) else "špatně"
        print(self._uspesnost)
    

    def zapis_do_statistik(self):
        statistika = pd.read_excel("statistika_uloh.xlsx",dtype = str)
        if self._uspesnost == "správně":
            statistika[self._typ][0] = int((statistika[self._typ][0]))+1
            statistika[self._typ][1] = int(statistika[self._typ][1])+1
        else:
            statistika[self._typ][1] = int(statistika[self._typ][1])+1
        statistika.to_excel("statistika_uloh.xlsx",index = False)




