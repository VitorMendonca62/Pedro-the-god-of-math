import pygame
from pygame.locals import *
from map import *
from sys import exit
from level import *

pygame.init()

game_running = True

width = 640
height = 640

screen_center = (width / 2, height / 2)
zoom = 1

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Teste")
clock = pygame.time.Clock()

map = Map(screen)



while game_running:
  screen.fill((0,0,0))      

  player = pygame.draw.rect(screen, (232,123,123), (screen_center[0] - 20, screen_center[1] - 20,20*zoom,20*zoom))  
  map.update(player)
  
  clock.tick(30)
  pygame.display.update()

