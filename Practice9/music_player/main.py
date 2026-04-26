import pygame
from mutagen.mp3 import MP3
from player import Player

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 160))
pygame.display.set_caption("Music Player")

playlist = [
    "music/01. Radiohead - You.mp3",
    "music/Radiohead - Nice Dream.mp3",
    "music/Muse - Sunburn.mp3",
    "music/Aikyn Tolepbergen - Сені Сагындым.mp3",
    "music/Malcolm Todd - Roommates.mp3",
    "music/Макс Корж - Жить в кайф.mp3"
]

font = pygame.font.SysFont( "comicsansms" ,  16 )

player = Player(playlist, screen)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_b:
                player.previous()
            elif event.key == pygame.K_q:
                running = False

    pos = pygame.mixer.music.get_pos()

    if pos > 0:
        seconds = pos / 1000
    else:
        seconds = 0
    track_length = player.track_length
    progress = seconds / track_length
    progress = min(progress, 1)
    current_seconds = int(seconds)

    minutes = current_seconds // 60
    secs = current_seconds % 60

    total_minutes = int(track_length) // 60
    total_secs = int(track_length) % 60

    time_text = font.render(f"{minutes:02}:{secs:02} / {total_minutes:02}:{total_secs:02}", True, (255, 255, 255))

    screen.fill((255, 0, 0))

    player.draw() 
    screen.blit(time_text, (650, 90))
    pygame.draw.rect(screen, (200, 200, 200), (50, 120, 700, 8))
    pygame.draw.rect(screen, (0, 200, 0), (50, 120, 700 * progress, 8))

    pygame.display.flip()

pygame.quit()