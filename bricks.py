from pygame.sprite import Sprite


class Brick(Sprite):
    def __init__(self, image, x, y, special_effect=None):
        Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.special_effect = special_effect
