from pygame.sprite import Sprite
from pygame.image import load

image = load('images/food.png')

class Ball(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y