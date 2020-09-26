import pygame
import sys
import random
import os
import pygame.freetype
x=20
kutusayisi=1
pygame.init()
font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"fonts","cnr.otf")
font_size = 10
myfont = pygame.freetype.Font(font_path, font_size)
puan=0
saat=pygame.time.Clock()
liste=range(1,751)
liste1=range(100,256)
en=800
boy=600
kırmızı=(255,0,0)
yesil=(0,255,0)
rastgele=(random.choice(liste1),random.choice(liste1),random.choice(liste1))
dusmany=0
dusmanx=random.choice(liste)
dusman_en=50
dusman_boy=50
oyuncux=400
oyuncuy=550
oyuncu_en=50
oyuncu_boy=50
ekran=pygame.display.set_mode((en,boy))
oyunbitti=0
while oyunbitti==0:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
            if event.key==pygame.K_LEFT:        
               oyuncux =oyuncux-oyuncu_en
            elif event.key==pygame.K_RIGHT:
                oyuncux=oyuncux+oyuncu_boy
            if oyuncux>=800:
                oyuncux=750
            if oyuncux<=0:
                oyuncux=0          
    ekran.fill((0,0,0))
    if dusmany>=0 and dusmany<=800:
        dusmany+=20
    else:
        dusmany=0
        puan=puan+10
        dusmanx=random.choice(liste)
        rastgele=(random.choice(liste1),random.choice(liste1),random.choice(liste1))
        if x<=30:
            x=x+1
        if puan>10:
            dusman1x=random.choice(liste)
            if puan>20:
                dusman2x=random.choice(liste)
                if puan>30:
                    dusman3x=random.choice(liste)

                            

    if (dusmany==580 and dusmanx-50<oyuncux<dusmanx+50) or (puan>10 and dusmany==580 and dusman1x-50<oyuncux<dusman1x+50) or (puan>20 and dusmany==580 and dusman2x-50<oyuncux<dusman2x+50) or (puan>30 and dusmany==580 and dusman3x-50<oyuncux<dusman3x+50) :
        oyunbitti=1

    

        while oyunbitti==1:
            ekran.fill((0,0,0))
            myfont.render_to(ekran, (300,200), "Skorun :" + str(puan), kırmızı, None, size=32)
            myfont.render_to(ekran, (300,300), "OYUN BITTI!!!", kırmızı, None, size=32)
            myfont.render_to(ekran, (200,400), "Yeni oyun icin r'ye bas.", kırmızı, None, size=32)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        puan=-10
                        x=20
                        oyunbitti=0
                        
    
    saat.tick(x)

    myfont.render_to(ekran, (650, 4), "Skor:"+str(puan), kırmızı, None, size=32)    
    pygame.draw.rect(ekran,kırmızı,(oyuncux,oyuncuy,oyuncu_en,oyuncu_boy))
    pygame.draw.rect(ekran,rastgele,(dusmanx,dusmany,oyuncu_en,oyuncu_boy))
    if puan>10:
        pygame.draw.rect(ekran,rastgele,(dusman1x,dusmany,oyuncu_en,oyuncu_boy))
        if puan>20:
            pygame.draw.rect(ekran,rastgele,(dusman2x,dusmany,oyuncu_en,oyuncu_boy))
            if puan>30:
                pygame.draw.rect(ekran,rastgele,(dusman3x,dusmany,oyuncu_en,oyuncu_boy))



            
    pygame.display.update()
#birden fazla kutu nasıl oluşturulabilir ? 