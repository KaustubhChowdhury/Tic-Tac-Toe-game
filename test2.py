import pygame
from pygame.locals import *

pygame.init()

#All variables used
Screen_Width = 300
Screen_Height = 300
X = 300
Y = 300
bg = (255,255,200)
grid = (50,50,50)
screen_width2 = 10
player = 1
markers = []
green = (255,0,0)
red = (0,255,0)
for x in range(3):
    row = [0]*3
    markers.append(row)

#The main screen
screen = pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("Test2")

#The functions used
def draw_grid():

    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0,x*100), (Screen_Width,x*100), screen_width2)
        pygame.draw.line(screen, grid, (x*100,0), (x*100,Screen_Height), screen_width2)
def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos*100 + 15, y_pos*100 + 15), (x_pos*100 + 85,y_pos*100 +85), screen_width2)
                pygame.draw.line(screen, green, (x_pos*100 +15, y_pos*100 +85), (x_pos*100 +85, y_pos*100 +15), screen_width2)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos*100 +50, y_pos*100 +50), 38 , screen_width2)
            y_pos += 1
        x_pos += 1

clicked = False
running = True

#The main loop
while running:

    draw_grid()
    draw_markers()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if markers[cell_x // 100][cell_y // 100] == 0:
                markers[cell_x // 100][cell_y // 100] = player
                player *= -1
            print(player)
        


    pygame.display.update()
pygame.quit()