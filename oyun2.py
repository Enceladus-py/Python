import pygame
import sys
import random
import os
import pygame.freetype
pygame.freetype.init()
pygame.init()
font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"fonts","cnr.otf")
font_size = 10
myfont = pygame.freetype.Font(font_path, font_size)
saat=pygame.time.Clock()
renk=(random.choice(range(0,256)),random.choice(range(0,256)),random.choice(range(0,256)))
skor=0
can=3
x=50
y=500
x1=100
y1=random.choice(range(100,501,50))
fps=60
degisken1=1
degisken2=0
ekran=pygame.display.set_mode((675,600))
oyun=True
while oyun:
    degisken3=2
    ekran.fill((0,0,0))
    for event in pygame.event.get():                        
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if y>0 and event.key==pygame.K_UP:
                y-=50 
            if y<500 and event.key==pygame.K_DOWN:
                y+=50 
            if event.key==pygame.K_v:
                degisken2=125
    
                
    if degisken2==125:
        fps=20
        saat.tick(fps)
        x1+=50
        if x1>=675:
            x1=x+25
            fps=60
            saat.tick(fps)
            degisken2=0  
    
    if x1>=625 and y1==y:
        y1=random.choice(range(100,511,50))
        y1=random.choice(range(100,511,50))
        y1=random.choice(range(100,511,50))
        renk=(random.choice(range(0,256)),random.choice(range(0,256)),random.choice(range(0,256)))
        skor+=10
        degisken3=1
    if degisken3!=1 and x1>=620:
        can=can-1
    
    if can==0:
        oyun = False
        while oyun==False:
            ekran.fill((0,0,0))
            myfont.render_to(ekran, (200,200), "Oyun bitti! " ,(255,0,0), None, size=32) 
            myfont.render_to(ekran, (200,300), "Skorun: " + str(skor),(255,0,0), None, size=32) 
            myfont.render_to(ekran, (200,400), "Yeni oyun icin r'ye bas.", (255,0,0), None, size=32)
            pygame.display.update()
            for event in pygame.event.get():                        
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        can=3
                        skor=0
                        y1=random.choice(range(100,501,50))
                        oyun=True



    myfont.render_to(ekran, (4,50), "Canın: " + str(can),(255,0,0), None, size=32)    
    myfont.render_to(ekran, (4,4), "Skorun: " + str(skor),(255,0,0), None, size=32)            
    pygame.draw.rect(ekran,(0,0,degisken2),(x1,y,25,25))            
    pygame.draw.polygon(ekran,(50,25,0),[(0,600),(0,550),(675,550),(675,600)])
    pygame.draw.rect(ekran,(0,255,0),(x,y,25,60))
    pygame.draw.rect(ekran,(renk),(650,y1,25,25))
    pygame.display.update()

