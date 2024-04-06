import pygame

def take_sprites_player():
  names_sprites = [
    'src/assets/sprites/player_stopped.png',
    'src/assets/sprites/player_stopped_up.png',
    'src/assets/sprites/player_walking_up1.png',
    'src/assets/sprites/player_walking_up2.png',
    'src/assets/sprites/player_stopped_right.png',
    'src/assets/sprites/player_walking_right1.png',
    'src/assets/sprites/player_walking_right2.png',
    'src/assets/sprites/player_stopped_left.png',
    'src/assets/sprites/player_walking_left1.png',
    'src/assets/sprites/player_walking_left2.png',
    'src/assets/sprites/player_stopped.png',
    'src/assets/sprites/player_walking_down1.png',
    'src/assets/sprites/player_walking_down2.png']

  sprites = []

  for name in names_sprites:
    sprites.append(pygame.image.load(name))
    
  return sprites

def place_sprites_collectibles(size):
  names_sprites = [
    'src/assets/sprites/naturals.png',
    'src/assets/sprites/integer.png',
    'src/assets/sprites/racionals.png',
    'src/assets/sprites/reals.png']
  
  sprites = []

  for name in names_sprites:
    sprite = pygame.image.load(name)
    sprites.append(pygame.transform.scale(sprite, (size, size)))
    
  return sprites