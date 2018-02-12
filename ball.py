from pygame.sprite import Sprite, collide_mask
from pygame.image import load
import math
import map

IMAGE = load('images/balls/ball.png')
BALL_DIAMETR = 17


class Ball(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = map.PLATFORM.rect.y - BALL_DIAMETR
        self.dx = 0
        self.dy = -10
        self.isGlued = True
        self.speed = 10

    def update(self):
        if self.isGlued:
            self.rect.x = map.PLATFORM.rect.x+map.PLATFORM.width/2-BALL_DIAMETR/2
        else:
            self.edge_collide()
            self.platform_collide()
            self.move()

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def edge_collide(self):
        if self.rect.x+BALL_DIAMETR >= map.MAP_SIZE[0] or self.rect.x <= 0:
            self.dx *= -1
        if self.rect.y+BALL_DIAMETR >= map.MAP_SIZE[1] or self.rect.y <= 0:
            self.dy *= -1

    def platform_collide(self):
        if collide_mask(map.PLATFORM, self):
            reflection_angle = map.PLATFORM.get_reflection_angle(self.rect.x)
            self.dx = self.speed*math.cos(reflection_angle)
            self.dy = -self.speed*math.sin(math.fabs(reflection_angle))