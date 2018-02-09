from platform import Platform
from ball import Ball

MAP_SIZE = (800, 600)
PLATFORM = Platform(0, 450)
BALL = Ball(PLATFORM.rect.x + PLATFORM.width / 2, 433)