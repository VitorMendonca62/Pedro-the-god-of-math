import pygame
from pygame.locals import *
from sys import exit
from level import *

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

# print(levels)

while game_running:
  screen.fill((0,0,0))      

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

  clock.tick(60)
  pygame.display.update()