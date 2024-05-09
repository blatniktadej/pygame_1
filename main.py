import random

import pygame
from math import hypot
pygame.init()
clock=pygame.time.Clock()
pygame.mouse.set_visible(False)
screen=pygame.display.set_mode((700,400))
pygame.display.set_caption("Moja prva igra!")
ozadje=pygame.image.load("ozadje.jpg").convert_alpha()
font=pygame.font.SysFont("Consolas",32)
target_pos=(100,100)
tocke=0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mous_pos=pygame.mouse.get_pos()
            a=mous_pos[0]-target_pos[0]
            b=mous_pos[1]-target_pos[1]
            h=hypot(a,b)
            if h<=10:
                tocke=tocke+3
                target_pos=(random.randint(30,670),random.randint(30,370))
            elif h <= 20:
                tocke = tocke + 2
                target_pos = (random.randint(30, 670), random.randint(30, 370))
            elif h <= 30:
                tocke = tocke + 1
                target_pos = (random.randint(30, 670), random.randint(30, 370))
            else:
                tocke-=2
                target_pos=(random.randint(30,670),random.randint(30,370))

    screen.blit(ozadje,(0,0))
    #tarča
    pygame.draw.circle(screen,"black",target_pos,30)
    pygame.draw.circle(screen,"white",target_pos,20)
    pygame.draw.circle(screen,"black",target_pos,10)
    target_pos=(target_pos[0]+3,target_pos[1])
    #nariši merček
    mous_pos=pygame.mouse.get_pos()

    pygame.draw.circle(screen,"red",mous_pos,20,2)
    pygame.draw.line(screen,"red",mous_pos,(mous_pos[0],mous_pos[1]-30),2)
    pygame.draw.line(screen,"red",mous_pos,(mous_pos[0],mous_pos[1]+30),2)
    pygame.draw.line(screen,"red",mous_pos,(mous_pos[0]-30,mous_pos[1]),2)
    pygame.draw.line(screen,"red",mous_pos,(mous_pos[0]+30,mous_pos[1]),2)





    text=font.render("Točke:"+str(tocke),True,(255,0,0))
    screen.blit(text,(20,25))




    pygame.display.update()
    clock.tick(60)
