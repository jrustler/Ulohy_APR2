from priklad import Priklad
import pandas as pd
class Statistika_u:

    def __init__(self,s_soubor):
        self._s_soubor = s_soubor

    @property 
    def s_soubor(self):
        return self._s_soubor


    @s_soubor.setter
    def s_soubor(self, value):
        self._s_soubor = value
    
    def reset_statistik(self):
        data = [(0,0,0),(0,0,0)]
        d = pd.DataFrame(data,columns=["typ1","typ2","typ3"])
        d.to_excel(self._s_soubor,index=False)
       
    def vypis_statistiky(self):
        statistiky = pd.read_excel(self._s_soubor,dtype=str)
        for typ in statistiky:
            print(str(typ)+" "+str(statistiky[typ][0])+"/"+str(statistiky[typ][1]))
        
    