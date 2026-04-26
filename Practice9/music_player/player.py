import pygame
from mutagen.mp3 import MP3

pygame.font.init()

class Player():
    def __init__(self, playlist,screen):
        self.playlist = playlist
        self.index = 0
        self.track = ""
        self.text = ""
        self.screen = screen
        self.font = pygame.font.SysFont( "comicsansms" ,  32 )
        self.track_length = 1
        self.audio = 0

    def play(self):
        pygame.mixer.music.load(self.playlist[self.index])
        pygame.mixer.music.play()
        self.track = self.playlist[self.index]
        self.audio = MP3(self.track)
        self.track_length = self.audio.info.length

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.index = (self.index + 1) % len(self.playlist)
        self.play()

    def previous(self):
        self.index = (self.index - 1) % len(self.playlist)
        self.play()
    def draw(self):
        if self.track:
            name = self.track.split("/")[-1].replace(".mp3", "")
            text = self.font.render(name, True, (255, 255, 255))
            self.screen.blit(text, (50, 40))