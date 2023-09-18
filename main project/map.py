import pygame
import pygame.locals
from level import Level, levels_size

pygame.init()

white = (255,255,255)
vertical_wall = pygame.image.load("assets/vertical-wall.png")
horizontal_wall = pygame.image.load("assets/horizontal-wall.png")

class Map():
  def __init__(self,screen):
    self.screen = screen
    self.walls_rects = list()
    self.matriz_game = list()  
    self.number_level = 0
    self.x = 0
    self.y = 0

    self.last_x = 0
    self.last_y = 0

    level_0 = Level(self.number_level)
    self.matriz_game.append(level_0.do_matriz_map())

    self.draw_map(self.matriz_game, self.number_level, self.screen, self.x, self.y, True)

  def draw_map(self,matriz,level,screen,x,y, born): 
    bigger_wall_size = 60
    smalller_wall_size = 4
    level = 1
    for matriz_level in matriz:
      for line in range(levels_size[level]):
        for column in range(levels_size[level]):

          direction_walls = list(matriz_level[line][column])

          for direction in direction_walls:
            wall_x = bigger_wall_size * column + x
            wall_y = bigger_wall_size * line + y

            if direction == "<":
              pass
            if direction == ">":
              wall_x += 60
            if direction == "v":
              wall_y += 60
              wall_x += 4
            if direction == "^":
              pass

            if direction == "<" or direction == ">":
              image = vertical_wall
            elif direction == "^" or direction == "v":
              image = horizontal_wall

            rect = screen.blit(image,(wall_x,wall_y))
            self.walls_rects.append(rect)

            if direction == "S" and born:
              self.x = - bigger_wall_size * (column) + bigger_wall_size * smalller_wall_size
              self.y = - bigger_wall_size * (line / 2 + 2) - bigger_wall_size / 2 + smalller_wall_size
            

  def move_map(self,player):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        exit()

      keys = pygame.key.get_pressed()

      if self.last_x != self.x: self.last_x = self.x
      if self.last_y != self.y: self.last_y = self.y 

      if keys[pygame.K_w] or keys[pygame.K_s]:
        if keys[pygame.K_w]:
          self.y += 2
        if keys[pygame.K_s]:
          self.y -= 2
      
      if keys[pygame.K_a] or keys[pygame.K_d]:
        if keys[pygame.K_a]:
          self.x += 2
        if keys[pygame.K_d]:
          self.x -= 2

  def analyze_collision(self,player):
    for wall in self.walls_rects:
      if player.colliderect(wall):
        self.x = self.last_x
        self.y = self.last_y

        self.walls_rects = list()
  
  def update(self,player):
    self.analyze_collision(player)
    self.move_map(player)
    self.draw_map(self.matriz_game, self.number_level, self.screen, self.x, self.y, False)

# TO-do:
# Fazer uma missao para passar de level
# Fazer a colisao do personagem
# Movimentação do mapa