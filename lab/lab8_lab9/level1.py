import pygame, sys
from worm import Snake  # Импортируем класс Snake из модуля 'worm'

pygame.init()  # Инициализируем Pygame

def level1(score):
    window = pygame.display.set_mode((850, 600))  # Создаём игровое окно

    clock = pygame.time.Clock()  # Создаём объект Clock для управления частотой кадров
    fps = 5  # Количество кадров в секунду

    font = pygame.font.Font(None, 36)  # Создаём объект шрифта для отображения текста
    text = font.render("level1", True, (255, 255, 255))  # Рендерим текст для отображения

    apple = (4, 18)  # Начальная позиция яблока

    walls = [(10, 10), (10, 11)]  # Координаты блоков-стен

    snake = Snake([(6, 4), (5, 4)], walls)  # Создаём объект змейки с начальными позициями и стенами

    fruit = 1  # Индикатор типа фрукта

    direct = 0  # Начальное направление движения змейки
    fail = False  # Флаг, указывающий на окончание игры

    # Главный игровой цикл
    while len(snake.pos) < 6:  # Продолжаем игру, пока длина змейки не достигнет 6
        for e in pygame.event.get():  # Обрабатываем события Pygame
            if e.type == pygame.QUIT:  # Если игрок закрыл игру
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:  # Если нажата клавиша
                # Изменяем направление змейки в зависимости от нажатой клавиши
                if e.key == pygame.K_UP and direct != 1:
                    direct = 3
                elif e.key == pygame.K_DOWN and direct != 3:
                    direct = 1
                elif e.key == pygame.K_LEFT and direct != 0:
                    direct = 2
                elif e.key == pygame.K_RIGHT and direct != 2:
                    direct = 0

        # Обновляем позицию яблока, счёт и тип фрукта после съедения яблока
        apple, score, fruit = snake.eat(apple, score, fruit)

        # Определяем цвет яблока в зависимости от его типа
        if fruit == 1:
            color = (255, 0, 0)  # Красный
        elif fruit == 2:
            color = (255, 255, 0)  # Жёлтый
        else:
            color = (0, 0, 255)  # Синий

        score_text = font.render("score: " + str(score), True, (255, 255, 255))  # Рендерим текст счёта

        # Двигаем змейку и проверяем столкновение
        fail = snake.move(direct)
        while fail:  # Если змейка столкнулась с собой
            for e in pygame.event.get():  # Ожидаем выхода из игры
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # Обновляем отображение игры
        window.fill((0, 0, 0))  # Заполняем фон чёрным цветом
        pygame.draw.rect(window, color, (25*apple[0], 25*apple[1], 25, 25))  # Рисуем яблоко
        for i in walls:  # Рисуем стены
            pygame.draw.rect(window, (122, 122, 122), (25*i[0], 25*i[1], 25, 25))
        snake.draw(window)  # Рисуем змейку
        window.blit(text, (750, 15))  # Отображаем текст уровня
        window.blit(score_text, (15, 15))  # Отображаем счёт
        pygame.display.flip()  # Обновляем экран
        clock.tick(fps)  # Контролируем частоту кадров
    
    return score  # Возвращаем финальный счёт
