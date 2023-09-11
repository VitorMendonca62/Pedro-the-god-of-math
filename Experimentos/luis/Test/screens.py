import pygame
from button import Button

pygame.init()
# Tamanho da tela 
WIDTH = 800
HEIGHT = 600 

# Definição do tamanho da tela e definição do background
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Cria uma tela e determina o seu tamanho
bg_img = pygame.image.load('assets/images/background.png')
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))

# Fonte 
default_font = pygame.font.SysFont('arial', 30)

def write_text(text_content, font, color, pos_x, pos_y):
    text = font.render(text_content, True, color)
    screen.blit(text, (pos_x, pos_y))

def help_screen():
    help_screen_bg = pygame.image.load('assets/images/help_screen.png')
    help_screen_bg = pygame.transform.scale(help_screen_bg,(WIDTH,HEIGHT))
    pygame.display.set_caption("Pedro: God of the Math") # Coloca o nome do jogo
    # Título e Ícone
    icon = pygame.image.load('assets/images/icon.png')
    pygame.display.set_icon(icon)
    
    while True:
        screen.blit(help_screen_bg, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        BUTTONS_LIST = []
        font_text = pygame.font.SysFont('arial', 20)
        EXPLANATION_MESSAGE = """
Jair messias bolsonaro foi o único presidente\n
que ajudou positivamente para a política brasileira\n
ao implementar as suas medidas
"""
        write_text(EXPLANATION_MESSAGE, font_text, (0,0,0), 110, 90)
        # Imagem do botão (e a sua conversão para o tamanho ideal)
        BUTTON_IMAGE = pygame.image.load("assets/images/start_button.png")
        BUTTON_IMAGE = pygame.transform.scale(BUTTON_IMAGE, (251, 81))

        
        for i in BUTTONS_LIST:
            i.interaction_text_color(mouse_pos)
            i.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if START_BUTTON.clicked(mouse_pos):
                   # print("Clicado")
                #if QUIT_BUTTON.clicked(mouse_pos):
                    #print("Clicado a parte de sair")
                    #pygame.quit()
                    #exit()

        pygame.display.update()


def main_menu():
    pygame.display.set_caption("Pedro: God of the Math") # Coloca o nome do jogo
    
    # Título e Ícone
    icon = pygame.image.load('assets/images/icon.png')
    pygame.display.set_icon(icon)
    
    while True:
        screen.blit(bg_img, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        
        BUTTONS_LIST = []

        # Imagem do botão (e a sua conversão para o tamanho ideal)
        BUTTON_IMAGE = pygame.image.load("assets/images/start_button.png")
        BUTTON_IMAGE = pygame.transform.scale(BUTTON_IMAGE, (251, 81))

        # Botão de iniciar o jogo
        START_BUTTON = Button(BUTTON_IMAGE, 400, 250, default_font, "Iniciar")
        BUTTONS_LIST.append(START_BUTTON)
        
        # Botão de fechar o jogo
        QUIT_BUTTON = Button(BUTTON_IMAGE, 400, 350, default_font, "Sair")
        BUTTONS_LIST.append(QUIT_BUTTON)
        
        for i in BUTTONS_LIST:
            i.interaction_text_color(mouse_pos)
            i.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.clicked(mouse_pos):
                    help_screen()
                    print("Clicado")
                if QUIT_BUTTON.clicked(mouse_pos):
                    print("Clicado a parte de sair")
                    pygame.quit()
                    exit()

        pygame.display.update()

