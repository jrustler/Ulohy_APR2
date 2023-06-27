import sys
import random
import pandas as pd
from databaze import Databaze
from priklad import Priklad
from zak import Zak
from test import Test
from data_zaku import Data_zaku
from statistika_u import Statistika_u

def ui(kdo,data_zaku,test,statistika_u,zak):
    menu = {"z":"---------------------- \n znovu? : 1 \n konec? : 2 \n me znamky : 3 \n muj prumer : 4 ",
            "u": "---------------------- \n restart: 1 \n konec : 2 \n vymazat data zaku : 3 \n zaci s vysledky : 4 \n vytvor test do txt :5 \n reset statistik : 6 \n vypis statistik : 7"}
    ui_input = {"z":{"1": main,
                     "2": sys.exit,
                     "3":zak.vypis_znamky,
                     "4":zak.vypis_prumer},
                "u":{"1":main,
                    "2":sys.exit,
                    "3":data_zaku.reset_zaci,
                    "4":data_zaku.vysledky_zaku,
                    "5":test.vytvor_test_txt,
                    "6":statistika_u.reset_statistik,
                    "7":statistika_u.vypis_statistiky}}
    print(menu[kdo])
    co = input(" Co dal?")
    ui_input[kdo][co]()
    ui(kdo,data_zaku,test,statistika_u,zak)

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
    test = Test(format,databaze)
    data_zaku = Data_zaku(soubor)
    statistika_u=Statistika_u("statistika_uloh.xlsx")
    zak = Zak(0,soubor) #umely zak
    if kdo == "z":
        zak = data_zaku.jaky_zak()
        test.vytvor_test()
        test.spust_test()
        test.vypis_spravne()
        test.oznamkuj_se()
        zak.pridej_znamku(test.znamka)
    ui(kdo,data_zaku,test,statistika_u,zak)
    

    
if __name__ == "__main__":
    main()

