import sys
import random
import pandas as pd
from databaze import Databaze
from priklad import Priklad
from zak import Zak
from Test import Test

def vysledky_zaku(soubor):
    df = pd.read_excel(soubor,dtype = str)
    if len(df) !=0:
        for c in df:
            print(df[c][0]+" "+df[c][1]+" : "+df[c][2])
    else:
        print("zatim zadna data o zacich")

def co_dal(zak):
    co = input("Znovu?:1/konec?:2/me znamky:3")
    if co == str(1) :
        main()
    elif co == str(2) :
        print("sbohem")
        sys.exit(2)
    elif co == str(3):
        zak.vypis_znamky()
        zak.vypis_prumer()
        co_dal(zak)
    else:
        co_dal(zak)
    
def co_dal_u(soubor,databaze,format):
    co = input("zaci s vysledky:1/konec:2/vymazat data zaku:3/restart:4/vytvor test do txt:5/reset statistik:6/vypis statistik:7")
    if co == str(1):
        vysledky_zaku(soubor)
        co_dal_u(soubor,databaze,format)
    elif co == str(2):
        print("sbohem")
        sys.exit(2)
    elif co == str(3):
        reset_zaci(soubor)
        co_dal_u(soubor,databaze,format)
    elif co == str(4):
        main()
    elif co == str(5):
        test = Test(format,databaze)
        vytvor_test(test)
        vytvor_test_txt(test)
        co_dal_u(soubor,databaze,format)
    elif co == str(6):
        s = open("statistika_uloh.txt","w")
        s.write("typ1 = 0/0\ntyp2 = 0/0\ntyp3 = 0/0")
        s.close()
        co_dal_u(soubor,databaze,format)
    elif co == str(7):
        vypis_statistiky()
        co_dal_u(soubor,databaze,format)
    else:
        co_dal_u(soubor,databaze,format)

def jaky_zak(soubor):
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
    typ = "typ1"
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
    p1 = Priklad(zadani,vysledek,typ)
    return p1

def vytvor_typ2(databaze):
    typ = "typ2"
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
    p2 = Priklad(zadani,vysledek,typ)
    return p2

def vytvor_typ3(databaze):
    typ = "typ3"
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
    p3 = Priklad(zadani,vysledek,typ)
    return p3

def vytvor_test(testik):
    for i in range(testik.format[0]):
        testik.pridej_priklad(vytvor_typ1(testik.databaze))
    for i in range(testik.format[1]):
        testik.pridej_priklad(vytvor_typ2(testik.databaze))
    for i in range(testik.format[2]):
        testik.pridej_priklad(vytvor_typ3(testik.databaze))

def oznamkuj(body,testik,zak):
    max_body = len(testik.priklady)
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
    for p in testik.priklady:
        spravne_vysledky+=(" "+str(p.zneni)+": "+str(p.vysledek)+"\n")
    print(f"Test jsi splnil na {procenta} procent a dostal jsi {znamka}")
    print(f"správné výsledky byly:\n{spravne_vysledky}")
    return zak

def vytvor_test_txt(test,txt_zadani = "zadani.txt",txt_reseni = "reseni.txt"):
    z = open(txt_zadani,"w")
    r = open(txt_reseni,"w")
    for k,p in enumerate(test.priklady):
        z.write(str(k+1)+". "+p.zneni+"\n")
        r.write(str(k+1)+". "+str(p.vysledek)+"\n")
    z.close()
    r.close()

def vypis_statistiky():
    s = open("statistika_uloh.txt","r")
    for l in s:
        print(l)
    s.close()

def main():
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
        zak = jaky_zak(soubor)
        testik = Test(format,databaze)
        vytvor_test(testik)
        zak = oznamkuj(testik.spust_test(),testik,zak)
        co_dal(zak)
    if kdo == "u":
        co_dal_u(soubor,databaze,format)

    
if __name__ == "__main__":
    main()

