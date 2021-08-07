import pygame,sys,os
import random

from pygame.constants import K_a, K_d, K_s, K_w, MOUSEBUTTONDOWN

pygame.init()

RED=(255,0,0)
WHITE=(255,255,255)
font=pygame.font.SysFont('comicsansms',20)
clock = pygame.time.Clock()
widht,height=600,600
screen=pygame.display.set_mode((widht,height))
pygame.display.set_caption("racing")
FPS=60
highScore=0
Score=0
carx=200
cary=500
vel=5
velObs=5
obsCooldawn=150


#load game assets
blueCar=pygame.image.load(os.path.join("C:\\Users\\E6420\\Desktop\\vsCode\\pygame\\assets\\blueCar.png"))
greenCar=pygame.image.load(os.path.join("C:\\Users\\E6420\\Desktop\\vsCode\\pygame\\assets\\gCar.png"))
greenCar=pygame.transform.scale(greenCar,(100,50))
greenCar=pygame.transform.rotate(greenCar,90)#scale background
yellowCar=pygame.image.load(os.path.join("C:\\Users\\E6420\\Desktop\\vsCode\\pygame\\assets\\\yellowCar.png"))
yellowCar=pygame.transform.scale(yellowCar,(80,50))
yellowCar=pygame.transform.rotate(yellowCar,-90)#scale background
racingRoad=pygame.image.load(os.path.join("C:\\Users\\E6420\\Desktop\\vsCode\\pygame\\assets\\racingRoad.png"))
racingRoad=pygame.transform.scale(racingRoad,(400,600))
woodBackground=pygame.image.load(os.path.join("C:\\Users\\E6420\\Desktop\\vsCode\\pygame\\assets\\woodback.png"))#import background
woodBackground=pygame.transform.scale(woodBackground,(200,700))#scale background
blackCar=pygame.image.load(os.path.join("C:\\Users\\E6420\\Desktop\\vsCode\\pygame\\assets\\blackCar.png"))
barrel=pygame.image.load(os.path.join("C:\\Users\\E6420\\Desktop\\vsCode\\pygame\\assets\\barrel.png"))
roadStop=pygame.image.load(os.path.join("C:\\Users\\E6420\\Desktop\\vsCode\\pygame\\assets\\roadStop.png"))
scorePannel=pygame.image.load(os.path.join("C:\\Users\\E6420\\Desktop\\vsCode\\pygame\\assets\\scorePannel.png"))#import background
scorePannel=pygame.transform.scale(scorePannel,(150,150))




def drawText(text,font,color,surface,x,y):
    textObj=font.render(str(text),1,color)
    textRect=textObj.get_rect()
    textRect.topleft=(x,y)
    surface.blit(textObj,textRect)


def main():
    global carx,cary,obsCooldawn,Score,velObs
    run=True
    lives=3
    alive=True
    obsticleImages=[yellowCar,barrel,roadStop,blackCar]
    obsticlesx=[110,160,210,260]
    while run:
        clock.tick(FPS)
        screen.blit(racingRoad,(0,0))
        screen.blit(woodBackground,(400,0))
        carRect=pygame.Rect(carx,cary,50,100)
        screen.blit(greenCar,(carx,cary))

        #car mouvements
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a] and carx>80:
            carx-=vel
        if keys[pygame.K_d] and carx<280:
            carx+=vel
        if keys[pygame.K_s] and cary<height-100:
            cary+=vel
        if keys[pygame.K_w] and cary>0:
            cary-=vel   

        
        #obsticle generation
        if obsCooldawn==150:
            obsticley=0
            obsticlex=random.choice(obsticlesx)
            obsticleImage=random.choice(obsticleImages)
            obsCooldawn=0
            if obsticleImage==obsticleImages[0]:
                obsticleWight=50
                obsticleHeight=75
            if obsticleImage==obsticleImages[1]:
                obsticleWight=35
                obsticleHeight=55        
            if obsticleImage==obsticleImages[2]:
                obsticleWight=55
                obsticleHeight=25
            if obsticleImage==obsticleImages[3]:
                obsticleWight=35
                obsticleHeight=60
            velObs+=1

        obsticleRect=pygame.Rect(obsticlex,obsticley,obsticleWight,obsticleHeight)
        #pygame.draw.rect(screen,WHITE,obsticleRect,0,0)
        screen.blit(obsticleImage,(obsticlex,obsticley))
        obsticley+=velObs 
        obsCooldawn+=1



        #collision with obsticles
        if carRect.colliderect(obsticleRect):
            lives-=1
            if lives==0:
                sys.exit()
            #drawText("YOU LOSE",font,RED,screen,200,300)
            #drawText("press R to restart",font,RED,screen,200,350)




        #score display
        screen.blit(scorePannel,(425,100))
        drawText("CurrentScore :",font,WHITE,screen,450,50)
        drawText(Score,font,WHITE,screen,500,150)
        #drawText(lives,font,RED,screen,500,300)


        if alive:
            Score+=1
        
        #main loop
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
                sys.exit()
   



        pygame.display.update()
    pygame.quit()
    sys.exit()
        
        
#start        
main()