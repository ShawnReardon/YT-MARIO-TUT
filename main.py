import pygame, sys
from settings import *
from pygame import *
from tiles import Tile
from level import Level

pygame.init()



SCREEN = display.set_mode((screen_width, screen_height))
CLOCK = time.Clock()
level = Level(level_map, SCREEN)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  SCREEN.fill((255,0,255))
  level.run()
  

  display.update()
  CLOCK.tick(60)