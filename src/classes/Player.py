import pygame
from pygame.locals import *
from utils.sprites import take_sprites_player

class Player(pygame.sprite.Sprite):
  def __init__(self,coords_initial):
    pygame.sprite.Sprite.__init__(self)
    self.sprites = take_sprites_player() #Lista para armazenar todas as sprites do personagem

    self.current_sprite = 0
    self.current_up = 1
    self.current_right = 4
    self.current_left = 7
    self.current_down = 10
    self.image = self.sprites[self.current_sprite]

    self.coords_initial = coords_initial
    self.size = (21, 36)
      
  def draw_player(self):
    self.image = pygame.transform.scale(self.image, self.size)
    self.rect = self.image.get_rect()
    x = self.coords_initial[0] - (self.size[0] / 2)
    y = self.coords_initial[1] - (self.size[1] / 2)
    self.rect.topleft =  x, y

  #Funções para definir as modificações de sprite de acordo com o movimento desejado
  def down(self): 
    self.image = self.sprites[int(self.current_down)]
    self.current_down += 0.25       
    if self.current_down > 12.2:
      self.current_down = 10
    self.image = pygame.transform.scale(self.image, self.size) 

  def up(self):
    self.image = self.sprites[int(self.current_up)]
    self.current_up += 0.25       
    if self.current_up >= 4:
        self.current_up = 1
    self.image = pygame.transform.scale(self.image, self.size)  

  def right(self):
    self.image = self.sprites[int(self.current_right)] 
    self.current_right += 0.25        
    if self.current_right >= 7:
        self.current_right = 4
    self.image = pygame.transform.scale(self.image, self.size)  

  def left(self):
    self.image = self.sprites[int(self.current_left)]   
    self.current_left += 0.25      
    if self.current_left >= 10:
        self.current_left = 7 
    self.image = pygame.transform.scale(self.image, self.size)      

  def player_movement(self):
    keys = pygame.key.get_pressed()
    if keys[K_w] or keys[K_s]:
      if keys[K_w]:
        self.up()
      if keys[K_s]:
        self.down()

    if keys[K_a] or keys[K_d]:
      if keys[K_a]:
        self.left()
      if keys[K_d]:
        self.right()    

  def update(self): 
    self.player_movement()
    self.draw_player()
  