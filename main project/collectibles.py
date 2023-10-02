import pygame
from random import choice, randint

symbols_collectibles = {
  "N": randint(1,3),
  "Z": randint(3,5),
  "Q": randint(2,4),
  "R": randint(1,3)
  }
  
class Collectible():
  size = 250/11
  naturals = pygame.image.load('sprites/naturals.png')
  naturals = pygame.transform.scale(naturals, (size, size))
  integers = pygame.image.load('sprites/integer.png')
  integers = pygame.transform.scale(integers, (size, size))
  racionals = pygame.image.load('sprites/racionals.png')
  racionals = pygame.transform.scale(racionals, (size, size))
  reals = pygame.image.load('sprites/reals.png')
  reals = pygame.transform.scale(reals, (size, size))
  
  def __init__(self, item):

    self.item = item
    self.all_collectibles = list()
    self.rect = pygame.Rect(0,0, 0, 0)
    self.collected = False

    if item == "N": 
      self.sets = Collectible.naturals
      self.name = "Naturals"
    if item == "Z": 
      self.sets = Collectible.integers
      self.name = "Integers"
    if item == "Q": 
      self.sets = Collectible.racionals
      self.name = "Racionals"
    if item == "R": 
      self.sets = Collectible.reals
      self.name = "Reals"

    self.row = choice(range(0,14))
    self.column = choice(range(0,14))

    self.adress = (self.row,self.column)
