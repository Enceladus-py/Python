import pygame,sys,random
pygame.mixer.init(44100, -16, 2, 512)
pygame.init()
bg_y=0
score=0
highscore=0
gameover=False
d=False
f=False
bullety=430
bulletx=-100
fps=pygame.time.Clock()
surface=pygame.display.set_mode((600,600))
pygame.display.set_caption("Space Game")

pygame.mixer.music.load("gameover.mp3")

font=pygame.font.SysFont(None,48)
img=font.render("GAME OVER",True,(255,255,255))
img1=font.render("Press R for restart.",True,(255,255,255))
img2=font.render("Score: "+str(score),True,(255,255,255))
img3=font.render("Highscore: "+str(highscore),True,(255,255,255))

bg=pygame.image.load("space.png").convert()
player=pygame.image.load("rocket.png")
rock=pygame.image.load("rock.png")
explosion=pygame.image.load("explosion.png")

player_rect=player.get_rect(center=(100,500))
rock_rect=rock.get_rect(center=(100,0))

bg=pygame.transform.scale(bg,(600,600))
player=pygame.transform.scale(player,(80,90))

game=True

rocks=[]
rocks.append(rock_rect)

while game:

    

    fps.tick(120)
                                                                 #EXPLOSİON,Birden fazla SES
    surface.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_v and not d:
                d=True
                bulletx=player_rect.centerx
            if event.key==pygame.K_r and gameover:
                f=True
            

    keys=pygame.key.get_pressed()
    if keys[pygame.K_a] and player_rect.centerx>=20:
        player_rect.centerx-=5
    if keys[pygame.K_d] and player_rect.centerx<=600:
        player_rect.centerx+=5


    bg_y-=1
    if bg_y<=-600:
        bg_y=0
    

    for i in rocks:

        i.centery+=3
        if i.centery>=700:
            i.centery=0
            i.centerx=random.randrange(0,600)
    
        if player_rect.centerx-40<=i.centerx<=player_rect.centerx+40 and player_rect.centery-10<=i.centery<=player_rect.centery:
            
            pygame.mixer.music.play(0)
            gameover=True


    if not gameover:

        img2=font.render("Score: "+str(score),True,(255,255,255))

        surface.blit(bg,(0,bg_y))
        surface.blit(bg,(0,bg_y+600))
        surface.blit(img2,(450,550))
        surface.blit(player,player_rect)
        for x in rocks:
            surface.blit(rock,x)

        if d:
            pygame.draw.circle(surface,(255,120,0),(bulletx,bullety),10)
            bullety-=7
            if bullety<=0:
                bullety=430
                bulletx=-100
                d=False
    
    else:

        if highscore<score:
            highscore=score

        img2=font.render("Score: "+str(score),True,(255,255,255))
        img3=font.render("Highscore: "+str(highscore),True,(255,255,255))

        surface.blit(bg,(0,bg_y))
        surface.blit(bg,(0,bg_y+600))
        surface.blit(img,(200,200))
        surface.blit(img1,(200,400))
        surface.blit(img2,(200,270))
        surface.blit(img3,(200,330))

        rocks=[rock_rect]
        if f:
            player_rect.centerx,player_rect.centery=100,500
            bulletx=-100
            bullety=430
            for i in rocks:
                i.centerx,i.centery=random.randrange(0,600),0
            gameover=False
            f=False
            d=False
            score=0

        pygame.display.update()

    for i in rocks:

        if i.centerx-20<=bulletx<=i.centerx+20 and i.centery-20<=bullety<=i.centery+20:
            
            score+=1
            i.centerx,i.centery=random.randrange(0,600),0
            d=False
            bullety=430
            bulletx=-100    
            if score<=20:
                rocks.append(rock.get_rect(center=(random.randrange(0,600),0)))

    pygame.display.update()