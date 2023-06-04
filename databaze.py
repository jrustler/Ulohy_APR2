class Databaze:
    
    def __init__(self,soubor):
        self._soubor = soubor
        self._typ1 = [line[2:-1] for line in open(self._soubor,"rt") if line[0]=="1"]
        self._typ2 = [line[2:-1] for line in open(self._soubor,"rt") if line[0]=="2"]
        self._typ3 = [line[2:-1] for line in open(self._soubor,"rt") if line[0]=="3"]
    @property 
    def soubor(self):
        return self._soubor


    @soubor.setter
    def soubor(self, value):
        self._soubor = value
    
    @property 
    def typ1(self):
        return self._typ1


    @typ1.setter
    def soubor(self, value):
        self._typ1 = value
    
    @property 
    def typ2(self):
        return self._typ2


    @typ2.setter
    def soubor(self, value):
        self._typ2 = value
    
    @property 
    def typ3(self):
        return self._typ3


    @typ3.setter
    def soubor(self, value):
        self._typ3 = value
    
a=Databaze("priklady1.txt")
print(a.typ1,a.typ2,a.typ3)
