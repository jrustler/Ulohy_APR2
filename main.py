import sys
import random
import pandas as pd
from databaze import Databaze
from priklad import Priklad
from zak import Zak

databaze = Databaze("priklady1.txt")
format = [1,2]

def co_dal(zak):
    co = input("Znovu?:1/konec?:2/me znamky:3")
    if co == str(1) :
        main(format)
    if co == str(2) :
        print("sbohem")
        sys.exit(2)
    if co == str(3):
        zak.vypis_znamky()
        co_dal(zak)
    if co != str(1) and co != str(2) and co != str(3):
        co_dal(zak)
    

def handler():
    udaje=[0,0,"0"]
    zaci = pd.read_excel("zaci.xlsx")
    st = input("Zadejte sve st:")
    if st not in zaci.columns:
        udaje[0]=input("zadej sve jmeno:")
        udaje[1]=input("zadej sve prijmeni:")
        zaci[st] = udaje
        zaci.to_excel("zaci.xlsx",index = False)
    zak = Zak(st,"zaci.xlsx")
    return zak  

def reset_zaci(soubor):
    d = pd.DataFrame([],[])
    d.to_excel(soubor, index = False)

def vytvor_typ1():
    
    zadani = random.choice(databaze.typ1)
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
    p1 = Priklad(zadani,vysledek)
    return p1
def vytvor_typ2():
    zadani = random.choice(databaze.typ2)
    a = random.randint(1,10)
    k1 = random.randint(-10,10)
    k2 = random.randint(-10,10)
    b = -a*(k1 + k2)
    c = a*k1*k2
    zadani = zadani.replace("$a",str(a))
    if b > 0:
        zadani = zadani.replace("$b","+"+str(b))
    if b < 0 :
        zadani = zadani.replace("$b",str(b))
    if b == 0:
        zadani = zadani.replace("$bx"," ")
    if c > 0:
        zadani = zadani.replace("$c","+"+str(c))
    if c < 0:
        zadani = zadani.replace("$c",str(c))
    if c == 0:
        zadani = zadani.replace("$c","")
    
    if k1>k2:
        vysledek =str(k1)+","+str(k2)
    else:
        vysledek =str(k2)+","+str(k1)
    
    p2 = Priklad(zadani,vysledek)
    
    return p2

def vytvor_test(format):
    test = []
    for i in range(format[0]):
        test.append(vytvor_typ1())
    for i in range(format[1]):
        test.append(vytvor_typ2())
    return test

def spust_test(test):
    body = 0
    for p in test:
        p.vypis_a_zkontroluj()
        if p.uspesnost == "správně":
            body+=1
    return body
def oznamkuj(body,testik,zak):
    max_body = len(testik)
    procenta = int((body/max_body)*100)
    if procenta >=85:
        znamka = 1
    if procenta < 85 and procenta >= 70:
        znamka = 2
    if procenta < 70 and procenta >= 55:
        znamka = 3
    if procenta < 55 and procenta >= 40:
        znamka = 4
    if procenta <40:
        znamka = 5
    zak.pridej_znamku(znamka)
    print(f"Test jsi splnil na {procenta} procent a dostal jsi {znamka}")
    return zak
def main(format):
    reset_zaci("zaci.xlsx")
    zak = handler()
    testik = vytvor_test(format)
    zak = oznamkuj(spust_test(testik),testik,zak)
    co_dal(zak)
    
if __name__ == "__main__":
    main(format)

#reset_zaci("zaci.xlsx")
#testik = vytvor_test(format)
#oznamkuj(spust_test(testik),testik)
