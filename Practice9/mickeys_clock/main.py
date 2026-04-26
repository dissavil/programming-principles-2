import pygame
from clock import Clock
pygame.init()

screen = pygame.display.set_mode((1536 , 1024))
pygame.display.set_caption("Mickeys Clock")

clock = pygame.time.Clock()
running = True

mickeyclock = Clock(screen)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            

    screen.fill((255, 255, 255))

    mickeyclock.draw()
    mickeyclock.hands()

    pygame.display.flip()

pygame.quit()
