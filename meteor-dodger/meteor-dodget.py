import sys
import pygame
import math
import random

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constrain()

    def screen_constrain(self):
        self.rect.right = 1280 if self.rect.right >= 1280 else self.rect.right
        self.rect.left = 0 if self.rect.left <= 0 else self.rect.left
        self.rect.top = 0 if self.rect.top <= 0 else self.rect.top
        self.rect.bottom = 720 if self.rect.bottom >= 720 else self.rect.bottom

class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, x_speed, y_speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.movement()

    def movement(self):
        self.rect.centerx = 50 * math.sin(2*3.1416*(self.x_speed/160)*self.rect.centery) + 640
        self.rect.centery += self.y_speed

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

spaceship = SpaceShip('game-assets/spaceship.png', 640, 500, 10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor = Meteor('game-assets/Meteor1.png', 640, 0, 1, 1)
meteor_group = pygame.sprite.Group()
meteor_group.add(meteor)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((45,45,60))

    meteor_group.draw(screen)
    meteor_group.update()

    spaceship_group.draw(screen)
    spaceship_group.update()

    pygame.display.update()
    clock.tick(120)
