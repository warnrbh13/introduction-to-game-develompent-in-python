import pygame
import sys
import random

pygame.init()  # Instantiates the game itself
pygame.mouse.set_visible(False)     # All related with mouse is with pygame.mouse

screen = pygame.display.set_mode((1280, 720))  # Creates display screen, mode seems to set the size
clock = pygame.time.Clock()  # Determines the maximum fps
wood_bg = pygame.image.load('shooting range assets/Wood_BG.png')  # Store images from program directory and stores it
land_bg = pygame.image.load('shooting range assets/Land_BG.png')
water_bg = pygame.image.load('shooting range assets/Water_BG.png')
cloud1_bg = pygame.image.load('shooting range assets/Cloud1.png')
cloud2_bg = pygame.image.load('shooting range assets/Cloud2.png')

crosshair = pygame.image.load('shooting range assets/crosshair.png')
duck_surface = pygame.image.load('shooting range assets/duck.png')
game_font = pygame.font.Font(None, 200) # Params are font and size

text_surface = game_font.render('You Won!', True, (255, 255, 255))
text_rect = text_surface.get_rect(center = (screen.get_width()/2, screen.get_height()/2))

land_position_y = 560
land_speed = 0.45

water_position_y = 640
water_speed = 1

duck_list = []
for duck in range(10):
    duck_position_x = random.randrange(50, 1200)
    duck_position_y = random.randrange(120, 600)
    duck_rect = duck_surface.get_rect(center = (duck_position_x, duck_position_y))
    duck_list.append(duck_rect)

cloud1_list = []
num_of_duck = 4
for cloud in range(num_of_duck):
    cloud_position_x = random.randrange(50, screen.get_width()-50)
    cloud_position_y = random.randrange(50, screen.get_height()/3)
    cloud_rect = cloud1_bg.get_rect(center = (cloud_position_x, cloud_position_y))
    cloud1_list.append(cloud_rect)

cloud2_list = []
for cloud in range(num_of_duck):
    cloud_position_x = random.randrange(50, screen.get_width()-50)
    cloud_position_y = random.randrange(50, screen.get_height()/3)
    cloud_rect = cloud2_bg.get_rect(center = (cloud_position_x, cloud_position_y))
    cloud2_list.append(cloud_rect)

crosshair_rect = crosshair.get_rect()
while True:
    for event in pygame.event.get():  # I guess it iterates from all kind of events, event detection can mean an
        if event.type == pygame.QUIT:  # output detection can be done with if statements looking for events
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos) # This is where rectangle is created for an image

        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, duck_rect in enumerate(duck_list):
                if duck_rect.collidepoint(event.pos):
                    duck_list.pop(index)

    screen.blit(wood_bg, (0, 0))  # Logical operation in which a block of data is rapidly moved or copied in mem
    for duck_rect in duck_list:
        screen.blit(duck_surface, duck_rect)
    land_position_y += land_speed
    if land_position_y >= 620 or land_position_y <= 500:
        land_speed *= -1
    screen.blit(land_bg, (0, land_position_y))
    water_position_y += water_speed
    if water_position_y >= 660 or water_position_y <= 620:
        water_speed *= -1
    screen.blit(water_bg, (0, water_position_y))
    for index, cloud in enumerate(cloud1_list):
        screen.blit(cloud1_bg, cloud1_list[index])
        screen.blit(cloud2_bg, cloud2_list[index])
    screen.blit(crosshair, crosshair_rect) # The rectangle is what is used to place surface on specific pos
    if not duck_list:
        screen.blit(text_surface, text_rect)
    pygame.display.update()  # Telling python display needs to be refreshed
    clock.tick(120)  # Truncate fps value
