import random
from databaze import Databaze
from priklad import Priklad

databaze = Databaze("priklady1.txt")
format = [3]

def vytvor_priklad(typ):
    
    if typ == 1:
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
            o = random.choice(["+","-","*","/"])
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

def vytvor_test(format):
    test = []
    for i in range(format[0]):
        test.append(vytvor_priklad(1))
    return test

def spust_test(test):
    body = 0
    for p in test:
        p.vypis_a_zkontroluj()
        if p.uspesnost == "správně":
            body+=1
    return body
def oznamkuj(body,testik):
    max_body = len(testik)
    procenta = (body/max_body)*100
    if procenta >=85:
        znamka = 1
    if procenta < 85 and procenta >= 70:
        znamka = 2
    if procenta < 70 and procenta >= 55:
        znamka = 3
    if procenta < 55 and procenta >= 40:
        znamka = 4
    else:
        znamka = 5
    print(f"Test jsi splnil na {procenta} procent a dostal jsi {znamka}")


#testik = vytvor_test(format)
#oznamkuj(spust_test(testik),testik)
