import pygame, sys
from worm import Snake  # Импорт класса Snake из модуля 'worm'

pygame.init()  # Инициализация Pygame

def level2(score):
    window = pygame.display.set_mode((850, 600))  # Создание окна игры

    clock = pygame.time.Clock()  
    fps = 6 
    font = pygame.font.Font(None, 36)  
    text = font.render("level2", True, (255, 255, 255))  

    apple = (20, 18)  # Начальная позиция яблока

    walls = [(15, 10), (15, 11), (16, 10), (16, 11)]  # Координаты блоков стен

    snake = Snake([(6, 4), (5, 4)], walls)  # Создание объекта змейки с начальными координатами и стенами

    fruit = 1  # Тип фрукта

    direct = 0  # Начальное направление змейки (0 — вправо)
    fail = False  # Флаг, сигнализирующий о завершении игры

    # Главный игровой цикл
    while len(snake.pos) < 6:  # Игра продолжается, пока длина змейки меньше 6
        for e in pygame.event.get():  # Обработка событий Pygame
            if e.type == pygame.QUIT:  # Если пользователь закрыл окно
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:  # Если нажата клавиша
                # Изменение направления змейки
                if e.key == pygame.K_UP and direct != 1:
                    direct = 3  # Вверх
                elif e.key == pygame.K_DOWN and direct != 3:
                    direct = 1  # Вниз
                elif e.key == pygame.K_LEFT and direct != 0:
                    direct = 2  # Влево
                elif e.key == pygame.K_RIGHT and direct != 2:
                    direct = 0  # Вправо

        # Обновление позиции яблока, счёта и типа фрукта при поедании
        apple, score, fruit = snake.eat(apple, score, fruit)

        # Определение цвета яблока по типу фрукта
        if fruit == 1:
            color = (255, 0, 0)  # Красный
        elif fruit == 2:
            color = (255, 255, 0)  # Жёлтый
        else:
            color = (0, 0, 255)  # Синий

        score_text = font.render("score: " + str(score), True, (255, 255, 255))  # Отображение счёта

        # Движение змейки и проверка на столкновение
        fail = snake.move(direct)
        while fail:  # Если произошло столкновение (например, со стеной или собой)
            for e in pygame.event.get():  # Ожидание выхода пользователя
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # Отрисовка элементов на экране
        window.fill((0, 0, 0))  # Очистка экрана (чёрный фон)
        pygame.draw.rect(window, color, (25*apple[0], 25*apple[1], 25, 25))  # Рисуем яблоко
        for i in walls:  # Рисуем стены
            pygame.draw.rect(window, (122, 122, 122), (25*i[0], 25*i[1], 25, 25))
        snake.draw(window)  # Рисуем змейку
        window.blit(text, (750, 15))  # Отображение текста уровня
        window.blit(score_text, (15, 15))  # Отображение счёта
        pygame.display.flip()  # Обновление экрана
        clock.tick(fps)  # Ограничение частоты кадров

    return score  # Возврат финального счёта
