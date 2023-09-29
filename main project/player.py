import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/player_stopped.png'))
        self.sprites.append(pygame.image.load('sprites/player_stopped_up.png'))
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
        self.current_sprite = 0
        self.up = 1
        self.right = 4
        self.left = 7
        self.down = 10
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (13*2, 21*2))
        self.rect = self.image.get_rect()
        self.rect.topleft = 307, 298


    def baixo(self, x, y):
        self.image = self.sprites[int(self.current_sprite)]
        self.current_sprite += 0.25       
        if self.current_sprite >= 13:
            self.current_sprite = 11
        self.rect.topleft = x, y
        self.image = pygame.transform.scale(self.image, (13*2, 22*2))    
    def cima(self, x, y):
        self.image = self.sprites[int(self.current_sprite)]
        self.current_sprite += 0.25       
        if self.current_sprite >= 4:
            self.current_sprite = 2
        self.rect.topleft = x, y
        self.image = pygame.transform.scale(self.image, (13*2, 22*2))    
    def direita(self, x, y):
        self.image = self.sprites[int(self.current_sprite)] 
        self.current_sprite += 0.25         
        if self.current_sprite >= 7:
            self.current_sprite = 5
        self.rect.topleft = x, y
        self.image = pygame.transform.scale(self.image, (13*2, 23*2))      
    def esquerda(self, x, y):
        self.image = self.sprites[int(self.current_sprite)]   
        self.current_sprite += 0.25      
        if self.current_sprite >=10:
            self.current_sprite = 8
        self.rect.topleft = x, y 
        self.image = pygame.transform.scale(self.image, (13*2, 22*2))           
    def parado(self, x, y):
        self.image = self.sprites[0]
        self.rect.topleft = x, y
        self.image = pygame.transform.scale(self.image, (13*2, 22*2))
        
    
#linha 730
