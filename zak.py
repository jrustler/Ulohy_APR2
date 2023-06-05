import pandas as pd

class Zak:

    def __init__(self,st,soubor):
        self._st = st
        self._soubor = pd.read_excel("zaci.xlsx")
        self._jmeno = self._soubor[st][0]
        self._prijmeni = self._soubor[st][1]
        self._znamky = self._soubor[st][2]
     
    @property 
    def st(self):
        return self._st


    @st.setter
    def st(self, value):
        self._st = value
    
    @property 
    def soubor(self):
        return self._soubor


    @soubor.setter
    def soubor(self, value):
        self._soubor = value
    
    @property 
    def jmeno(self):
        return self._jmeno


    @jmeno.setter
    def jmeno(self, value):
        self._jmeno = value
    
    @property 
    def prijmeni(self):
        return self._prijmeni


    @prijmeni.setter
    def prijmeni(self, value):
        self._prijmeni = value
    
    @property 
    def znamky(self):
        return self._znamky


    @znamky.setter
    def znamky(self, value):
        self._znamky = value

