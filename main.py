import pygame
from ball import Ball

pygame.init()
window = pygame.display.set_mode((800, 600))
screen = pygame.Surface((800, 600))

sprites = pygame.sprite.Group()
ball = Ball(244, 220)
sprites.add(ball)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0, 100, 200))
    sprites.draw(screen)
    window.blit(screen, (0, 0))
    pygame.display.flip()

