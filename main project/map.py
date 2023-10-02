import pygame
from level import Level
from pygame.locals import *
from collectibles import *
from colors import *
from player import Player

pygame.init()
COLLECT_SOUND = pygame.mixer.Sound('./assets/sounds/collect_sound.mp3') # Efeito sonoro de click

class Map():
  def __init__(self,screen):
    self.all_collectibles_rects = list() # todos os coletaveis
    self.collectibles = list() # todos os coletaveis
    self.colle_adresses = list()
    self.walls_rects = list() # Vai estar armazenado todos os retangulos das paredes 
    self.screen = screen
    self.horizontal_walls = pygame.image.load('sprites/horizontal_woods.png')
    self.vertical_walls = pygame.image.load('sprites/vertical_woods.png')
    self.background = pygame.image.load('sprites/background1.png')

    # É no eixo das abscissas e ordenadas onde o mapa está localizado
    self.x = 0
    self.y = 0 
    # Ultimo valor de x e y  que foi atribuiddo
    self.last_x = 0 
    self.last_y = 0
    self.size_map = 15 # tamanho do mapa

    # Esse dicionário que vai mostrar quanto foi coletado de cada um:
    self.collected = {
      "N": 0,
      "Z": 0,
      "Q": 0,
      "R": 0
    }

    level = Level()
    self.matriz_game = level.do_matriz_map() # Vai pegar a matriz do mapa
    self.draw_map(self.screen, self.x, self.y, True) # Vai desenhar o mapa

    for symbol in symbols_collectibles.keys():
      for _ in range(symbols_collectibles[symbol]): # quantos desse tipo eu quero
        collectible = Collectible(symbol)
      
        while collectible.adress in self.colle_adresses:
          collectible = Collectible(symbol)

        self.colle_adresses.append(collectible.adress)
        self.collectibles.append(collectible)
        self.matriz_game[collectible.row][collectible.column] += symbol

  def draw_map(self, screen, x, y, born): 
    square_size = 60 # Tamanho do quadrado
    height_square_size = 10 # Tamanho do quadrado
    
    screen.blit(self.background, (self.x - 450, self.y - 300))

    self.horizontal_walls = pygame.transform.scale(self.horizontal_walls, (height_square_size, square_size))
    self.vertical_walls = pygame.transform.scale(self.vertical_walls, (square_size, height_square_size))

    for row in range(self.size_map):
      for column in range(self.size_map):
        items = list(self.matriz_game[row][column]) # vai ser os simbolos de um elemento da matriz, por exemplo <^Sy

        for item in items:
          # indicar em qual coordenada o item vai ficar, é a partir do tamanho do quadrado e onde o item ta localizado na matriz e um valor dinamico x ou y, isso faz com que o mapa movimente a partir das teclas pressioandas
          item_x = square_size * column + x
          item_y = square_size * row + y

          # desenhando as paredes
          if item in ("<","^", ">", "v"):
            if item == ">":
              item_x += 60
            elif item == "v":
              item_y += 60

            if item == "<" or item == ">":
              screen.blit(self.horizontal_walls, (item_x, item_y))  
              rect = pygame.Rect(item_x, item_y, height_square_size, square_size)
            elif item == "^" or item == "v":
              rect = pygame.Rect(item_x, item_y, square_size, height_square_size)
              screen.blit(self.vertical_walls, (item_x, item_y))
            self.walls_rects.append(rect)

          if item == "S" and born:
            self.x = - 15
            self.y = - square_size * (row - 4) + 21

          if item in symbols_collectibles.keys():
            item_x += 22
            item_y += 22
            size = 20

            for collectible in self.collectibles:
              if collectible.row == row and collectible.column == column:
                collectible.rect = pygame.Rect(item_x, item_y, size, size)               
                screen.blit(collectible.sets, (item_x, item_y))
            
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
        self.y += self.pace
      if keys[K_s]:
        self.y -= self.pace
      
    if keys[K_a] or keys[K_d]:
      if keys[K_a]:
        self.x += self.pace
      if keys[K_d]:  
        self.x -= self.pace
  
  
  def analyze_collision(self,player):
    for wall in self.walls_rects:
      if player.rect.colliderect(wall):
        self.x = self.last_x
        self.y = self.last_y
        self.pace = 0
        self.walls_rects = list()

    for collectible in self.collectibles:
      if collectible.rect.colliderect(player) and not collectible.collected:
        self.collectibles.remove(collectible)
        self.matriz_game[collectible.row][collectible.column] = self.matriz_game[collectible.row][collectible.column][:-1]
        self.collected[collectible.item] += 1
        collectible.collected = True
        pygame.mixer.Sound.play(COLLECT_SOUND)
        condition_victory = analyze_victory(self.collected)
        if condition_victory:
          print("Terminastes")
  
  def update(self,player):
    self.analyze_collision(player)
    self.move_map()
    self.draw_map(self.screen, self.x, self.y, False)


