
verseny_adatok=[]


intputfajl="F1-2024dec.csv"


def adat_beolvasas(fajlnev):
    try:
        with open(fajlnev, encoding="utf-8") as fajl:
            global verseny_adatok
            verseny_adatok= fajl.readlines()

        
    except Exception as ex:
        print("Cs! : Hiba oka:{ex}")
    except FileExistsError: 
        print("Gebasz van baszod!!!!")
    
#ELJÁRÁS
def pontatlanok():
    # 1. Hány versenyző nem szerzett még pontot?
    db=0
    for i in range(1, len(verseny_adatok)):
        if (int(verseny_adatok[i].split(",")[1])==0):
            db=db+1

    print(f"{db} versenyző nem szerzett még pontott. \n")

#FÜGGVÉNY
def versenyzo_kereso(nev):
    i = 0
    while(i<len(verseny_adatok) and nev not in verseny_adatok[i]):
        i+=1
    if (i<len(verseny_adatok)):
        return True
    else:
        return False
#ELJÁRÁS
def csapat(nev):
    #4.Melyik csapatban volt Pierre Gasly?
    i=1
    while i<len(verseny_adatok) and "Pierre Gasly" not in verseny_adatok[i]:
        i+=1
         
    if i<len(verseny_adatok):
        print(nev,verseny_adatok[i].split(",")[2].strip()),"csapatba van!   :)"
    else:
        print("Pierre Gasly nics!")
#FÜGGVÉNY
def csapat_tagok(csapatnev):
    #8.Kik vannak a McLarenbe?
    db1=0
    masik=[]
    
    for i in range(2,len(verseny_adatok)):
        if verseny_adatok[i].split(",")[2].strip()==csapatnev:
            db1+=1
            masik.append(verseny_adatok[i].split(",")[0])
            
    return masik
#ELJÁRÁS
def pont():
    # 2.B Mindenki szerzett-e már 90 pontott?????????????
    i=1
    while (i<len(verseny_adatok) and int(verseny_adatok[i].split(",")[1]))>90:
        i=+1
    if i==len(verseny_adatok):
        return True
    else:
        return False      
        
        
        
        
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
""" # 1. Hány versenyző nem szerzett még pontot?
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
for i in range(2,len(verseny_adatok)):
    if verseny_adatok[i]>verseny_adatok[maxi]:
        maxi=i
        max=verseny_adatok[i].split(",")[1]
print(f"A legkevesebb ponttal rendelkező versenyző: {verseny_adatok[maxi].split(",")[1]}")
 
#7. Kinek van a legkevesebb pontja?  
mini=1
min=verseny_adatok[i].split(",")[1]
for i in range(2,len(verseny_adatok)):
    if verseny_adatok[i]<verseny_adatok[min]:
        mini=i
        min=verseny_adatok[i].split(",")[1]
print(f"A legkevesebb ponttal rendelkező versenyző: {verseny_adatok[mini].split(",")[0]}")

#8.Kik vannak a McLarenbe?
db1=0
masik=[]
for i in range(1,len(verseny_adatok)):
    if verseny_adatok[i].split(",")[2].strip()=='McLaren':
        db1+=1
        masik.append(verseny_adatok[i].split(",")[0])
print(f"Ők vannak a McLaren-nél: {verseny_adatok[i].split(",")[0]}")

#9.kinek van és kinek nics pontja?
dby=0
dbx=0
y=[]
x=[]
for i in range(1,len(verseny_adatok)):
    if(int(verseny_adatok[i].split(",")[1]>0)):
        dby=+1
        y.append(verseny_adatok[i].split(",")[0])
    else:
        dbx=+1
        x.append(verseny_adatok[i].split(",")[0])
print(f"Van pontja: {y}")
print(f"Nincs pontja: {x}")

#10.
for i in range(1, len(verseny_adatok)-1):
    min=i
    minertek=int(verseny_adatok[i].split(",")[1])
    for j in range(i+1, len(verseny_adatok)):
        if(int(verseny_adatok[j].split(",")[1])<int(verseny_adatok[min].split(",")[1])):
            min=j
            minertek=int(verseny_adatok[j].split(",")[1])
    s=verseny_adatok[i]
    verseny_adatok[i]=verseny_adatok[min]
    verseny_adatok[min]=s
for i in verseny_adatok:
    print(i) """

#PROGRAM
adat_beolvasas(intputfajl)

pontatlanok()
van_e=versenyzo_kereso("Fernando")
if van_e:
    print("Van Fernando")
else:
    print("Nics Fernando")

#4.F eljárás hívás
csapat("Pierre Gasly")

#8.F függvény hívás
csapat_nev="McLaren"
tag_lista=csapat_tagok(csapat_nev)

print(f"Ezek a személyek vannak a {csapat_nev} istállójában: ")
i=1
for nev in tag_lista:
    print(f"{i}. {nev:>30}")
    i+=1
#2.B, 3.F, 5.F ELJÁRÁSsal

#2.B
pont=verseny_adatok[1]
if pont:
    print("igen")
else:
    print("nem") 

#6.F 2*, 9.F FÜGGVÉNYnyel
print(":|")