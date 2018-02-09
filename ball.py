from pygame.sprite import Sprite
from pygame.image import load
import map

IMAGE = load('images/balls/ball.png')
BALL_DIAMETR = 17


class Ball(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = 0
        self.dy = 0
        self.isGlued = True

    def update(self):
        if self.isGlued:
            self.rect.x = map.PLATFORM.rect.x + map.PLATFORM.width / 2
        else:
            self.move()

    def move(self):
        self.dy = -1
        self.rect.y += self.dy
