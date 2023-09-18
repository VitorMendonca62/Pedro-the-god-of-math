from random import randint
from level import levels_size

levels_amount_collectibles = [(6,8),(10,12),(11,13)]

class Collectibles:
    def __init__(self, level,type):
        level = 0
        type = "normal"
        self.level = level
        min = levels_amount_collectibles[level][0]
        max = levels_amount_collectibles[level][1]
        self.amount = randint(min,max)
        self.type = type
        self.list = list()

    def insert_matriz(self):
        x = randint(levels_size[self.level])
        y = randint(levels_size[self.level])
        coords = (x,y)
        for item in self.list:
            item_x = item[0]
            item_y = item[1]
            distance = ((x - item_x)^2 + (y - item_y)^2) / (1/2)
            if distance < 5:
                coords = self.insert_matriz()
        
        matriz = map.take_matriz(self.level)
        matriz[x,y] += "C"
        print(matriz)
        return coords