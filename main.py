import pygame
import map

pygame.init()
window = pygame.display.set_mode(map.MAP_SIZE)
screen = pygame.Surface(map.MAP_SIZE)
sprites = pygame.sprite.Group()
ball = map.BALL
platform = map.PLATFORM
bricks = map.BRICKS
sprites.add(ball, platform)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                ball.isGlued = False
    platform.update()
    ball.update()
    bricks.update()
    screen.fill((0, 100, 200))
    bricks.draw(screen)
    sprites.draw(screen)
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(10)
