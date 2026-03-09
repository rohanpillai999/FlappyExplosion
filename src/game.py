import pygame
import random
from enum import Enum

from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class GameState(Enum):
    PLAYING = 1
    GAME_OVER = 2
    MENU = 3

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("src/assets/flappy.png").convert()
        self.rect = self.surf.get_rect()
        self.last_jump = 0
        self.speed = 0
    def update(self, jumped):
        if jumped:
            if pygame.time.get_ticks() - self.last_jump >= 90:
                self.speed -= 30
                self.last_jump = pygame.time.get_ticks()
        
        self.speed += 5
        self.rect.move_ip(0, self.speed)
        
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            return True
        return False
    def reset(self):
        self.rect.left = SCREEN_WIDTH // 2
        self.rect.top = SCREEN_HEIGHT // 2



# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the 'player'
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

clock = pygame.time.Clock()

state = GameState.MENU

while running:
    # events = pygame.event.get()
    pressed_keys = pygame.key.get_pressed()
    
    

    if state == GameState.MENU:

        if pressed_keys[K_p]:
            state = GameState.PLAYING
            player.reset()
        screen.fill((0, 0, 0))
    elif state == GameState.GAME_OVER:
        if pressed_keys[K_ESCAPE]:
            state = GameState.MENU
        screen.fill((255, 0, 0))
    elif state == GameState.PLAYING:
        dead = False

        if pressed_keys[K_UP]:
            dead = player.update(True)
        else:
            dead = player.update(False)

        screen.fill((135, 206, 250))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        if dead:
            state = GameState.GAME_OVER
    
    pygame.display.flip()
    
    clock.tick(30)