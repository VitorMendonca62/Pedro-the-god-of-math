import pygame
from sys import exit 
from pygame.locals import *

pygame.init() # Inicia o código em pygame

# Tela e background image
screen = pygame.display.set_mode((800,500)) # Cria uma tela e determina o seu tamanho
bg_img = pygame.image.load('images/background.png')
bg_img = pygame.transform.scale(bg_img,(800,500))

# Fonte 
font = pygame.font.SysFont(None, 20) 
TXT_COLOUR = (255, 255, 255)



# Imagens dos botões
BUTTON_SIZE = (100, 100)

start_img = pygame.image.load('images/start_button.png')
#start_img = pygame.transform.scale(start_img, BUTTON_SIZE)

quit_img = pygame.image.load('images/quit_button.png')
#quit_img = pygame.transform.scale(quit_img, BUTTON_SIZE)


# Os botões serão considerados objetos
class Button(): # Criação da classe objeto
    def __init__(self, x, y, image, scale): # Fora criado o scale para definir a escala do tamanho do botão
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self): # Função para desenhar o botão na tela
        action = False
        position = pygame.mouse.get_pos() # Pegar a posição do mouse

        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # O 0 foi utilizado para relacionar com o botão de clique esquerdo
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0: # O 0 foi utilizado para relacionar com o botão de clique esquerdo
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y)) # Essa tupla como segundo elemento vai representar a posição do botão
        
        return action

# Criação das instâncias do Botã
start_button = Button(100,200, start_img, 0.4)
quit_button = Button(450,200, quit_img, 0.4)

# Título e Ícone
pygame.display.set_caption("Pedro: God of the Math") # Coloca o nome do jogo
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
 
while True: # Para apenas não rodar uma vez e fechar a aplicação, é necessário um loop
    screen.blit(bg_img, (0,0))
    draw_text("TESTE", font, TXT_COLOUR, 160, 250)
    if start_button.draw():
        pass
    if quit_button.draw():
        print("teste2")
        
    for event in pygame.event.get(): # Para todo o evento que acontecer, por isso um for tendo element. 
        if event.type == pygame.QUIT: # Se o evento foi clicar no X para fechar
            pygame.quit() # Isso fecha a aplicação, porém se fosse apenas essa parte, daria erro no código ao fechar
            exit() # Evita o erro importando de outra biblioteca chamada sys
    pygame.display.update()
