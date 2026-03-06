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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("src/assets/flappy.png").convert()
        self.rect = self.surf.get_rect()
        self.last_jump = 0
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            if pygame.time.get_ticks() - self.last_jump >= 90:
                self.rect.move_ip(0, -30)
                self.last_jump = pygame.time.get_ticks()
        self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

clock = pygame.time.Clock()

state = GameState.MENU

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                state = GameState.MENU
            elif event.key == K_p:
                state = GameState.PLAYING

    if state == GameState.PLAYING:
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        screen.fill((135, 206, 250))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        if player.rect.bottom >= SCREEN_HEIGHT:
            state = GameState.GAME_OVER
            player.rect.left = 0
            player.rect.top = 0
    elif state == GameState.GAME_OVER:
        screen.fill((255, 0, 0))
    elif state == GameState.MENU:
        screen.fill((0, 0, 0))
    
    pygame.display.flip()
    
    clock.tick(30)