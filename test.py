import pygame
from pygame.locals import *

pygame.init()

Screen_Width = 300
Screen_Height = 300
X = 300
Y = 300
grid = (255,0,0)


screen = pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("Test")

def Cross():
    pygame.draw.line(screen, grid, (X,0), (0,Y), 10)
    pygame.draw.line(screen, grid, (0,0), (X,Y), 10)
    pygame.draw.circle(screen, grid, (X/2,Y/2), 100, 10)


clicked = False
running = True


while running:
    Cross()
    for event in pygame.event.get():
        if running == False:
            pygame.QUIT
        if event.type == pygame.MOUSEBUTTONUP and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == True:
            clicked = False
            running = False

    pygame.display.update()
pygame.quit()