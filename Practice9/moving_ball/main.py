import pygame
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Ball")
x = 400
y = 300
ball = Ball(x, y)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ball.move_up()

    if keys[pygame.K_DOWN]:
        ball.move_down(600)

    if keys[pygame.K_LEFT]:
        ball.move_left()

    if keys[pygame.K_RIGHT]:
        ball.move_right(800)

    screen.fill((255, 255, 255))
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()