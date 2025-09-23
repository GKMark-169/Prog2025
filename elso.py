import random


szamok=[]

#100 elemű lista feltöltése 1-99 között véletlenszámokkal
for i in range(100):
    #..... szám generálás
    rszam = random.randint(1, 100)

    #szám elhelyezése a listába
    szamok.append(rszam)
    
#ellenőrzés
print(szamok)




#egyszámjáték
jatek_szam = 0
nem_talaltdb = 0

#kitalálandó szám beállítása
kitalalando_szam = szamok[random.randint(0, len(szamok))]

tipp = int(input("Kérek egy egész számot [1-100]: "))

if (tipp == kitalalando_szam):
    print("De jó neked")
elif(tipp < kitalalando_szam):
    print("A szám nagyob!")
else:
    print("A szám kicib!")
    
while(tipp != kitalalando_szam):
    tipp = int(input("Kérek egy egész számot [1-100]: "))
    
    if (tipp == kitalalando_szam):
        print("De jó neked")
    elif(tipp < kitalalando_szam):
        print("A szám nagyob!")
    else:
        print("A szám kicib!")