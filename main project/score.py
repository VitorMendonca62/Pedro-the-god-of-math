from collectibles import *
from colors import *

width = 900
height = 600
screen = pygame.display.set_mode((width,height))

dif = 130
ini_symbol = 470-(dif*2)
ini_text = ini_symbol + 25
score_bar = pygame.image.load('assets/images/start_button.png')
score_bar = pygame.transform.scale(score_bar, (width,65))


def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def colle_sub(map,symbol,index,name):
    screen.blit(name,(ini_symbol + dif*index, height-50,20,20))
    draw_text(f"({map.collected[symbol]}/{map.symbols_collectibles[symbol]})",30,white,ini_text+dif*index,height-50)

def show_score(map):
    #pygame.draw.rect(screen,(120,120,120),(0,height-40,width,40))
    screen.blit(score_bar, (0,height-70))
    colle_sub(map,'N',0,Collectible.naturals)
    colle_sub(map,'Z',1,Collectible.integers)
    colle_sub(map,'Q',2,Collectible.racionals)
    colle_sub(map,'R',3,Collectible.reals)