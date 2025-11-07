import pygame
import sys

pygame.init()

WIDTH=900
HEIGHT=900

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC TAC TOE")

BOARD = pygame.image.load("assets/TTT.png")
X_IMG = pygame.image.load("assets/X1.png")
O_IMG = pygame.image.load("assets/01.png")

BG_COLOR = (214, 201, 227)

board = [[1,2,3], [4,5,6], [7,8,9]]
graphical_board= [[[None,None], [None,None], [None,None]],
                  [[None,None], [None,None], [None,None],],
                  [[None,None], [None,None], [None,None]]]

to_move = 'X'

SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64,64))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()