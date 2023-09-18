import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura, altura = 640, 480

tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption("Jogo teste aprendizado")

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()
    
    """
    desenhar retangulos:
    pygame.draw.rect(tela,(R,G,B),(x,y,width,height))

    desenhar círculos:
    pygame.draw.rect(tela,(R,G,B),(x,y),raio)

    """

    pygame.draw.rect(tela,(255,0,0), (200,300,40,50))

    

    pygame.display.update()