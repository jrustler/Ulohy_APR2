import pandas as pd

class Zak:

    def __init__(self,st,soubor):
        self._st = st
        self._soubor = soubor
        self._df = pd.read_excel(soubor)
     
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
    def df(self):
        return self._df


    @df.setter
    def df(self, value):
        self._df = value
    
    def vypis_jmeno(self):
        print(self.df[self.st][0])
    
    def vypis_prijmeni(self):
        print(self.df[self.st][1])
    
    def vypis_znamky(self):
        print(f"tve znamky jsou: {self.df[self.st][2]}")

    def pridej_znamku(self,znamka):
        if self.df[self.st][2]=="0":
            self.df[self.st][2] = str(znamka)
        else:
            self.df[self.st][2]+=", "+str(znamka)
        self.df.to_excel(self.soubor,index = False)
