import pygame
from pygame.locals import *
from classes.Map import Map
from classes.Player import Player
from classes.Score import Score

width = 900
height = 600
screen = pygame.display.set_mode((width,height))

def game(menu):
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
  
  score = Score()

  while game_running:
    screen.fill((0,0,0))    
    all_sprites.update()
    game_running = not map.update(player, score)
    player.update()
    all_sprites.draw(screen)
    
    score.show(screen, map)

    clock.tick(30)
    pygame.display.update()
    
    if not game_running: 
      score.victory_screen(screen,menu)
