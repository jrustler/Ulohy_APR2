import sys
import random
import pandas as pd
from databaze import Databaze
from priklad import Priklad
from zak import Zak

def vysledky_zaku(soubor):
    df = pd.read_excel(soubor)
    for c in df:
        print(df[c][0]+" "+df[c][1]+" : "+df[c][2])

def co_dal(zak):
    co = input("Znovu?:1/konec?:2/me znamky:3")
    if co == str(1) :
        main()
    if co == str(2) :
        print("sbohem")
        sys.exit(2)
    if co == str(3):
        zak.vypis_znamky()
        zak.vypis_prumer()
        co_dal(zak)
    if co != str(1) and co != str(2) and co != str(3):
        co_dal(zak)
    
def co_dal_u(soubor):
    co = input("zaci s vysledky:1/konec:2/vymazat data zaku:3/restart:4")
    if co == str(1):
        vysledky_zaku(soubor)
        co_dal_u(soubor)
    if co == str(2):
        print("sbohem")
        sys.exit(2)
    if co == str(3):
        reset_zaci(soubor)
        co_dal_u(soubor)
    if co == str(4):
        main()

def handler(soubor):
    udaje=[0,0,"0"]
    zaci = pd.read_excel(soubor)
    st = input("Zadejte sve st:")
    if st not in zaci.columns:
        udaje[0]=input("zadej sve jmeno:")
        udaje[1]=input("zadej sve prijmeni:")
        zaci[st] = udaje
        zaci.to_excel(soubor,index = False)
    zak = Zak(st,soubor)
    return zak  

def reset_zaci(soubor):
    d = pd.DataFrame([],[])
    d.to_excel(soubor, index = False)

def vytvor_typ1(databaze):
    
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
def vytvor_typ2(databaze):
    zadani = random.choice(databaze.typ2)
    a = random.randint(1,10)
    k1 = random.randint(-10,10)
    k2 = random.randint(-10,10)
    b = a*(-k1 + -k2)
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
def vytvor_typ3(databaze):
    zadani = random.choice(databaze.typ3)
    m = random.choice([30000,10000,4000,5000,50000,60000,80000])
    cm = random.randint(1,9)
    j = random.choice(["cm","m","km"])
    km = random.randint(1,9)
    zadani = zadani.replace("$m",str(m))
    if zadani.count("$cm") != 0:
        zadani = zadani.replace("$cm",str(cm))
        zadani = zadani.replace("$j",str(j))
        if j == "cm":
            vysledek=str(round((cm*m),1)).replace(".0","")
        if j == "m":
            vysledek=str(round(cm*(m/100),1)).replace(".0","")
        if j == "km":
            vysledek = str(round(cm*(m/100000),1)).replace(".0","")
    else:
        zadani = zadani.replace("$km",str(km))
        vysledek = str(round((km/m)*100000,1)).replace(".0","")
    p3 = Priklad(zadani,vysledek)
    return p3



def vytvor_test(format,databaze):
    test = []
    for i in range(format[0]):
        test.append(vytvor_typ1(databaze))
    for i in range(format[1]):
        test.append(vytvor_typ2(databaze))
    for i in range(format[2]):
        test.append(vytvor_typ3(databaze))
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
    spravne_vysledky =""
    for p in testik:
        spravne_vysledky+=(" "+str(p.zneni)+": "+str(p.vysledek)+"\n")
    print(f"Test jsi splnil na {procenta} procent a dostal jsi {znamka}")
    print(f"správné výsledky byly:\n{spravne_vysledky}")
    return zak
def main():
    #reset_zaci("zaci.xlsx")
    data = input("nazev souboru s predlohami prikladu (pro prednastaveny soubor (priklady1.txt : 1))")
    soubor = input("kam ukladat data o zacich? (xlsx) (pro prednastaveny soubor (zaci.xlsx): 1)")
    jak = input("kolik prikladu jakeho typu? typ1,typ2,typ3")
    if data == "1":
        data = "priklady1.txt"
    if soubor == "1":
        soubor = "zaci.xlsx"
    format = [int(i) for i in jak.split(",")]
    databaze = Databaze(data)
    kdo = input("Jsi ucitel nebo zak? (u/z)")
    if kdo == "z":
        zak = handler(soubor)
        testik = vytvor_test(format,databaze)
        zak = oznamkuj(spust_test(testik),testik,zak)
        co_dal(zak)
    if kdo == "u":
        co_dal_u(soubor)

    
if __name__ == "__main__":
    main()

