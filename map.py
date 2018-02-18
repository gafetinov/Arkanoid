from platform import Platform
from ball import Ball
from bricks import Brick
from pygame.sprite import Group
from pygame.image import load


green_brick = load('images/bricks/green_brick.png')
MAP_SIZE = (800, 600)
PLATFORM = Platform(0, 450)
BALL = Ball(PLATFORM.rect.x + PLATFORM.width / 2 + 123, 433)
brick_size = (80, 20)
BRICKS = Group()
level1 = ['          '
          '          '
          '          '
          '          '
          '----------'
          '----------'
          '----------'
          '----------'
          '----------']
x = 0
y = 0
for row in level1:
    for cell in row:
        if cell == '-':
            BRICKS.add(Brick(green_brick, x, y))
        x += brick_size[0]
    y += brick_size[1]
