import pygame

def write_text(text_content, font_path, color, pos_x, pos_y, font_size, screen): # Função para escrever texto na tela 
  font = pygame.font.Font(font_path, font_size)
  text = font.render(text_content, True, color)
  screen.blit(text, (pos_x, pos_y))