from pygame import *
from tiles import Tile
from settings import tile_size, screen_width
from player import Player

class Level:
  def __init__(self, level_data, surface):
    self.display_surface = surface
    self.setup_level(level_data)
    self.world_shift = 0
    
  def setup_level(self, layout):
    self.tiles = sprite.Group()
    self.player = sprite.GroupSingle()
    for row_index, row in enumerate(layout):
      for col_index, col in enumerate(row):
        if col == 'X':
          
          x = col_index * tile_size
          y = row_index * tile_size
          tile = Tile((x,y), tile_size)
          self.tiles.add(tile)
          
        if col == 'P':
          print('P')
          x = col_index * tile_size
          y = row_index * tile_size
          player_sprite = Player((x,y), tile_size)
          self.player.add(player_sprite)
  def scroll_x(self):
    player = self.player.sprite
    player_x = player.rect.centerx
    direction_x = player.direction.x

    if player_x < screen_width / 4 and direction_x < 0:
      self.world_shift = 8
      player.speed = 0
    elif player_x > screen_width * .75 and direction_x > 0:
      self.world_shift = -8
      player.speed = 0
    else:
      self.world_shift = 0
      player.speed = 8

  def horizontal_movement_collision(self):
    player = self.player.sprite

    player.rect.x += player.direction.x * player.speed

    for sprite in self.tiles.sprites():
      if sprite.rect.colliderect(player.rect):
        if player.direction.x < 0:
          player.rect.left = sprite.rect.right

        elif player.direction.x > 0:
          player.rect.right = sprite.rect.left



  def run(self):
    self.tiles.update(self.world_shift)
    self.player.draw(self.display_surface)
    self.tiles.draw(self.display_surface)
    self.player.update()
    self.scroll_x()
    self.horizontal_movement_collision()
  