from pygame import sprite, Surface, rect

class Tile(sprite.Sprite):
  def __init__(self, pos, size):
    super().__init__()
    self.image = Surface((size, size))
    self.image.fill('grey')
    self.rect = self.image.get_rect(topleft = pos)

  def update(self, x_shift):
    self.rect.x += x_shift