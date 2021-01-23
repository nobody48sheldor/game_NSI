import pygame
import time
from math import *
import numpy as np

pygame.init()
pygame.display.set_caption("game_nsi")
screen = pygame.display.set_mode((800,600))
t = 0

background = pygame.image.load('img/background_menu.png')
screen.blit(background,(0, 0))

class game:
    def __init__(self):
        self.player = player()
        self.key_pressed = {}

    def update(self, screen):
        screen.blit(game.player.image, game.player.rect)
        if self.key_pressed.get(pygame.K_UP) == True:
            self.player.forward()

        if self.key_pressed.get(pygame.K_DOWN) == True:
            self.player.backward()

        if self.key_pressed.get(pygame.K_RIGHT) == True:
            self.player.right()

        if self.key_pressed.get(pygame.K_LEFT) == True:
            self.player.left()

class player:
    def __init__(self):
        self.velocity = 5
        self.image = pygame.image.load('img/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 260


    def forward(self):
        self.rect.y += -self.velocity
        print("z", self.rect.x, self.rect.y)

    def backward(self):
        self.rect.y += self.velocity
        print("s", self.rect.x, self.rect.y)

    def right(self):
        self.rect.x += self.velocity
        print("d", self.rect.x, self.rect.y)

    def left(self):
        self.rect.x += -self.velocity
        print("q", self.rect.x, self.rect.y)


running = True

game.__init__(game)
player.__init__(player)
game()
player()

while running == True:
    screen.blit(background,(0, 0))
    game.update(game, screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            game.key_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.key_pressed[event.key] = False
