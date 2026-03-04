import pygame
from enum import Enum

from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class GameState(Enum):
    PLAYING = 1
    GAME_OVER = 2
    MENU = 3

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

state = GameState.MENU

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                state = GameState.MENU
            elif event.key == K_p:
                state = GameState.PLAYING

    if state == GameState.PLAYING:
        screen.fill((135, 206, 250))
    elif state == GameState.GAME_OVER:
        screen.fill((0, 0, 0))
    elif state == GameState.MENU:
        screen.fill((0, 0, 0))
    
    pygame.display.flip()