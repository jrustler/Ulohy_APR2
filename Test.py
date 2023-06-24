
class Test:

    def __init__(self,format,databaze,priklady=[]):
        self._format = format
        self._databaze = databaze
        self._priklady = []

    
    @property 
    def format(self):
        return self._format


    @format.setter
    def format(self, value):
        self._format = value

    @property 
    def databaze(self):
        return self._databaze


    @databaze.setter
    def databaze(self, value):
        self._databaze = value
    
    @property 
    def priklady(self):
        return self._priklady


    @priklady.setter
    def priklady(self, value):
        self._priklady = value

    def pridej_priklad(self,priklad):
        self._priklady.append(priklad)
    
    def spust_test(self):
        body = 0
        for p in self._priklady:
            p.vypis_a_zkontroluj()
            p.zapis_do_statistik()
            if p.uspesnost == "správně":
                body+=1
        return body

    