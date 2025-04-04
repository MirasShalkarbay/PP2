import pygame, sys
from worm import Snake  # Импорт класса Snake из модуля 'worm'

pygame.init()  # Инициализация Pygame

def level3(score):
    window = pygame.display.set_mode((850, 600))  # Создание игрового окна

    clock = pygame.time.Clock()  # Создание часов Pygame для управления частотой кадров
    fps = 8  # Количество кадров в секунду

    font = pygame.font.Font(None, 36)  # Создание объекта шрифта для отображения текста
    text = font.render("level1", True, (255, 255, 255))  # Отображение текста "level1" (ошибка — надо бы "level3")

    apple = (15, 9)  # Начальная позиция яблока

    walls = [(7, 18), (4, 12), (15, 5), (2, 8), (11, 3), (19, 17), (6, 0), (13, 9)]  # Координаты блоков-стен

    snake = Snake([(6, 4), (5, 4)], walls)  # Создание объекта змейки с начальными координатами и стенами

    fruit = 1  # Индикатор типа фрукта

    direct = 0  # Начальное направление движения змейки
    fail = False  # Флаг окончания игры (столкновение)

    # Главный игровой цикл
    while len(snake.pos) < 6:  # Игра продолжается, пока длина змейки меньше 6
        for e in pygame.event.get():  # Обработка событий Pygame
            if e.type == pygame.QUIT:  # Если игрок закрыл окно
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:  # Если нажата клавиша
                # Изменение направления змейки в зависимости от нажатой клавиши
                if e.key == pygame.K_UP and direct != 1:
                    direct = 3  # Вверх
                elif e.key == pygame.K_DOWN and direct != 3:
                    direct = 1  # Вниз
                elif e.key == pygame.K_LEFT and direct != 0:
                    direct = 2  # Влево
                elif e.key == pygame.K_RIGHT and direct != 2:
                    direct = 0  # Вправо

        # Обновление позиции яблока, счёта и типа фрукта, если змейка его съела
        apple, score, fruit = snake.eat(apple, score, fruit)

        # Определение цвета яблока в зависимости от типа фрукта
        if fruit == 1:
            color = (255, 0, 0)  # Красный
        elif fruit == 2:
            color = (255, 255, 0)  # Жёлтый
        else:
            color = (0, 0, 255)  # Синий

        score_text = font.render("score: " + str(score), True, (255, 255, 255))  # Отображение текста со счётом

        # Движение змейки и проверка на столкновение
        fail = snake.move(direct)
        while fail:  # Если змейка столкнулась (с собой или стеной)
            for e in pygame.event.get():  # Ожидание выхода пользователя
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # Обновление отображения на экране
        window.fill((0, 0, 0))  # Заливка фона чёрным цветом
        pygame.draw.rect(window, color, (25*apple[0], 25*apple[1], 25, 25))  # Отрисовка яблока
        for i in walls:  # Отрисовка стен
            pygame.draw.rect(window, (122, 122, 122), (25*i[0], 25*i[1], 25, 25))
        snake.draw(window)  # Отрисовка змейки
        window.blit(text, (750, 15))  # Отображение уровня
        window.blit(score_text, (15, 15))  # Отображение счёта
        pygame.display.flip()  # Обновление экрана
        clock.tick(fps)  # Задержка для ограничения частоты кадров
    
    return score  # Возврат финального счёта
