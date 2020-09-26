import pygame
import sys
import random
pygame.init()
saat=pygame.time.Clock()
ekran=pygame.display.set_mode((500,500))
degisken=0
hareket=5
s1=(255,0,0)
s2=(255,255,0)
dusmansayisi=0
koordinat=range(0,501,50)                         #OYUN BAŞLANGIÇ EKRANI AYARLA
size=10
font2 = pygame.font.SysFont(None, 24)
font3 = pygame.font.SysFont(None, 64)
x1=100
y1=100
class Dusman:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def ciz(self):
    pygame.draw.circle(ekran,s2,(self.x,self.y),10)
  def rand123(self):
    self.x=random.choice(koordinat)
    self.y=random.choice(koordinat)
  def dusmanx(self):
    return self.x
  def dusmany(self):
    return self.y

dusmanlar=[]
def ekle():
  dusmanlar.append(Dusman(random.choice(koordinat),random.choice(koordinat))) 
ekle()

font5 = pygame.font.SysFont(None, 48)
font6 = pygame.font.SysFont(None, 24)
img4 = font6.render("Oynanış", True, (255,100,10))
img5 = font6.render("GERİ", True, (255,100,10))
img6 = font6.render("Beslendikçe büyü ve diğer renge geç.", True, (255,100,10))
imgw = font6.render("W-YUKARI", True, (255,100,10))
imgs = font6.render("S-AŞAĞI", True, (255,100,10))
imga = font6.render("A-SOL", True, (255,100,10))
imgd = font6.render("D-SAĞ", True, (255,100,10))
rectx=200
recty=250
def renk():
  saat.tick(5)
  img7 = font5.render("BAŞLA", True, (random.choice(range(100,256)),random.choice(range(100,256)),random.choice(range(100,256))))
  ekran.blit(img7, (200,160))

intro=True
oyun=False
while intro:
  ekran.fill((0,0,0))
  mouse_pos = pygame.mouse.get_pos() 

  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      sys.exit()
    if event.type==pygame.MOUSEBUTTONUP:
      if 200<=mouse_pos[0]<=310 and 160<=mouse_pos[1]<=270:
        oyun=True
        intro=False
      if rectx<=mouse_pos[0]<=rectx+100 and recty<=mouse_pos[1]<=recty+50:
        ayarlar=True
        while ayarlar:
          ekran.fill((0,0,0))
          mouse_pos = pygame.mouse.get_pos()  
          for event in pygame.event.get():
            if event.type==pygame.QUIT:
              sys.exit()
            if event.type==pygame.MOUSEBUTTONUP:
              if 200<=mouse_pos[0]<=300 and 300<=mouse_pos[1]<=350:
                ayarlar=False
                intro=True

          pygame.draw.rect(ekran,(100,10,10),(200,300,100,50))
          ekran.blit(img5,(230,310))    
          ekran.blit(imgw,(230,110))    
          ekran.blit(imgs,(230,140))    
          ekran.blit(imga,(230,170))    
          ekran.blit(imgd,(230,200))
          ekran.blit(img6,(150,250))    
          pygame.display.update()  
        


  pygame.draw.rect(ekran,(0,0,0),(200,160,110,50))
  pygame.draw.rect(ekran,(100,10,10),(rectx,recty,100,50))
  renk()
  ekran.blit(img4, (rectx+10,recty+10))
  pygame.display.update()

t0=pygame.time.get_ticks()/1000
while oyun:
  t1=pygame.time.get_ticks()/1000
  dt=t1-t0
  gecenzaman=str(pygame.time.get_ticks()/1000)[0:4]

  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      sys.exit()
  keys=pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    x1-=hareket
  if keys[pygame.K_RIGHT]:
    x1+=hareket
  if keys[pygame.K_DOWN]:
    y1+=hareket
  if keys[pygame.K_UP]:
    y1-=hareket
              
  ekran.fill((0,0,0))
  
  

  for i in range(len(dusmanlar)):
    dusmanlar[i].ciz()

    if dusmanlar[i].dusmanx()-size<=x1<=dusmanlar[i].dusmanx()+size and dusmanlar[i].dusmany()-size<=y1<=dusmanlar[i].dusmany()+size:
      size+=2
      dusmansayisi+=1
      dusmanlar[i].rand123()
      if len(dusmanlar)<=5:
        ekle()

  if size>=100:
    ekle()
    ekle()
    degisken+=1
    hareket+=2
    size=10
    s1=(random.choice(range(0,256)),random.choice(range(0,256)),random.choice(range(0,256)))

  if degisken==3:
    oyun=False
    while not oyun:
      t2=pygame.time.get_ticks()/1000
      ekran.fill((0,0,0))
      font = pygame.font.SysFont(None, 48)
      font1 = pygame.font.SysFont(None, 24)
      img = font.render("OYUN BİTTİ", True, (255,0,0))
      img3 = font1.render("Yediğin yemek sayısı: "+ str(dusmansayisi), True, (255,0,0))
      img1 = font1.render("Tekrar oynamak için r'ye bas. ", True, (225,125,0))
      ekran.blit(img, (150,160)) 
      ekran.blit(img3, (150,250)) 
      ekran.blit(img1, (150,350))
      ekran.blit(font2.render("Geçen zaman: " + str(dt)[0:4] + " saniye", True, (255,0,0)),(150,300))
      pygame.display.update()
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          sys.exit()
        elif event.type==pygame.KEYDOWN:
          if event.key==pygame.K_r:
            t1=t2
            t0=t1
            hareket=5
            size=10
            degisken=0
            s1=(255,0,0)
            dusmanlar=[]
            ekle()
            oyun=True
      
  if x1<0:
      x1=500
  if x1>500:
      x1=0
  if y1<0:
      y1=500
  if y1>500:
      y1=0

  

  pygame.draw.circle(ekran,s1,(x1,y1),size)
  img2 = font2.render("Ağırlık:"+str(size), True, (225,125,0))
  ekran.blit(img2,(20,20))
  ekran.blit(font3.render("*" * degisken, True, (0,0,255)),(18,40))
  ekran.blit(font2.render("Zaman: " + str(dt)[0:4], True, (255,0,0)),(120,20))
  
  pygame.display.update()  
  saat.tick(80)

  





    

