import pygame
import sys
import time

# Inisialisasi pygame
pygame.init()

# Tentukan ukuran layar
screen_width = 800
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lirik Lagu 'Blue' - Yung Kai")

# Warna
white = (255, 255, 255)
black = (0, 0, 0)

# Font dan ukuran
font_size = 24
font = pygame.font.SysFont(None, font_size)

# Lirik lagu
lyrics = (
    "Your morning eyes, I could stare like watching stars "
    "I could walk you by, and I'll tell without a thought "
    "You'd be mine, would you mind if I took your hand tonight? "
    "Know you're all that I want this life "
    "I'll imagine we fell in love "
    "I'll nap under moonlight skies with you "
    "I think I'll picture us, you with the waves "
    "The ocean's colors on your face "
    "I'll leave my heart with your air "
    "So let me fly with you "
    "Will you be forever with me? "
    "My love will always stay by you "
    "I'll keep it safe, so don't you worry a thing, I'll tell you I love you more "
    "It's stuck with you forever, so promise you won't let it go "
    "I'll trust the universe will always bring me to you "
    "I'll imagine we fell in love "
    "I'll nap under moonlight skies with you "
    "I think I'll picture us, you with the waves "
    "The ocean's colors on your face "
    "I'll leave my heart with your air "
    "So let me fly with you "
    "Will you be forever with me?"
)

# Konversi lirik menjadi surface
text_surface = font.render(lyrics, True, black)
text_width, text_height = text_surface.get_size()

# Posisi awal teks
x = screen_width
y = (screen_height - text_height) // 2

# Muat dan mainkan musik
pygame.mixer.music.load("yung kai - blue (Official Audio).mp3")  # Ganti dengan path file Anda
pygame.mixer.music.play()

# Dapatkan durasi lagu
song_duration = pygame.mixer.Sound("yung kai - blue (Official Audio).mp3").get_length()

# Kecepatan gerak teks
speed = (text_width + screen_width) / song_duration

# Loop utama
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gerakkan teks ke kiri
    x -= speed * clock.get_time() / 1000

    # Jika teks sudah sepenuhnya lewat, reset posisinya
    if x < -text_width:
        x = screen_width

    # Gambar background dan teks
    screen.fill(white)
    screen.blit(text_surface, (x, y))
    pygame.display.flip()

    # Batasi frame rate
    clock.tick(60)

pygame.quit()
sys.exit()