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
        self.destroy()

    def movement(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed
    def destroy(self):
        self.kill() if self.rect.right > 1350 else None
        self.kill() if self.rect.left < -50 else None
        self.kill() if self.rect.top < -50 else None
        self.kill() if self.rect.bottom > 780 else None

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

spaceship = SpaceShip('game-assets/spaceship.png', 640, 500, 10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor_group = pygame.sprite.Group()
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == METEOR_EVENT:
            random_meteor = random.choice(['game-assets/Meteor1.png', 'game-assets/Meteor2.png', 'game-assets/Meteor3.png'])
            random_xpos = random.randrange(1, 1280)
            random_ypos = random.randrange(1, 50)
            random_xspeed = random.randrange(-5, 5)
            random_yspeed = random.randrange(1, 5)
            random_meteor = Meteor(random_meteor, random_xpos, random_ypos, random_xspeed, random_yspeed)
            meteor_group.add(random_meteor)

    screen.fill((45, 45, 60))

    meteor_group.draw(screen)
    meteor_group.update()

    spaceship_group.draw(screen)
    spaceship_group.update()

    pygame.display.update()
    clock.tick(120)
