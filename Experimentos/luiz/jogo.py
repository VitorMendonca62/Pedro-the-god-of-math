import pygame
import random

pygame.init()

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
cinza = (100,100,100)

# Configurações da tela
largura, altura = 640, 480

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Coletor de Itens")

class Jogador:
    def __init__(self):
        self.rect = pygame.draw.rect(tela,preto,(largura/2,altura/2,50,50))
        self.cor = preto

    """
    def mover(self, dx, dy):
        self.rect.move_ip(dx, dy)
    """

class Coletavel:
    def __init__(self, cor):
        self.rect = pygame.Rect(random.choice([50, 200]), random.randint(50, altura-50), 30, 30)
        self.cor = cor

    def mover(self, dx, dy):
        self.rect.move_ip(dx, dy)

def desenhar_texto(texto, tamanho, cor, x, y):
    fonte = pygame.font.Font(None, tamanho)
    texto = fonte.render(texto, True, cor)
    tela.blit(texto, (x, y))

jogador = Jogador()
coletaveis = [Coletavel(vermelho), Coletavel(verde), Coletavel(azul), Coletavel(cinza)]

# Loop principal do jogo
rodando = True
relogio = pygame.time.Clock()
pontuacoes = {vermelho: 0, verde: 0, azul: 0, cinza: 0}

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    for coletavel in coletaveis:

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            #jogador.mover(-5, 0)
            coletavel.mover(5,0)

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            #jogador.mover(5, 0)
            coletavel.mover(-5,0)

        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            #jogador.mover(0, -5)
            coletavel.mover(0,5)

        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            #jogador.mover(0, 5)
            coletavel.mover(0,-5)

    # Checar colisões com os coletáveis
    for coletavel in coletaveis:
        if jogador.rect.colliderect(coletavel.rect):
            pontuacoes[coletavel.cor] += 1
            coletaveis.remove(coletavel)
            coletaveis.append(Coletavel(coletavel.cor))

    # Atualizar a tela
    tela.fill(branco)
    pygame.draw.rect(tela, jogador.cor, jogador.rect)

    for coletavel in coletaveis:
        pygame.draw.rect(tela, coletavel.cor, coletavel.rect)

    desenhar_texto(f'Vermelho: {pontuacoes[vermelho]}', 30, vermelho, 10, 10)
    desenhar_texto(f'Verde: {pontuacoes[verde]}', 30, verde, 10, 50)
    desenhar_texto(f'Azul: {pontuacoes[azul]}', 30, azul, 10, 90)
    desenhar_texto(f'Cinza: {pontuacoes[cinza]}', 30, cinza, 10, 130)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
