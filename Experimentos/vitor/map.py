import pygame
from level import Level, levels_size

pygame.init()

white = (255,255,255)

class Map:
  def __init__(self,screen):
    self.screen = screen
    self.walls_rects = pygame.sprite.Group()
    self.matriz_game = list()  
    self.number_level = 0
    self.x = 0
    self.y = 0

    level_0 = Level(self.number_level)
    self.matriz_game.append(level_0.take_matriz_map())

    self.draw_map(self.matriz_game, self.number_level, self.screen, self.x, self.y, True)

  def draw_map(self,matriz, level,screen,x,y, born): 
    bigger_wall_size = 60
    smalller_wall_size = 5
    level = 1
    for matriz_level in matriz:
      for line in range(levels_size[level]):
        for column in range(levels_size[level]):

          direction_walls = list(matriz_level[line][column])

          for direction in direction_walls:
            wall_x = bigger_wall_size * column + x
            wall_y = bigger_wall_size * line + y

            if direction == "<":
              pygame.draw.rect(screen, white, (wall_x, wall_y, smalller_wall_size, bigger_wall_size))  
            if direction == ">":
              pygame.draw.rect(screen, white, (wall_x + 60, wall_y, smalller_wall_size, bigger_wall_size))  
            if direction == "v":
              pygame.draw.rect(screen, white, (wall_x, wall_y + 60 , bigger_wall_size + 5, smalller_wall_size))  
            if direction == "^":
              pygame.draw.rect(screen, white, (wall_x, wall_y, bigger_wall_size,smalller_wall_size)) 
            if direction == "S" and born:
              self.x = - bigger_wall_size * (column) + bigger_wall_size * smalller_wall_size
              self.y = - bigger_wall_size * (line / 2 + 2) - bigger_wall_size / 2 + smalller_wall_size

  def move_map(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        pygame.quit()
        exit()

      keys = pygame.key.get_pressed()
      
      if keys[pygame.K_w] or keys[pygame.K_s]:
        if keys[pygame.K_w]:
          self.y += 5
        if keys[pygame.K_s]:
          self.y -= 5
      
      if keys[pygame.K_a] or keys[pygame.K_d]:
        if keys[pygame.K_a]:
         self.x += 5
        if keys[pygame.K_d]:
         self.x -= 5

  def update(self):
    self.draw_map(self.matriz_game, self.number_level, self.screen, self.x, self.y, False)
    self.move_map()

# TO-do:
# Fazer uma missao para passar de level
# Fazer a colisao do personagem
# Movimentação do mapa