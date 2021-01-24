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
        self.rocket = rocket()
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

        if rocket.rocket_launch_C == True:
            screen.blit(self.rocket.image, self.rocket.rect)

class player:
    def __init__(self):
        self.velocity = 5
        self.image = pygame.image.load('img/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 260
        self.rocket = 5


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


class rocket:
    def __init__(self):
        self.v = 0
        self.velocity = 50
        self.image = pygame.image.load('img/rocket.png')
        self.rect = self.image.get_rect()
        self.rect.x = game.player.rect.x
        self.rect.y = game.player.rect.y
        self.rocket_launch_C = False

    def rocket_launch(self):
        print(self.v)
        if self.v < self.velocity:
            self.rect.x = self.rect.x + (diff_x)
            self.rect.y = self.rect.y + (diff_y)
            self.v = self.v + 1
        if self.v == self.velocity:
            print("a")



running = True

game.__init__(game)
player.__init__(player)
rocket.__init__(rocket)
game()
player()
rocket()

while running == True:
    screen.blit(background,(0, 0))
    game.update(game, screen)
    pygame.display.flip()

    if rocket.rocket_launch_C == True:
        game.rocket.rocket_launch()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            game.key_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.key_pressed[event.key] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            game.player.rocket = game.player.rocket - 1
            mouse_pos = pygame.mouse.get_pos()
            player_pos = (game.player.rect.x, game.player.rect.y)
            diff_x = int((mouse_pos[0] - game.player.rect.x)/rocket.velocity)
            diff_y = int((mouse_pos[1] - game.player.rect.y)/rocket.velocity)
            rocket.v = 0
            rocket.__init__(rocket)
            rocket.rocket_launch_C = True
            print("exec")
