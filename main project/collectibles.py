import pygame
import random
from colors import *
    # self.rect = pygame.draw.rect(screen,self.color,(x,colle_y,20,20))

class Collectible():
  def __init__(self, item):
    self.item = item
    self.all_collectibles = list()
    self.rect = pygame.Rect(0,0, 0, 0)
    
    self.row = 0
    self.column = 0

    if item == "r": self.color = red
    if item == "g": self.color = green
    if item == "b": self.color = blue
    if item == "y": self.color = yellow

    choice = self.take_choice(item)
    self.row = random.choice(choice[0])
    self.column = random.choice(choice[1])

  def analyze_collision(self, player,matriz):
    if player.colliderect(self.rect):
      matriz[self.row][self.column] = matriz[self.row][self.column][:-1]
    return player.colliderect(self.rect)

  def take_choice(self, item):
    interval0_6 = range(0,6)
    interval7_14 =  range(7,14)
    if item == "r": return [interval0_6, interval0_6]
    if item == "g": return [interval7_14, interval0_6]
    if item == "b": return [interval0_6, interval7_14]
    if item == "y": return [interval7_14, interval7_14]
