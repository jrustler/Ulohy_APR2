from priklad import Priklad
import random

class Test:

    def __init__(self,format,databaze,priklady=[]):
        self._format = format
        self._databaze = databaze
        self._priklady = []
        self._body = 0
        self._znamka = 0
    
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


    @property 
    def body(self):
        return self._body


    @body.setter
    def priklady(self, value):
        self._body = value
    
    @property 
    def znamka(self):
        return self._znamka


    @znamka.setter
    def znamka(self, value):
        self._znamka = value


    def pridej_priklad(self,priklad):
        self._priklady.append(priklad)
    
    def spust_test(self):
        for p in self._priklady:
            p.vypis_a_zkontroluj()
            p.zapis_do_statistik()
    
    def oznamkuj_se(self):
        body = 0
        for p in self._priklady:
            if p.uspesnost == "správně":
                body += 1
        procenta = int((body/len(self._priklady))*100)
        znamky = {"1":range(85,101),"2":range(70,85),"3":range(55,70),"4":range(40,55),"5":range(0,40)}
        for k in znamky.keys():
            if procenta in znamky[k]:
                znamka = k
        self._znamka = znamka
        print(f"test jsi splnil na {procenta} procent a dostal jsi {self._znamka}")

    

    def vytvor_typ1(self):
        typ = "typ1"
        zadani = random.choice(self._databaze.typ1)
        cisla = []
        operatory = []
        kolik_cisel = zadani.count("$c")
        kolik_operatoru = zadani.count("$o")
        
        for i in range(kolik_cisel):
            c = random.randint(1,100)
            cisla.append(c)
            zadani = zadani.replace("$c",str(c),1)
        
        for i in range(kolik_operatoru):
            o = random.choice(["+","-","*"])
            operatory.append(o)
            zadani = zadani.replace("$o",o,1)
        pocty = ""
        
        for i in range(len(cisla)):
            pocty+=str(cisla[i])
            
            if i <= (len(operatory)-1):
                pocty+=operatory[0]
        
        vysledek = eval(pocty)
        p1 = Priklad(zadani,vysledek,typ)
        return p1

    def vytvor_typ2(self):
        typ = "typ2"
        zadani = random.choice(self._databaze.typ2)
        a = random.randint(1,10)
        k1 = random.randint(-10,10)
        k2 = random.randint(-10,10)
        b = a*(-k1 + -k2)
        c = a*k1*k2
        zadani = zadani.replace("$a",str(a))
        zapis = {b:["$b","$bx"],c:["$c","$c"]}
        for koef in zapis.keys():
            if koef > 0:
                zadani = zadani.replace(zapis[koef][0],"+"+str(koef))
            if koef < 0:
                zadani = zadani.replace(zapis[koef][0],str(koef))
            if koef == 0:
                zadani = zadani.replace(zapis[koef][1],"") 
        if k1>k2:
            vysledek =str(k1)+","+str(k2)
        else:
            vysledek =str(k2)+","+str(k1)
        p2 = Priklad(zadani,vysledek,typ)
        return p2

    def vytvor_typ3(self):
        typ = "typ3"
        zadani = random.choice(self._databaze.typ3)
        m = random.choice([30000,10000,4000,5000,50000,60000,80000])
        cm = random.randint(1,9)
        j = random.choice(["cm","m","km"])
        km = random.randint(1,9)
        zadani = zadani.replace("$m",str(m))
        if zadani.count("$cm") != 0:
            zadani = zadani.replace("$cm",str(cm))
            zadani = zadani.replace("$j",str(j))
            nuly = {"cm":1,"m":100,"km":100000}
            for jed in nuly.keys():
                if j == jed:
                    vysledek=str(round((cm*(m/nuly[jed])),1)).replace(".0","")
        else:
            zadani = zadani.replace("$km",str(km))
            vysledek = str(round((km/m)*100000,1)).replace(".0","")
        p3 = Priklad(zadani,vysledek,typ)
        return p3

    
    def vytvor_test(self):
        for i in range(self._format[0]):
            self.pridej_priklad(self.vytvor_typ1())
        for i in range(self._format[1]):
            self.pridej_priklad(self.vytvor_typ2())
        for i in range(self._format[2]):
            self.pridej_priklad(self.vytvor_typ3())
    
    def vytvor_test_txt(self,txt_zadani = "zadani.txt",txt_reseni = "reseni.txt"):
        if self._priklady == []:
            self.vytvor_test()
        z = open(txt_zadani,"w")
        r = open(txt_reseni,"w")
        for k,p in enumerate(self._priklady):
            z.write(str(k+1)+". "+p.zneni+"\n")
            r.write(str(k+1)+". "+str(p.vysledek)+"\n")
        z.close()
        r.close()
    
    def vypis_spravne(self):
        spravne_vysledky =""
        for p in self._priklady:
            spravne_vysledky+=(" "+str(p.zneni)+": "+str(p.vysledek)+"\n")
        print(f"správné výsledky byly:\n{spravne_vysledky}") 
    
