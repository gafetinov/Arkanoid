from pygame.sprite import Sprite
from pygame.image import load
import map
import math
import pygame.mouse

NORMAL_PLATFORM = load('images/platforms/normal_platform.png')


class Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = NORMAL_PLATFORM
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = 190
        self.height = 45
        self.dx = 0
        self.right = False
        self.left = False
        self.max_reflection_angle = 5*math.pi/6

    def move(self):
        mouse_posX = pygame.mouse.get_pos()[0]
        self.rect.x = mouse_posX - self.width / 2

    def edge_collide(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x+self.width >= map.MAP_SIZE[0]:
            self.rect.x = map.MAP_SIZE[0]-self.width

    def get_bonus(self):
        pass

    def get_reflection_angle(self, impact_point):
        return 5*math.pi/6-2*math.pi/3/190*(impact_point -self.rect.x)

    def update(self):
        self.move()
        self.edge_collide()

