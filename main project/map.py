import pygame
from level import Level
from pygame.locals import *

pygame.init()

vertical_wall = pygame.image.load("assets/vertical-wall.png")
horizontal_wall = pygame.image.load("assets/horizontal-wall.png")

class Map():
  def __init__(self,screen):
    self.screen = screen
    self.walls_rects = list() # Vai estar armazenado todos os retangulos das paredes 
    # É no eixo das abscissas e ordenadas onde o mapa está localizado
    self.x = 0 
    self.y = 0 
    # Ultimo valor de x e y  que foi atribuiddo
    self.last_x = 0 
    self.last_y = 0
    self.size_map = 15 # tamanho do mapa

    level = Level()
    self.matriz_game = level.do_matriz_map() # Vai pegar a matriz do mapa
    self.draw_map(self.screen, self.x, self.y, True) # Vai desenhar o mapa
    
    self.matriz_game[0][0] += "r"
    self.matriz_game[0][14] += "g"
    self.matriz_game[14][0] += "b"
    self.matriz_game[14][14] += "y"

  def draw_map(self,screen,x,y,born): 
    square_size = 60 # Tamanho do quadrado
    height_square_size = 4 # Tamanho do quadrado

    for line in range(self.size_map):
      for column in range(self.size_map):
        items = list(self.matriz_game[line][column]) # vai ser os simbolos de um elemento da matriz, por exemplo <^Sy

        for item in items:
          # indicar em qual coordenada o item vai ficar, é a partir do tamanho do quadrado e onde o item ta localizado na matriz e um valor dinamico x ou y, isso faz com que o mapa movimente a partir das teclas pressioandas
          item_x = square_size * column + x
          item_y = square_size * line + y

          # desenhando as paredes
          if item == ">":
            item_x += 60
          elif item == "v":
            item_y += 60

          if item in ("<","^", ">", "v"):
            if item == "<" or item == ">":
              rect = pygame.Rect(item_x, item_y, height_square_size, square_size)
            elif item == "^" or item == "v":
              rect = pygame.Rect(item_x, item_y, square_size, height_square_size)
            
            self.walls_rects.append(rect)
            pygame.draw.rect(screen, (255,255,255), rect)

          
          # Desenhar os coletaveis
          if item == "r":
            pygame.draw.rect(screen, (255,0,0), (item_x+22, item_y+22,20,20))
          if item == "g":
            pygame.draw.rect(screen, (0, 255, 0), (item_x+22, item_y+22,20,20))
          if item == "b":
            pygame.draw.rect(screen, (0, 0, 255), (item_x+22, item_y+22,20,20))
          if item == "y":
            pygame.draw.rect(screen, (255,255,0), (item_x+22, item_y+22,20,20))


          if item == "S" and born:
            self.x = - square_size * (column) + square_size * 4 
            self.y = - square_size * (line / 2 + 2) - square_size / 2 
            
  def move_map(self):
    self.last_x = self.x
    self.last_y = self.y 

    self.pace = 4
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        exit()

    keys = pygame.key.get_pressed()
    if keys[K_w] or keys[K_s]:
      if keys[K_w]:
        self.y = self.y + self.pace
      if keys[K_s]:
        self.y = self.y - self.pace
    if keys[K_a] or keys[K_d]:
      if keys[K_a]:
        self.x = self.x + self.pace
      if keys[K_d]:  
        self.x = self.x - self.pace

  def analyze_collision(self,player):
    for wall in self.walls_rects:
      if player.colliderect(wall):
        self.x = self.last_x
        self.y = self.last_y
        self.pace = 0
        self.walls_rects = list()

  def update(self,player):
    self.analyze_collision(player)
    self.move_map()
    self.draw_map(self.screen, self.x, self.y, False)

# TO-do:
# Fazer uma missao para passar de level

