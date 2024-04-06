import pygame
from random import randint
from utils.sprites import place_sprites_collectibles

symbols_collectibles = {
  0: {
    "N": randint(1,3),
    "Z": randint(3,5),
    "Q": randint(2,4),
    "R": randint(1,3)
  },
  1: {
    "N": randint(2,4),
    "Z": randint(4,6),
    "Q": randint(3,5),
    "R": randint(2,4)
  },
  2: {
    "N": randint(3,5),
    "Z": randint(5,7),
    "Q": randint(4,6),
    "R": randint(3,5)
  },
}
class Collectible():
  size = 270 / 8
  sprites = place_sprites_collectibles(size)
  
  def __init__(self, item):
    sprites = Collectible.sprites
    
    self.item = item
    self.all_collectibles = list()
    self.rect = pygame.Rect(0,0, 0, 0)
    self.collected = False

    if item == "N": 
      self.sets = sprites[0]
      self.name = "Naturals"
    elif item == "Z": 
      self.sets = sprites[1]
      self.name = "Integers"
    elif item == "Q": 
      self.sets = sprites[2]
      self.name = "Racionals"
    elif item == "R": 
      self.sets = sprites[3]
      self.name = "Reals"

    self.row = randint(0,14)
    self.column = randint(0,14)

    self.adress = (self.row,self.column)
