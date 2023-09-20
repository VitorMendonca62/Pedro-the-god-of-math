import pygame
from random import randint
from level import levels_size

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)

class Collectible:
    def __init__(self, place, color, colle_x, colle_y,id):
        self.rect = pygame.draw.rect(place,color,(colle_x,colle_y,20,20))
        self.color = color
        self.id = id
        self.collected = False
