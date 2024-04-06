import pygame
from classes.Collectible import symbols_collectibles, Collectible
from utils.collectibles import analyze_victory

pygame.init()
COLLECT_SOUND = pygame.mixer.Sound('src/assets/sounds/collect_sound.mp3') # Efeito sonoro de click

class Collectibles:
  def __init__(self):
    self.collectibles = list() # todos os coletaveis
    self.colle_adresses = list() # todos os endereços dos coletaveis
    self.collected = {
      "N": 0,
      "Z": 0,
      "Q": 0,
      "R": 0
    }
    
  def create(self, matriz_game, level):
    for symbol in symbols_collectibles[level].keys():
      for _ in range(symbols_collectibles[level][symbol]): # quantos desse tipo eu quero
        collectible = Collectible(symbol)
      
        while collectible.adress in self.colle_adresses:
          collectible = Collectible(symbol)

        self.colle_adresses.append(collectible.adress)
        self.collectibles.append(collectible)
        matriz_game[collectible.row][collectible.column] += symbol
    
    return matriz_game
  
  def analyze_collision(self, player, matriz_game, level):
    collectibles = self.collectibles
    condition_victory = False
    for collectible in collectibles:
      if collectible.rect.colliderect(player) and not collectible.collected:
        collectibles.remove(collectible)
        matriz_game[collectible.row][collectible.column].replace(collectible.item, "")
        self.collected[collectible.item] += 1
        collectible.collected = True
        pygame.mixer.Sound.play(COLLECT_SOUND)
        condition_victory = analyze_victory(self.collected, level)
        
        if condition_victory:
          pygame.mixer.music.pause()
          pygame.mixer.Sound.play(pygame.mixer.Sound('src/assets/sounds/victory_sound.mp3'))
          return [matriz_game, condition_victory]
        
    return [matriz_game, condition_victory]
          