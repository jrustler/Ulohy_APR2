import pandas as pd
from zak import Zak

class Data_zaku:
    
    def __init__(self,soubor):
        self._soubor = soubor
        
    
    @property 
    def soubor(self):
        return self._soubor


    @soubor.setter
    def soubor(self, value):
        self._soubor = value

    def reset_zaci(self):
        d = pd.DataFrame([],[])
        d.to_excel(self._soubor, index = False)
    
    def vysledky_zaku(self):
        df = pd.read_excel(self._soubor,dtype = str)
        if len(df) !=0:
            for c in df:
                print(str(df[c][0])+" "+str(df[c][1])+" : "+str(df[c][2]))
        else:
            print("zatim zadna data o zacich")
    
    def jaky_zak(self):
        udaje=[0,0,"0"]
        zaci = pd.read_excel(self._soubor)
        st = input("Zadejte sve st:")
        if st not in zaci.columns:
            udaje[0]=input("zadej sve jmeno:")
            udaje[1]=input("zadej sve prijmeni:")
            zaci[st] = udaje
            zaci.to_excel(self._soubor,index = False)
        zak = Zak(st,self._soubor)
        return zak  