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
kitalalando_szam = input()