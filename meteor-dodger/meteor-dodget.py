import sys, pygame


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

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

spaceship = SpaceShip('game-assets/spaceship.png', 640, 500, 10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((45,45,60))

    spaceship_group.draw(screen)
    spaceship_group.update()

    pygame.display.update()
    clock.tick(120)
