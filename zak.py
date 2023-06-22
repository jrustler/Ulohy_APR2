import pandas as pd

class Zak:

    def __init__(self,st,soubor):
        self._st = st
        self._soubor = soubor
        self._df = pd.read_excel(soubor,dtype = str)
     
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
        print(self._df[self._st][0])
    
    def vypis_prijmeni(self):
        print(self._df[self._st][1])
    
    def vypis_znamky(self):
        print(f"tve znamky jsou: {self._df[self._st][2]}")
    
    def vypis_prumer(self):
        seznam =[int(i) for i in self.df[self._st][2].split(", ")]
        prumer = sum(seznam)/len(seznam)
        print(f"tvůj průměr je {prumer}")

    def pridej_znamku(self,znamka):
        if self._df[self._st][2]=="0":
            self_.df[self._st][2] = str(znamka)
        else:
            self._df[self._st][2]+=", "+str(znamka)
        self._df.to_excel(self._soubor,index = False)
