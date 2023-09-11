from random import randint
import cv2

levels_size = [12,15,17] # A cada fase que passar o mapa vai ficar maior

class Level:
  def __init__(self,level):
    self.level = level
    # self.size = levels_size[self.level]  
    self.size = levels_size[1]  
    # random_number = randint(0,10) # Como está muito fácil criar diversos mapas, podemos fazer com que a cada vez que jogar ser um mapa diferente
    random_number = 1 # Como está muito fácil criar diversos mapas, podemos fazer com que a cada vez que jogar ser um mapa diferente
    self.level_photo = cv2.imread(f"./assets/levels/{self.level}/maze{random_number}.png") # Pega uma estrutura de mapa aleatorio a partir do nivel
    self.matriz = list()

  def take_matriz_map(self):
    for column in range(self.size):
      elements_line = list() # Representa uma linha da matriz
      for line in range(self.size):
        # Essa conta faz "sentido", posso explicar depois
        slice_photo = self.level_photo[(column * 16) + 1 : ((column + 1) * 16 + 1), (line * 16) + 1 : ((line + 1) * 16) + 1] # Pega um quadrado do labirindo 16x16
        string = str()

        # Esses simbolos a baixo vai servir para mostrar ao código onde tem parede, ou seja, 
        # < - Parede no lado esquerdo
        # ^ - Parede em cima
        # > - Parede no lado direito
        # v - Parede embaixo

        left_point = tuple(slice_photo[8,0])
        up_point = tuple(slice_photo[0,8])
        right_point = tuple(slice_photo[8,15])
        down_point = tuple(slice_photo[15,8])
        all_points = [left_point, up_point, right_point, down_point] 

        if (0,0,0) == left_point: string += "<"
        if (0,0,0) == up_point: string += "^"
        if (0,0,0) == right_point: string += ">"
        if (0,0,0) == down_point: string += "v"

        # Verifica o começo e o fim do labirinto, se a cor for vermelha, então, ele irá colocar um E na string, caso seja verda, será S
        # Sim, o vermelho ta invertido e eu não sei o porquê
        
        for point in all_points:
          if point == (0,0,255):
            string += "E"
          if point == (0,255,0):
            string += "S"

        elements_line.append(string)
      self.matriz.append(elements_line)

    return self.matriz


# todo

a = [1,2,3]

a[0:1]
print(a)