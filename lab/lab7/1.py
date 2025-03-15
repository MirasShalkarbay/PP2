import pygame
import datetime

pygame.init()

width, height = 501, 501
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Clock')

left_hand = pygame.transform.scale(pygame.image.load('img/left.png'), (400, 330))
right_hand = pygame.transform.scale(pygame.image.load('img/right.png'), (200, 220))
background_mickie = pygame.transform.scale(pygame.image.load('img/mickie.jpg'), (width, height))

center = (width / 2, height / 2) 

clock = pygame.time.Clock()

running = True
while running:

    current_time = datetime.datetime.now()
    minute = current_time.minute
    second = current_time.second

    min_angle = -(minute * 6)  # 360 / 60 мин  = 6 в минуту
    sec_angle = -(second * 6)  # 360 / 60 сек = 6 в сек   
                               # "-" потому что по дефолту идет против часовой

    rotated_left_hand = pygame.transform.rotate(left_hand, sec_angle)
    rotated_right_hand = pygame.transform.rotate(right_hand, min_angle)

    left_rect = rotated_left_hand.get_rect(center=center)
    right_rect = rotated_right_hand.get_rect(center=center)

    screen.blit(background_mickie, (0, 0))  
    screen.blit(rotated_right_hand, right_rect.topleft)   
    screen.blit(rotated_left_hand, left_rect.topleft)  

    pygame.display.update()
    clock.tick(1) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
