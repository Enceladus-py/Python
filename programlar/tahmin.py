import random
liste=range(1,101)
print("***TAHMİN OYUNU***")
print(list(liste))
sayi=random.choice(liste)
can=10
print("10 deneme hakkın var.")
tahmin=int(input("tahmin gir :"))
while can>0:
    if tahmin==sayi:
        print("dogru")
        break
        input()
    elif 0< abs(sayi-tahmin)<=10 :
        print("cok cok yaklastin")
        if 0<tahmin<=10 :
          print("tuttugum sayi su aralikta: ", "[",1,",",tahmin+10,"]")
        else:    
          print("tuttugum sayi su aralikta: ", "[",tahmin-10,",",tahmin+10,"]")
        can=can-1
        if can>0:
              tahmin=int(input("tahmin gir :"))
    elif 10< abs(sayi-tahmin)<=20:
        print("cok yaklastin")
        if 0<tahmin<=20 :
          print("tuttugum sayi su aralikta: ", "[",1,",",tahmin+20,"]")
        else:    
          print("tuttugum sayi su aralikta: ", "[",tahmin-20,",",tahmin+20,"]")
        can=can-1
        if can>0:
           tahmin=int(input("tahmin gir :"))
    elif 20< abs(sayi-tahmin)<=30:
        print("biraz yaklastin")
        if 0<tahmin<=30 :
          print("tuttugum sayi su aralikta: ", "[",1,",",tahmin+30,"]")
        else:    
          print("tuttugum sayi su aralikta: ", "[",tahmin-30,",",tahmin+30,"]")
        can=can-1
        if can>0:
           tahmin=int(input("tahmin gir :"))
    elif abs(sayi-tahmin)>30:
        print("uzaksin")
        can=can-1
        if can>0:
           tahmin=int(input("tahmin gir :"))
    else:
       print("yanlis")
       can=can-1
       if can>0:
          tahmin=int(input("tahmin gir :"))
else:
     print("deneme hakkin kalmadi.")
     print("tuttugum sayi: ", sayi)
input()