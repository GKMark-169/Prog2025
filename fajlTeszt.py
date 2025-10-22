
verseny_adatok=[]

try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        verseny_adatok= fajl.readlines()

        
except Exception as ex:
    print("Cs! : Hiba oka:{ex}")
except FileExistsError: 
    print("Gebasz van baszod!!!!")

'''
   1. [Megszámolás] [X]
   2. [Eldöntés 1] [X]
      [Eldöntés 2] [X]
   3. [Kiválasztás] [X]
   4. [Keresés] [X]
   5. [Sorozatszámítás, összegzés] [X]
   6. [Minimum/Maximum kiválasztás]
   
   7. [Másolás]
   8. [Kiválogatás]
   9. [Szétválogatás]
   10.[Metszet]
   11.[Únió]
   
   12.Rendezés
      [Egyszerű cserés rendezés]
      [Buborékos]
      [Minimum kiválasztásos]
'''
#------------------------------------------------------------------------------
# 1. Hány versenyző nem szerzett még pontot?
db=0
for i in range(1, len(verseny_adatok)):
    if (int(verseny_adatok[i].split(",")[1])==0):
        db=db+1
        
        
    
print(f"{db} versenyző nem szerzett még pontott. \n")

#------------------------------------------------------------------------------------
#2. Van-e Fernando nevű versenyző?
i = 0
while(i<len(verseny_adatok) and "Fernando" not in verseny_adatok[i]):
    i+=1
if (i<len(verseny_adatok)):
    print("Van Fernando versenyző!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("Nincs ilyen he!!!!")

# 2.B Mindenki szerzett-e már 90 pontott?????????????
i=1
while (i<len(verseny_adatok) and int(verseny_adatok[i].split(",")[1]))>90:
    i=+1
if i==len(verseny_adatok):
    print("igen")
else:
    print("nem")
    
#3. Melyik istálló pilotája Yuki Tsunoda?
i=0
while verseny_adatok[i].split(",")[0]!="Yuki Tsunoda":
    i+=1
print(f"Yuki Tsunoda helye: {verseny_adatok[i].split(",")[2]}")

#4.Melyik csapatban volt Pierre Gasly?
i=1
while i<len(verseny_adatok) and "Pierre Gasly" not in verseny_adatok[i]:
    i+=1
if i<len(verseny_adatok):
    print("Pierre Gasly", verseny_adatok[i].split(",")[2].strip()),"csapatba van!   :)"
else:
    print("Pierre Gasly nics!")
    
#5. Számolja ki a vesenyzők pontszámainak átlagát

S=0
osszeg=0
for i in range(1, len(verseny_adatok)):
    S+=int(verseny_adatok[i].split(",")[1])
print(f"a versenyzők pontszámainak átlaga: {S/len(verseny_adatok)-1}")
    
#6. Kiszerezte a legtöbb pontot? pontok lacikám pontok
maxi=1
max=verseny_adatok[i].split(",")[1]
for i in range(1,len(verseny_adatok)):
    if verseny_adatok[i]>verseny_adatok[maxi]:
        maxi=i
        max=verseny_adatok[i].split(",")[1]
print(f"")
    
    
    
    
    
    
print("DOOOOOOOOMMMMMAAAAAAAA!!")