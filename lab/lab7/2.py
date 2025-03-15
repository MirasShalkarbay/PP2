import pygame

pygame.init()

width, height = 800, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('MusicBox')

Play = pygame.image.load('img/play.png')
Stop = pygame.image.load('img/stop.png')
Next = pygame.image.load('img/next.png')
Previous = pygame.image.load('img/past.png')

playlist = ['sounds/ACDC.mp3', 'sounds/Eminem.mp3', 'sounds/NEFFEX.mp3']
music_index = 0  

def play_music():
    pygame.mixer.music.load(playlist[music_index])
    pygame.mixer.music.play()

play_music()

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(Play, (50, 50))
    screen.blit(Stop, (200, 50))
    screen.blit(Next, (350, 50))
    screen.blit(Previous, (500, 50))

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                music_index -= 1
                if music_index < 0:
                    music_index = len(playlist) - 1
                play_music()

            elif event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                music_index += 1
                if music_index >= len(playlist):
                    music_index = 0
                play_music()   

            elif event.key == pygame.K_UP:
                pygame.mixer.music.unpause()

            elif event.key == pygame.K_DOWN:
                pygame.mixer.music.pause()
