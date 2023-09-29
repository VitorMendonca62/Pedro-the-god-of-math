import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/player_stopped.png'))
        self.sprites.append(pygame.image.load('sprites/player_stopped_up1.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_up1.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_up2.png'))
        self.sprites.append(pygame.image.load('sprites/player_stopped_right.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_right1.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_right2.png'))
        self.sprites.append(pygame.image.load('sprites/player_stopped_left.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_left1.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_left2.png'))
        self.sprites.append(pygame.image.load('sprites/player_stopped.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_down1.png'))
        self.sprites.append(pygame.image.load('sprites/player_walking_down2.png'))
        self.stopped = 0
        self.up = 1
        self.right = 4
        self.left = 7
        self.down = 10
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
    def baixo(self, x, y):
        self.image = self.sprites[int(self.current_sprite)]
        self.current_sprite += 0.2       
        if self.current_sprite >= len(self.current_sprite):
            self.current_sprite = 11
        self.rect.topleft = x, y    
    def cima(self, x, y):
        self.image = self.sprites[int(self.current_sprite)]
        self.current_sprite += 0.2          
        if self.current_sprite > 3:
            self.current_sprite = 2
        self.rect.topleft = x, y    
    def direita(self, x, y):
        self.image = self.sprites[int(self.current_sprite)] 
        self.current_sprite += 0.2         
        if self.current_sprite > 6:
            self.current_sprite = 5
        self.rect.topleft = x, y       
    def esquerda(self, x, y):
        self.image = self.sprites[int(self.current_sprite)]   
        self.current_sprite += 0.2       
        if self.current_sprite > 9:
            self.current_sprite = 8
        self.rect.topleft = x, y    
        
    def parado(self):
        if self.current_sprite == 11 or self.current_sprite == 12:
            self.current_sprite = 10
        elif self.current_sprite == 2 or self.current_sprite == 3:
            self.current_sprite = 1
        elif self.current_sprite == 5 or self.current_sprite == 6:
            self.current_sprite = 4
        elif self.current_sprite == 8 or self.current_sprite == 9:
            self.current_sprite = 7
    
#linha 730
