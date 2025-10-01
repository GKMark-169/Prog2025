try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        f= fajl.read()
        n=4/0
    
        print(f)
        print(n)
        
        
        
        

except FileExistsError: 
    print("Gebasz van baszod!!!!")
except ZeroDivisionError:
    print("Ne osz 0-al!!!!")
except Exception:
    print("Cs! : Hiba oka:{ex}")
print("Haaamooonddd!!")