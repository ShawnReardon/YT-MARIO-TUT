from pygame import sprite, Surface, rect, key
import pygame

class Player(sprite.Sprite):
  def __init__(self, pos, size):
    super().__init__()
    self.image = Surface((size / 2, size))
    self.image.fill('red')
    self.rect = self.image.get_rect(topleft = pos)
    self.direction = pygame.math.Vector2(0,0)

    # movment
    self.speed = 8
    self.gravity = 0.8
    self.jump_speed = -16

  def get_input(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
      self.direction.x = -1
    elif keys[pygame.K_d]:
      self.direction.x = 1
      print("d")
    else:
      self.direction.x = 0
    if keys[pygame.K_SPACE]:
      self.jump()

  def apply_gravity(self):
    self.direction.y += self.gravity
    self.rect.y += self.direction.y
  
  def jump(self):
    self.direction.y = self.jump_speed
  
  def update(self):
    self.get_input()
    self.apply_gravity()
