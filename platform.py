from pygame.sprite import Sprite
from pygame.image import load
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

    def move(self):
        mouse_posX = pygame.mouse.get_pos()[0]
        self.rect.x = mouse_posX - self.width / 2


    def get_bonus(self):
        pass

    def update(self):
        self.move()