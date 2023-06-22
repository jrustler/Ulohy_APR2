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
        odpoved=input(self._zneni + " \nzadej vysledek: ")
        s = open("statistika_uloh.txt","rt")
        data = s.read()
        if odpoved == str(self._vysledek):
            self._uspesnost = "správně"
            if self._typ == "typ1":
                    data = data.replace(data[7:10],str(int(data[7])+1)+"/"+str(int(data[9])+1),1)
            if self._typ == "typ2":
                    data = data.replace(data[18:21],str(int(data[18])+1)+"/"+str(int(data[20])+1),1)
            if self._typ == "typ3":
                    data = data.replace(data[29:32],str(int(data[29])+1)+"/"+str(int(data[31])+1),1)

        else:
            self._uspesnost = "špatně"
            if self._typ == "typ1":
                    data = data.replace(data[7:10],str(int(data[7]))+"/"+str(int(data[9])+1),1)
            if self._typ == "typ2":
                    data = data.replace(data[18:21],str(int(data[18]))+"/"+str(int(data[20])+1),1)
            if self._typ == "typ3":
                    data = data.replace(data[29:32],str(int(data[29]))+"/"+str(int(data[31])+1),1)
        
        s.close()
        s = open("statistika_uloh.txt","wt")
        s.write(data)
        s.close()
        print(self._uspesnost)
