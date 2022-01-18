import pygame
from random import randint
from sys import exit
pygame.init()

SCREEN_X,SCREEN_Y = 1000,600
screen=pygame.display.set_mode((SCREEN_X,SCREEN_Y),pygame.SCALED)
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

class Player(pygame.Rect):

    def __init__(self,x,y,color,point):
        self.x=x
        self.y=y
        self.color=color        
        self.point=point
        pygame.Rect.__init__(self,pygame.Rect(self.x,self.y,10,100))


class Ball(pygame.Rect):

    def __init__(self,x,y,vx,vy,color,radius):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.color=color
        self.radius=radius
        pygame.Rect.__init__(self,pygame.Rect(self.x,self.y,self.radius,self.radius))

    def move(self):
        global fps
        if self.top<0 or self.bottom>SCREEN_Y: 
            self.vy = -self.vy
            fps += 5

        self.x += self.vx
        self.y += self.vy

def player_move():
        global fps,movement

        keys=pygame.key.get_pressed()

        if keys[pygame.K_s]:
            if player1.bottom <= SCREEN_Y: player1.y += movement
        if keys[pygame.K_w]:
            if player1.top >= 0: player1.y -= movement
        if keys[pygame.K_UP]:
            if player2.top >= 0: player2.y -= movement
        if keys[pygame.K_DOWN]:
            if player2.bottom <= SCREEN_Y: player2.y += movement

def draw_line_alpha(surface, color, radius, center, vx, vy):

    target_rect = pygame.Rect(center, (0, 0)).inflate(2*radius,2*radius)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.line(shape_surf, color, (radius,radius),(radius-vx,radius-vy))
    surface.blit(shape_surf, target_rect)

def reset(n):
    global fps,movement
    pygame.time.wait(1000)

    if n==2: player2.point += 1
    else: player1.point += 1

    ball.x = SCREEN_X/2
    ball.y = SCREEN_Y/2
    ball.vx = 0
    ball.vy = randint(-5,5)
    fps = 80
    movement = 5

def draw_shapes():

    pygame.draw.rect(screen,player1.color,(player1.x,player1.y,10,100))
    pygame.draw.rect(screen,player2.color,(player2.x,player2.y,10,100))
    pygame.draw.circle(screen,ball.color,(ball.x,ball.y),ball.radius)
    shapes.append([(ball.x,ball.y),ball.vx,ball.vy])
    for i in shapes:
        draw_line_alpha(screen,(255,0,0,100),ball.radius,i[0],i[1],i[2])

    if len(shapes)>40:
        for i in range(20):
            shapes.pop(i)

def ball_collide():  #DEĞİŞECEK
    global fps,movement
    if (ball.midright[0]>=player2.midleft[0] and abs(ball.midright[1]-player2.midleft[1])<=50) or (ball.midleft[0]<=player1.midright[0] and abs(ball.midleft[1]-player1.midright[1])<=50):
        ball.vx = -ball.vx
        fps += 5
        movement -= 0.5

def game_over(): #DEĞİŞECEK
    print("GAME OVER")

#def spawn_power():

player1 = Player(0,250,(255,255,255),0)
player2 = Player(SCREEN_X-10,250,(255,255,255),0)
ball = Ball(SCREEN_X/2,SCREEN_Y/2,0,2,(255,255,255),4)
shapes=[]
fps = 80
movement = 5

while True:

    screen.fill(0)
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    if ball.vx == 0: ball.vx = randint(-1,1)

    ball.move()
    player_move()    

    ball_collide()

    if (ball.x < 0): reset(2)
    elif (ball.x > SCREEN_X): reset(1) 
       

    if player1.point==3 or player1.point==3:
        game_over()
        break
        
    draw_shapes()
    pygame.display.update(player1,player2,ball)
