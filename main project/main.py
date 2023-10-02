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

def desenhar_texto(texto, tamanho, cor, x, y):
    fonte = pygame.font.Font(None, tamanho)
    texto = fonte.render(texto, True, cor)
    screen.blit(texto, (x, y))

def show_collection(map):
  pygame.draw.rect(screen,(120,120,120),(0,height-40,width,40))

  dif = 130
  ini_symbol = 450-(dif*2)
  ini_text = ini_symbol + 25

  screen.blit(Collectible.naturals,(ini_symbol, height-27,20,20))
  desenhar_texto(f"({map.collected['N']}/{map.symbols_collectibles['N']})",30,white,ini_text,height-27)
  
  screen.blit(Collectible.integers,(ini_symbol + dif,height-27,20,20))
  desenhar_texto(f"({map.collected['Z']}/{map.symbols_collectibles['Z']})",30,white,ini_text+dif*1,height-27)
  
  screen.blit(Collectible.racionals,(ini_symbol + dif*2,height-27,20,20))
  desenhar_texto(f"({map.collected['Q']}/{map.symbols_collectibles['Q']})",30,white,ini_text+dif*2,height-27)
  
  screen.blit(Collectible.reals,(ini_symbol + dif*3,height-27,20,20))
  desenhar_texto(f"({map.collected['R']}/{map.symbols_collectibles['R']})",30,white,ini_text+dif*3,height-27)

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
