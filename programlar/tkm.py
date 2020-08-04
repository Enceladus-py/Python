import random
print("TAS KAGIT MAKAS OYUNUNA HOSGELDIN! ")
isim1= "Sen kazandın! "
isim2= "Bilgisayar kazandı! "
isim3= "Berabere! "
puan_oyuncu = 0
puan_bilgisayar = 0
print("Puanlar (bilgisayar/oyuncu) \n",puan_oyuncu,puan_bilgisayar)
liste1 = ["Tas","Makas","Kagıt"]
liste2 = [0,10,20]
while puan_bilgisayar in liste2 and puan_oyuncu in liste2 :
 oyuncu = int(input("tas(1), makas(2), kagıt(3) \n Birini sec! "))
 bilgisayar = random.choice(liste1)
 print("Bilgisayar sunu secti : ",bilgisayar)
 if oyuncu == 1 and bilgisayar == "Makas" :
   print(isim1)
   puan_oyuncu = puan_oyuncu + 10
   print("Puanlar (bilgisayar/oyuncu) \n",puan_bilgisayar,puan_oyuncu)
 elif oyuncu ==1 and bilgisayar == "Kagıt" : 
   print(isim2)
   puan_bilgisayar=puan_bilgisayar+10
   print("Puanlar (bilgisayar/oyuncu) \n",puan_bilgisayar,puan_oyuncu)
 elif oyuncu ==1 and bilgisayar == "Tas" :
   print(isim3)
   print("Puanlar (bilgisayar/oyuncu) \n",puan_bilgisayar,puan_oyuncu)
 elif oyuncu==2 and bilgisayar== "Tas":
   print(isim2)
   puan_bilgisayar=puan_bilgisayar+10
   print("Puanlar (bilgisayar/oyuncu) \n",puan_bilgisayar,puan_oyuncu)
 elif oyuncu==2 and bilgisayar== "Makas":
   print(isim3)
   print("Puanlar (bilgisayar/oyuncu) \n",puan_bilgisayar,puan_oyuncu)
 elif oyuncu ==2 and bilgisayar=="Kagıt":
   print(isim1)
   puan_oyuncu=puan_oyuncu+10
   print("Puanlar (bilgisayar/oyuncu) \n",puan_bilgisayar,puan_oyuncu)
 elif oyuncu==3 and bilgisayar=="Tas":
   print(isim1)
   puan_oyuncu=puan_oyuncu+10
   print("Puanlar (bilgisayar/oyuncu) \n",puan_bilgisayar,puan_oyuncu)
 elif oyuncu==3 and bilgisayar== "Makas":
   print(isim2)
   puan_bilgisayar=puan_bilgisayar+10
   print("Puanlar (bilgisayar/oyuncu) \n",puan_bilgisayar,puan_oyuncu)
 elif oyuncu ==3 and  bilgisayar=="Kagıt":
   print(isim3)
   print("Puanlar (bilgisayar/oyuncu) \n",puan_bilgisayar,puan_oyuncu)
if puan_oyuncu>20 or puan_bilgisayar>20:
   print("Oyun bitti! ")
   if puan_bilgisayar > puan_oyuncu:
      print("Kazanan Bilgisayar")
      input()
   else :
      print ("Kazanan Oyuncu")
      input()
 
   

  
   

