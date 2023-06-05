class Priklad:

    def __init__(self,zneni,vysledek):
        self._zneni = zneni
        self._vysledek = vysledek
        self._uspesnost = "zatím nic"


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

    def vypis_a_zkontroluj(self):
        odpoved=input(self.zneni)
        if odpoved == str(self.vysledek):
            self.uspesnost = "správně"
        else:
            self.uspesnost = "špatně"
        print(self.uspesnost)
