import pygame
import random


# Para escolher a quantidade de coletáveis, vá em map
# Modifique os números no dicionário symbols_collectibles

class Collectible():
  
  def __init__(self, item):
    size = 250/11
    self.naturals = pygame.image.load('sprites/naturals.png')
    self.naturals = pygame.transform.scale(self.naturals, (size, size))
    self.integers = pygame.image.load('sprites/integer.png')
    self.integers = pygame.transform.scale(self.integers, (size, size))
    self.racionals = pygame.image.load('sprites/racionals.png')
    self.racionals = pygame.transform.scale(self.racionals, (size, size))
    self.reals = pygame.image.load('sprites/reals.png')
    self.reals = pygame.transform.scale(self.reals, (size, size))

    self.item = item
    self.all_collectibles = list()
    self.rect = pygame.Rect(0,0, 0, 0)
    self.collected = False

    if item == "N": 
      self.sets = self.naturals
      self.name = "Naturals"
    if item == "Z": 
      self.sets = self.integers
      self.name = "Integers"
    if item == "Q": 
      self.sets = self.racionals
      self.name = "Racionals"
    if item == "R": 
      self.sets = self.reals
      self.name = "Reals"

    self.row = random.choice(range(0,14))
    self.column = random.choice(range(0,14))

    self.adress = (self.row,self.column)