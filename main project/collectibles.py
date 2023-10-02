import pygame
import random

# Para escolher a quantidade de coletáveis, vá em map
# Modifique os números no dicionário symbols_collectibles

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

    self.row = random.choice(range(0,14))
    self.column = random.choice(range(0,14))

    self.adress = (self.row,self.column)
