from pygame.sprite import Sprite

NORMAL = None

class Platform(Sprite):
    def __init__(self, x, y):
        self.rect = NORMAL.get_rect()
        self.rect.x = x
        self.rect.y = y