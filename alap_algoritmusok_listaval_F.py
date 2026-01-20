"""
    Ebben a feladatban a 12.B tanulócsoport
    DHCP témakörben
    mutatott teljesítményének néhány elemével
    kell műveleteket végeznie!
    
    Az adatok a 12B_dhcp_ponttabla.txt fájlban találhatóak meg!
    
    A fájl felépítése:
    1.sor: Tartalmazza a maximális pontszám feliratot és az értéket.
    2.sor: Az adatsorok oszlopaiban szereplő értékek magyarázatai:
        név
        elméleti dolgozat pontszáma
        gyakorlati dolgozat pontszáma
        össz pontszám
    3. sortól: az adatok
    
    A fejlécben és az adatértékek között az elválasztó karakter: ';'
    
    A programot metódusok segítségével oldja meg!
    A fájl végén találja a programot, ahol meghívhatja a metódusokat és kiírhatja az eredményeket. Kiírásnál jelenjen meg a feladat sorszáma is!
    Pl.: 13. feladat:
            A pontszámok átlaga: 435 pont.
"""

# *************************************
# GLOBÁLIS VÁLTOZÓK

ossz_pontszam = 0

tanulo_adatok = []


# *************************************

# METÓDUSOK/FÜGGVÉNYEK

"""
    1.
    Olvassa be a fájl tartalmát figyelembe véve a fájl szerkezetét!
    A maximális pontszámot tárolja el az ossz_pontszam változóban!
    A tanulók adatait egy "2D"-s listában  (lista a listában: tanulo_adatok) tárolja el.
    A metódus neve: fajl_beolvasas
"""

def fajl_beolvasas(inputfajl):
    try:
        with open(inputfajl, encoding="utf8")as fajl:
            global ossz_pontszam
            ossz_pontszam=int(fajl.readline().strip().split(" ")[2])
            
            fajl.readline()
            
            for sor in fajl:
                sornyi_adat=sor.strip().split(";")
                sornyi_adat[1]=int(sornyi_adat[1])
                sornyi_adat[2]=int(sornyi_adat[2])
                sornyi_adat[3]=int(sornyi_adat[3])
                tanulo_adatok.append(sornyi_adat)
            
    except IOError as hiba:
        print(f"hiba: {hiba}")



"""
    2.
    Határozza meg hány tanulóból áll a csoport!
    A metódus neve: csoport_letszam
"""
def csoport_letszam():
    return len(tanulo_adatok)




"""
    3.
    Határozza meg melyik tanuló gyűjtötte a legtöbb pontszámot!
    A metódus neve: legszorgalmasabb
"""
def legszorgalmasabb():
    maxi=0
    for i in range(1, len(tanulo_adatok)):
        if tanulo_adatok[i][3]>tanulo_adatok[maxi][3]:
            maxi=i
    return tanulo_adatok[maxi][0]

"""
    4.
    Mikulás közeledtével a tanár mindenkinek bónusz pontokat ír jóvá.
    Minden tanuló az össz pontszámának 5%-át kapja meg bónuszként.
    Kiírásnál jelenítse meg a tanulók nevét és az új pontszámokat.
    A metódus neve: miki_ajandek
"""
def miki_ajandek():
    for i in range(len(tanulo_adatok)):
        tanulo_adatok[i][3]=round(tanulo_adatok[i][3]*1.05)



# *************************************
#   PROGRAM
# *************************************
cim = "Eredmény feldolgozó szkript"
print(f"\n{'*' * 40}\n{cim.upper():^40}\n{'*' * 40}\n\n")


# fajl_beolvasas
inputfile="12B_dhcp_ponttabla.txt"
fajl_beolvasas(inputfile)
print(tanulo_adatok)
# csoport_letszam
print(f"A csoport létszáma:{csoport_letszam()}")
# legszorgalmasabb
print(f"A legtöbb pontot szerző tanuló: {legszorgalmasabb()}")
# miki_ajandek
miki_ajandek()
for i in range(len(tanulo_adatok)):
    print(f"{tanulo_adatok[i][0]:20}\t{tanulo_adatok[i][3]}")


print("\nProgram vége. BYE!\n")


