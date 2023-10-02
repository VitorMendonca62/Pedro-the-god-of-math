import pygame
from pygame.locals import *
from map import *
from sys import exit
from level import *
from colors import *
from player import *
from collectibles import *

width = 900
height = 600
screen = pygame.display.set_mode((width,height))

dif = 130
ini_symbol = 450-(dif*2)
ini_text = ini_symbol + 25

def draw_text(text, size, color, x, y):
  font = pygame.font.Font(None, size)
  text = font.render(text, True, color)
  screen.blit(text, (x, y))
  
def colle_sub(map,symbol,index,name):
  screen.blit(name,(ini_symbol + dif*index, height-27,20,20))
  draw_text(f"({map.collected[symbol]}/{map.symbols_collectibles[symbol]})",30,white,ini_text+dif*index,height-27)

def show_collection(map):
  pygame.draw.rect(screen,(120,120,120),(0,height-40,width,40))

  colle_sub(map,'N',0,Collectible.naturals)
  colle_sub(map,'Z',1,Collectible.integers)
  colle_sub(map,'Q',2,Collectible.racionals)
  colle_sub(map,'R',3,Collectible.reals)

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
    show_collection(map)

    clock.tick(30)
    pygame.display.update()
