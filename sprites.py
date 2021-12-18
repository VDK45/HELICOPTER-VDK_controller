import pygame
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

helicopter_1 = resource_path('sprites/helicopter_1.png')
helicopter_2 = resource_path('sprites/helicopter_2.png')
helicopter_crash_1 = resource_path('sprites/helicopter_crash_1.png')
helicopter_crash_2 = resource_path('sprites/helicopter_crash_2.png')
helicopter_crash_3 = resource_path('sprites/helicopter_crash_3.png')
helicopter_crash_4 = resource_path('sprites/helicopter_crash_4.png')
helicopter_damaged_1 = resource_path('sprites/helicopter_damaged_1.png')
helicopter_damaged_2 = resource_path('sprites/helicopter_damaged_2.png')

enemy_helicopter_1 = resource_path('sprites/enemy_helicopter_1.png')
enemy_helicopter_2 = resource_path('sprites/enemy_helicopter_2.png')

boat_r = resource_path('sprites/boat.png')
boat = pygame.image.load(boat_r)

helicopter_1 = pygame.image.load(helicopter_1)
helicopter_2 = pygame.image.load(helicopter_2)
helicopter_crash_1 = pygame.image.load(helicopter_crash_1)
helicopter_crash_2 = pygame.image.load(helicopter_crash_2)
helicopter_crash_3 = pygame.image.load(helicopter_crash_3)
helicopter_crash_4 = pygame.image.load(helicopter_crash_4)
helicopter_damaged_1 = pygame.image.load(helicopter_damaged_1)
helicopter_damaged_2 = pygame.image.load(helicopter_damaged_2)

enemy_helicopter_1 = pygame.image.load(enemy_helicopter_1)
enemy_helicopter_2 = pygame.image.load(enemy_helicopter_2)


helicopter_list = [helicopter_1, helicopter_2]
damaged_helicopter_list = [helicopter_damaged_1, helicopter_damaged_2]
enemy_helicopter_list = [enemy_helicopter_1, enemy_helicopter_2]

balloon = resource_path('sprites/balloon.png')
balloon = pygame.image.load(balloon)

spaceship = resource_path('sprites/spaceship.png')
spaceship = pygame.image.load(spaceship)

icon = resource_path('sprites/icon.png')
icon = pygame.image.load(icon)
background = resource_path('sprites/background.png')
background = pygame.image.load(background)
cloud = resource_path('sprites/cloud.png')
cloud = pygame.image.load(cloud)

all_sprites = [helicopter_1, helicopter_2, helicopter_damaged_1, helicopter_damaged_2, enemy_helicopter_1,
               enemy_helicopter_2, helicopter_crash_1, helicopter_crash_2, helicopter_crash_3, helicopter_crash_4,
               boat, balloon, spaceship, icon, background, cloud]


