import pygame
import math
import random as rand

black = (0, 0, 0)

pink = (255, 130, 190)
pink1 = (245, 165, 250)

pink2 = (255, 140, 200)


class uwus():
    uwu = pygame.sprite.Sprite
    def __init__(self):
        self.uwu.image = pygame.image.load("C:/Users/hunor/Downloads/uwu.png")

    
        

        self.uwu.rect = self.uwu.image.get_rect()
        self.uwu.rect.x = 2
        self.uwu.rect.y = 2        
        
        self.dx=4
        self.dy = 2

    def movement(self):

        
        if self.uwu.rect.x <= 0 or self.uwu.rect.x >= 402:
            self.dx = self.dx*(-1)

        if self.uwu.rect.x == 402:
            self.uwu.rect.y = 500

        if self.uwu.rect.x == 2:
            self.uwu.rect.y = 2



        if 1 == 1:
            self.uwu.rect.x = self.uwu.rect.x + self.dx            


    def draw(self, surface):
        surface.blit(self.uwu.image, (self.uwu.rect.x,  self.uwu.rect.y))
        
        if self.uwu.rect.x == 402:
            screen.fill((255, 253, 201), (402, 0, 200, 100))

        if self.uwu.rect.x == 2:
            screen.fill((255, 253, 201), (0, 500, 200, 100))





pygame.init()
screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("HAPPY LATE VALENTINES DAY LMAO    i love you uwu")

clock = pygame.time.Clock()

uwus = uwus()

t0 = (-math.pi)/2
t = 0
t1 = (math.pi)/2
t2 = math.pi

dt = 0.15


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            
    

    uwus.movement()

    if t == 0:
        screen.fill((255, 253, 201))

    uwus.draw(screen)

    
        
    if 1 == 1:
        #time step
        t0 += dt
        t += dt
        t1 += dt
        t2 += dt
        
        #===============================heart points===================================#
        x0 = int(300 + 10*16*(math.sin(t0)*math.sin(t0)*math.sin(t0)))
        y0 = int(300 - 10*(13*math.cos(t0) - 5*math.cos(2*t0) - 2*math.cos(3*t0) - math.cos(4*t0)))
        
        x = int(300 + 10*16*(math.sin(t)*math.sin(t)*math.sin(t)))
        y = int(300 - 10*(13*math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)))

        x1 = int(300 + 10*16*(math.sin(t1)*math.sin(t1)*math.sin(t1)))
        y1 = int(300 - 10*(13*math.cos(t1) - 5*math.cos(2*t1) - 2*math.cos(3*t1) - math.cos(4*t1)))

        x2 = int(300 + 10*16*(math.sin(t2)*math.sin(t2)*math.sin(t2)))
        y2 = int(300- 10*(13*math.cos(t2) - 5*math.cos(2*t2) - 2*math.cos(3*t2) - math.cos(4*t2)))

    #==================heart=====================#
    pygame.draw.circle(screen, pink, (x, y), 3)
    pygame.draw.line(screen, pink1, [300, 250], [x0, y0], 5)
    pygame.draw.line(screen, pink2, [300, 250], [x, y], 5)
    pygame.draw.line(screen, pink1, [300, 250], [x1, y1], 5)
    pygame.draw.line(screen, pink2, [300, 250], [x2, y2], 5)
    #=============================================#
    pygame.display.flip()
        
    clock.tick(60)