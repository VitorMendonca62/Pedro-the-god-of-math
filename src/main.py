import pygame
from sys import exit 
from classes.Button import Button
from game import game
from utils.score import write_text

pygame.init()

muted = False # Variável para detectar se a música encontra-se mutada

# Tamanho da tela 
WIDTH = 900 
HEIGHT = 600 

# Música e efeitos sonoros 
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load('src/assets/sounds/Soundtrack_menu.mp3') # Música de Background 
pygame.mixer.music.play(-1) # O -1 foi colcoado para estar em loop 

CLICK_SOUND = pygame.mixer.Sound('src/assets/sounds/clicked_sound.mp3') # Efeito sonoro de click

# Definição do tamanho da tela e definição do background
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Cria uma tela e determina o seu tamanho

# Relógio do fps
clock = pygame.time.Clock()

# Fonte 
font_path = 'src/assets/font/Pixeled.otf'
font = pygame.font.Font(font_path, 30)

def instructions_screen(): # A tela de instruções
    # Imagem de Background
    instructions_screen_bg = pygame.image.load('src/assets/images/help_screen.png')
    instructions_screen_bg = pygame.transform.scale(instructions_screen_bg,(WIDTH,HEIGHT))
    
    pygame.display.set_caption("Pedro: The God of Math") # Coloca o nome do jogo
    # Título e Ícone
    icon = pygame.image.load('src/assets/images/icon.png')
    pygame.display.set_icon(icon)

    while True:
        screen.blit(instructions_screen_bg, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        # Imagem do botão (e a sua conversão para o tamanho ideal)
        BUTTON_IMAGE = pygame.image.load("src/assets/images/exit_icon.png")
        BUTTON_IMAGE = pygame.transform.scale(BUTTON_IMAGE, (30, 30))

        QUIT_BUTTON = Button(BUTTON_IMAGE, 690, 127, font, "")
        QUIT_BUTTON.interaction_text(mouse_pos)
        QUIT_BUTTON.update(screen)

        # Conteúdo escrito da parte de instruções       
        STRING_LIST = [" O jogo tem como objetivo passar pelo", " labirinto coletando todos os conjuntos", " numericos no mapa. Utilize as teclas", " W A S D para mover o personagem.", "A quantidade coletada sera mostrada", "  na tela. Divirta-se e seja preciso! :)"] 
        
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
                    main_menu()
        clock.tick(60)
        pygame.display.update()

def main_menu():
    global muted
    
    # Declarando a imagem de background do main_menu
    bg_img = pygame.image.load('src/assets/images/main_background.png')
    bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))
    
    # Título e Ícone
    pygame.display.set_caption("Pedro: The God of Math") # Coloca o nome do jogo
    icon = pygame.image.load('src/assets/images/icon.png')
    pygame.display.set_icon(icon)
    
    # Imagem do botão 
    button_image_path = "src/assets/images/start_button.png"
    
    # Modificar o ícone se a música encontra-se mutada ou desmutada. 
    if muted: 
        button_image_music_path = "src/assets/images/muted_music_icon.png"
    else:
        button_image_music_path = "src/assets/images/music_icon.png"
    
    while True:
        screen.blit(bg_img, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        
        buttons_list = []

        # Imagem do botão (e a sua conversão para o tamanho ideal)
        BUTTON_IMAGE = pygame.image.load(button_image_path)
        BUTTON_IMAGE = pygame.transform.scale(BUTTON_IMAGE, (251, 81))

        # Imagem do ícone do botão da Música
        BUTTON_IMAGE_MUSIC = pygame.image.load(button_image_music_path)
        BUTTON_IMAGE_MUSIC = pygame.transform.scale(BUTTON_IMAGE_MUSIC, (41, 41))

        # Botão de iniciar o jogo
        START_BUTTON = Button(BUTTON_IMAGE, 250, 500, font, "Iniciar")
        buttons_list.append(START_BUTTON)
        
        # Botão de fechar o jogo
        INSTRUCTIONS_BUTTON = Button(BUTTON_IMAGE, 650, 500, font, "Instrucoes")
        buttons_list.append(INSTRUCTIONS_BUTTON)

        # Botão de mutar a música
        MUSIC_BUTTON = Button(BUTTON_IMAGE_MUSIC, 30, 30, font, "")
        buttons_list.append(MUSIC_BUTTON)
        
        for i in buttons_list:
            i.interaction_text(mouse_pos)
            i.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.clicked(mouse_pos):
                    pygame.mixer.Sound.play(CLICK_SOUND)
                    if not muted:
                        pygame.mixer.music.load('src/assets/sounds/game_soundtrack.mp3') # Música de Background 
                        pygame.mixer.music.play(-1) # O -1 foi colcoado para estar em loop 
                    game(main_menu)
                if INSTRUCTIONS_BUTTON.clicked(mouse_pos):
                    pygame.mixer.Sound.play(CLICK_SOUND)
                    instructions_screen()
                if MUSIC_BUTTON.clicked(mouse_pos):
                    pygame.mixer.Sound.play(CLICK_SOUND)
                    
                    if muted == False:  
                        muted = True
                        button_image_music_path = "src/assets/images/muted_music_icon.png"
                        pygame.mixer.music.pause()
                    else: # muted == True
                        muted = False
                        button_image_music_path = "src/assets/images/music_icon.png"
                        pygame.mixer.music.unpause()
        clock.tick(60)
        pygame.display.update()

main_menu()

