import random
d=1
print("zar atma oyununa hosgeldin! \naynı gelirse kazanirsin. ".title())
can=int(input("kac tane sans istersin? ".capitalize()))
print("Sans= " ,"*"*can)
liste=range(1,can+1)
zar=range(1,7)
while can >0 and d==1:
        a=random.choice(zar)
        b=random.choice(zar)
        print("zarlar soyle geldi: ".capitalize(), a,b)
        if a==b:
           print("kazandin".capitalize())
           print("oyun bitti.".capitalize())
           d=int(input("yeni oyuna devam etmek icin 1'e bas. ".capitalize()))
           if d==1:
                can=int(input("kac tane sans istersin? ".capitalize()))   
        else:
           print("kaybettin".capitalize())
           can=can-1
           if can >0:
              print("su kadar sans kaldi: ".capitalize() , "*"*can)
              d=int(input("oyuna devam etmek icin 1'e bas. ".capitalize()))
           else:
               print("sansin kalmadi.".capitalize())
               print("oyun bitti.".capitalize()) 
               d=int(input("yeni oyuna devam etmek icin 1'e bas. ".capitalize()))
               if d == 1 :
                  can=int(input("kac tane sans istersin? ".capitalize())) 
if d !=1:
   print("oyun bitti.".capitalize())




