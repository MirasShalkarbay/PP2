import pygame

pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Circle")

circle_speed = 20
circle_x = 200
circle_y = 100

clock = pygame.time.Clock()

running = True
while running:

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, "Red", (circle_x, circle_y),25)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and circle_x > 50:
        circle_x -= circle_speed
    elif keys[pygame.K_RIGHT] and circle_x < width - 50:
        circle_x += circle_speed
    
    if keys[pygame.K_UP] and circle_y > 50:
        circle_y -= circle_speed
    elif keys[pygame.K_DOWN] and circle_y < height - 50:
        circle_y += circle_speed
    
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(10)