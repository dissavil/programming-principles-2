import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 25
        self.color = (255, 0, 0)
        self.step = 20

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move_up(self):
        if self.y - self.step >= self.radius:
            self.y -= self.step

    def move_down(self, height):
        if self.y + self.step <= height - self.radius:
            self.y += self.step

    def move_left(self):
        if self.x - self.step >= self.radius:
            self.x -= self.step

    def move_right(self, width):
        if self.x + self.step <= width - self.radius:
            self.x += self.step