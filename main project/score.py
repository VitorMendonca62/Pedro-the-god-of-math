from collectibles import *
from colors import *



def show_score(screen, map):
    height = screen.get_height()
    width = screen.get_width()
    
    score_bar = pygame.image.load('assets/images/start_button.png')
    score_bar = pygame.transform.scale(score_bar, (width,65))

    def draw_text(text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    def draw_collectible(symbol, index, name):
        between_collectibles = 130
        collectible_x_left = (width / 2) - (between_collectibles * 2)
        text_x_left = collectible_x_left + 30
        position = between_collectibles * index

        size = 20
        collectible_x = collectible_x_left + position
        collectible_y = height - 52
        screen.blit(name, (collectible_x, collectible_y, size, size))
        
        total_collectible = symbols_collectibles[symbol]
        collectible_collected = map.collected[symbol] 
        
        string_text = f"({collectible_collected}/{total_collectible})"

        text_x = text_x_left + position
        text_y = height - 50
        draw_text(string_text, 30, black, text_x, text_y)

    position = (height - 40, width)
    screen.blit(score_bar, (0,height-70))

    draw_collectible('N', 0, Collectible.naturals)
    draw_collectible('Z', 1, Collectible.integers)
    draw_collectible('Q', 2, Collectible.racionals)
    draw_collectible('R', 3, Collectible.reals)


