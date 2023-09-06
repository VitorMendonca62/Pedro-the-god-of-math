import pygame
from pygame.locals import *
from sys import exit

from map import * 

# circulo = pygame.image.load('circulo.png')

pygame.init()

game_running = True

width = 640
height = 640
screen_center = (width / 2, height / 2)


x = 0
y = 0
zoom = 1

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Teste")
clock = pygame.time.Clock()

while game_running:
  screen.fill((0,0,0))

  walls = []
  for level in LEVELS:
      for i in range(len(level)):
        for j in range(len(level[i])):
          if level[i][j] == "P":
            wall = pygame.draw.rect(screen, (232,123,123), (x + 40*j,y + 40*i,TILES_SIZE,TILES_SIZE))
            0,
            walls.append(wall)

  x_antigo = x
  y_antigo = y
  for event in pygame.event.get():
    if event.type == QUIT:  
      pygame.quit()
      exit()

  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_w] or keys[pygame.K_s]:
    if keys[pygame.K_w]:
      y += 5
    if keys[pygame.K_s]:
      y -= 5
  
  if keys[pygame.K_a] or keys[pygame.K_d]:
    if keys[pygame.K_a]:
     x += 5
    if keys[pygame.K_d]:
     x -= 5

  player = pygame.draw.rect(screen, (232,123,123), (screen_center[0] - 20, screen_center[1] - 20,20*zoom,20*zoom))  
  
  for wall in walls:
    if player.colliderect(wall):
      print(x)
      print(x_antigo)
      print("_---------------------------")
      if x < 0: x+= 5
      else: x-=5

      # x = wall[0] + x_antigo
      # y = wall[1] + y_antigo

  clock.tick(60)
  pygame.display.update()