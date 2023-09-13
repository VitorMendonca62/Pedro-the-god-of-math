import pygame
import random

pygame.init()

# Definindo as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Configurações da tela
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Coletor de Itens")

class Jogador:
    def __init__(self,cor):
        self.rect = pygame.Rect(50, 50, 50, 50)
        self.cor = cor

    def mover(self, dx, dy):
        self.rect.move_ip(dx, dy)


class Coletavel:
    def __init__(self, cor):
        self.rect = pygame.Rect(random.choice([50, 200]), random.randint(50, ALTURA-50), 30, 30)
        self.cor = cor

def desenhar_texto(texto, tamanho, cor, x, y):
    fonte = pygame.font.Font(None, tamanho)
    texto = fonte.render(texto, True, cor)
    TELA.blit(texto, (x, y))


jogador = Jogador((20,87,120))
coletaveis = [Coletavel(VERMELHO), Coletavel(VERDE), Coletavel(AZUL)]

# Loop principal do jogo
rodando = True
relogio = pygame.time.Clock()
pontuacoes = {VERMELHO: 0, VERDE: 0, AZUL: 0}

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador.mover(-5, 0)
    if teclas[pygame.K_RIGHT]:
        jogador.mover(5, 0)
    if teclas[pygame.K_UP]:
        jogador.mover(0, -5)
    if teclas[pygame.K_DOWN]:
        jogador.mover(0, 5)

    # Checar colisões com os coletáveis
    for coletavel in coletaveis:
        if jogador.rect.colliderect(coletavel.rect):
            pontuacoes[coletavel.cor] += 1
            coletaveis.remove(coletavel)
            coletaveis.append(Coletavel(coletavel.cor))

    # Atualizar a tela
    TELA.fill(BRANCO)
    pygame.draw.rect(TELA, jogador.cor, jogador.rect)

    for coletavel in coletaveis:
        pygame.draw.rect(TELA, coletavel.cor, coletavel.rect)

    desenhar_texto(f'Vermelho: {pontuacoes[VERMELHO]}', 30, VERMELHO, 10, 10)
    desenhar_texto(f'Verde: {pontuacoes[VERDE]}', 30, VERDE, 10, 50)
    desenhar_texto(f'Azul: {pontuacoes[AZUL]}', 30, AZUL, 10, 90)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
