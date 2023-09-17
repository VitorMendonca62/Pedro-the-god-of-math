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

# parte dos coletáveis

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

class Coletavel:
  def __init__(self, cor):
    self.rect = pygame.Rect(random.choice([50, 200]), random.randint(50, 640-50), 30, 30)
    self.cor = cor
      
pontuacoes = {vermelho: 0, verde: 0, azul: 0}
coletaveis = [Coletavel(vermelho), Coletavel(verde), Coletavel(azul)]

# parte do jogo rodando

while game_running:
  screen.fill((0,0,0))      

  map.update()
  
  player = pygame.draw.rect(screen, (232,123,123), (screen_center[0] - 20, screen_center[1] - 20,20*zoom,20*zoom))  

  clock.tick(60)
  pygame.display.update()

  for coletavel in coletaveis:
    if player.rect.colliderect(coletavel.rect):
  
      pontuacoes[coletavel.cor] += 1
      coletaveis.remove(coletavel)
