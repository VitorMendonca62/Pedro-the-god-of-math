import pygame
from pygame.locals import *
from map import *
from sys import exit
from level import *
from colors import *
from player import *
from collectibles import *
from score import *

width = 900
height = 600
screen = pygame.display.set_mode((width,height))

def main_game():
  pygame.init()

  game_running = True

  screen = pygame.display.set_mode((width,height))
  pygame.display.set_caption("Pedro: The God of Math")
  clock = pygame.time.Clock()

  map = Map(screen)

  screen.blit(map.background, (0, 0))
  player = Player(307, 298) 
  all_sprites = pygame.sprite.Group()
  all_sprites.add(player)

  # prevenindo contra erro de quantidade de coletáveis
  if map.works:
    play = True

  else:
    play = False
    print("\n\nSe liga pq falhou:\n")
    print("Não tem espaço para todos esses coletáveis no labirinto.\n\nVá com calma :)\n\nDiminua a quantidade de coletáveis que dá certo.\n\n")

  while game_running and play:
    screen.fill((0,0,0))    
    all_sprites.update()
    map.update(player)
    player_movement(player)       
    all_sprites.draw(screen)
    
    #desenhando o placar
    show_score(map)

    clock.tick(30)
    pygame.display.update()
