import pygame

pygame.init()

white = (255,255,255)

class Map:
  def __init__(self):
    self.walls_rects = pygame.sprite.Group()
    self.level = 0
    self.draw_map(self.level)

  def draw_map(self,level,screen,x,y): 
    bigger_wall_size = 60
    smalller_wall_size = 5
    
    for line in range(len(level)):
      for column in range(len(level)):

        direction_walls = list(level[line][column])

        for direction in direction_walls:
          wall_x = bigger_wall_size * column + x
          wall_y = bigger_wall_size * line + y

          if direction == "<":
            pygame.draw.rect(screen, white, (wall_x, wall_y, smalller_wall_size, bigger_wall_size))  
          if direction == ">":
            pygame.draw.rect(screen, white, (wall_x + 60, wall_y, smalller_wall_size, bigger_wall_size))  
          if direction == "v":
            pygame.draw.rect(screen, white, (wall_x, wall_y + 60 ,bigger_wall_size + 5,smalller_wall_size))  
          if direction == "^":
            pygame.draw.rect(screen, white, (wall_x, wall_y, bigger_wall_size,smalller_wall_size)) 


# TO-do:
# Fazer uma missao para passar de level
# Fazer a colisao do personagem