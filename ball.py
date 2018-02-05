from pygame.sprite import Sprite
from pygame.image import load

IMAGE = load('images/food.png')

class Ball(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.rect = self.IMAGE.get_rect()
        self.rect.x = x
        self.rect.y = y