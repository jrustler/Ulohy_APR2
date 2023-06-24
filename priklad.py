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
        s = open("statistika_uloh.txt","rt")
        data = s.read()
        typy = {"správně":{"typ1":[7,10,9,1],"typ2":[18,21,20,1],"typ3":[29,32,31,1]},"špatně":{"typ1":[7,10,9,0],"typ2":[18,21,20,0],"typ3":[29,32,31,0]}}
        for o in typy.keys():
            if o == self._uspesnost:
                data = data.replace(data[typy[o][self._typ][0]:typy[o][self._typ][1]],str(int(data[typy[o][self._typ][0]])+int(typy[o][self._typ][3]))+"/"+str(int(data[typy[o][self._typ][2]])+1),1)
        s.close()
        s = open("statistika_uloh.txt","wt")
        s.write(data)
        s.close()