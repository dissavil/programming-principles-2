import pygame
import os
import datetime

class Clock:
    def __init__(self,screen):
        self.clock = pygame.image.load("images/clock.png")
        self.left = pygame.image.load("images/hand_left_centered.png")
        self.right = pygame.image.load("images/hand_right_centered.png")
        self.mickey = pygame.image.load("images/mikkey.png")
        self.screen = screen
    
    def draw(self):
        self.screen.blit(self.clock, (0, 0))
        self.screen.blit(self.mickey, (180, 0))
    def hands(self):
        self.now_date = datetime.datetime.now()
        self.hour = self.now_date.strftime("%I")
        self.minute = self.now_date.strftime("%M")
        self.angle_right = ((int(self.minute) / 60) + int(self.hour)) * 30
        self.angle_left = int(self.minute * 6)
        self.rotated_right = pygame.transform.rotate(self.right, 30)
        self.rotated_left = pygame.transform.rotate(self.left, self.angle_left)
        
        self.screen.blit(self.rotated_right, (768, 150))
        self.screen.blit(self.rotated_left, (0, 0))