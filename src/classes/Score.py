from classes.Collectible import Collectible, symbols_collectibles
from classes.Button import Button
from utils.colors import *
from utils.score import write_text
import pygame

font_path = 'src/assets/font/Pixeled.otf'
font = pygame.font.Font(font_path, 30)


class Score:
  def show(self, screen, map):
    height = screen.get_height()
    width = screen.get_width()
      
    score_bar = pygame.image.load('src/assets/images/perga.png')
    score_bar = pygame.transform.scale(score_bar, (width, 65))

    def draw_text(text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    def draw_collectible(symbol, index, name):
        between_collectibles = 130
        collectible_x_left = (width / 2) - (between_collectibles * 2)
        text_x_left = collectible_x_left + 40
        position = between_collectibles * index

        size = 20
        collectible_x = collectible_x_left + position
        collectible_y = height - 55.5
        screen.blit(name, (collectible_x, collectible_y, size, size))
        
        total_collectible = symbols_collectibles[map.level][symbol]
        collectible_collected = map.collectibles.collected[symbol] 
        
        string_text = f"({collectible_collected}/{total_collectible})"

        text_x = text_x_left + position
        text_y = height - 50
        draw_text(string_text, 30, black, text_x, text_y)

    screen.blit(score_bar, (0, height-70))

    draw_collectible('N', 0, Collectible.sprites[0])
    draw_collectible('Z', 1, Collectible.sprites[1])
    draw_collectible('Q', 2, Collectible.sprites[2])
    draw_collectible('R', 3, Collectible.sprites[3])

  def victory_screen(self, screen, menu):
    # Imagem de Background
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    
    victory_bg = pygame.image.load('src/assets/images/final_screen.png')
    victory_bg = pygame.transform.scale(victory_bg,(WIDTH,HEIGHT))
    
    pygame.display.set_caption("Pedro: The God of Math") # Coloca o nome do jogo
    # Título e Ícone
    icon = pygame.image.load('src/assets/images/icon.png')
    pygame.display.set_icon(icon)

    font_path = 'src/assets/font/Pixeled.otf'
    
    while True:
      screen.blit(victory_bg, (0,0))
      mouse_pos = pygame.mouse.get_pos()
      
      BUTTON_IMAGE = pygame.image.load("src/assets/images/exit_icon.png")
      BUTTON_IMAGE = pygame.transform.scale(BUTTON_IMAGE, (30, 30))

      QUIT_BUTTON = Button(BUTTON_IMAGE, 690, 127, font, "")
      QUIT_BUTTON.interaction_text(mouse_pos)
      QUIT_BUTTON.update(screen)
      
      # Conteúdo escrito da parte de instruções       
      STRING_LIST = ["Parabens por coletar todos os coletaveis.", "Pedro esta muito orgulhoso que voce conseguiu.", "Para jogar novamente, clique no X"] 
      
      # Posição inicial da escrita (será usada como referência para determinar as próximas linhas)
      initial_x = 200
      initial_y = 215

      
      # Loop criado para printar cada string para simular a quebra de linha
      for line in STRING_LIST:
          write_text(line, font_path, (0,0,0), initial_x, initial_y, 30, screen)
          initial_y += 30
  
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
            if QUIT_BUTTON.clicked(mouse_pos):
                menu()
          
      pygame.display.update()
