import pygame
from pygame.locals import *
from map import *
from player import Player
from score import *

width = 900
height = 600
screen = pygame.display.set_mode((width,height))

def game():
  pygame.init()

  game_running = True

  screen = pygame.display.set_mode((width,height))
  pygame.display.set_caption("Pedro: The God of Math")
  clock = pygame.time.Clock()

  map = Map(screen)

  screen.blit(map.background, (0, 0))
  player = Player((width/2, height/2)) 
  all_sprites = pygame.sprite.Group()
  all_sprites.add(player)

  # prevenindo contra erro de quantidade de coletáveis

  while game_running:
    screen.fill((0,0,0))    
    all_sprites.update()
    map.update(player)
    player.update()
    all_sprites.draw(screen)
    
    #desenhando o placar
    show_score(screen, map)

    clock.tick(30)
    pygame.display.update()
