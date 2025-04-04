import pygame
import random

class Snake:
    def __init__(self, pos, walls):
        # Инициализация змейки с её начальными координатами и стенами
        self.pos = pos  # Позиции змейки
        self.possible_possition = [(i, j) for i in range(34) for j in range(24)]  # Все возможные позиции на игровом поле
        self.possible_possition.append((-1, -1))  # Специальная позиция для обозначения нового сегмента змейки
        self.time = 0  # Счётчик времени (ходов)

        # Удаляем стартовые позиции змейки и стены из списка возможных позиций
        for i in pos:
            self.possible_possition.remove(i)
        for i in walls:
            self.possible_possition.remove(i)

    def move(self, direct):
        # Двигаем змейку в заданном направлении
        if direct == 0:
            self.pos.insert(0, (self.pos[0][0]+1, self.pos[0][1]))  # Вправо
        elif direct == 1:
            self.pos.insert(0, (self.pos[0][0], self.pos[0][1]+1))  # Вниз
        elif direct == 2:
            self.pos.insert(0, (self.pos[0][0]-1, self.pos[0][1]))  # Влево
        else:
            self.pos.insert(0, (self.pos[0][0], self.pos[0][1]-1))  # Вверх
        try:
            self.possible_possition.remove(self.pos[0])  # Удаляем новую позицию головы из возможных
        except:
            return True  # Столкновение — возвращаем True
        self.possible_possition.append(self.pos[-1])  # Добавляем старый хвост обратно в возможные позиции
        self.pos.pop()  # Удаляем старый хвост

    def eat(self, a, s, t):
        # Метод обработки съедания яблока
        self.time += 1  # Увеличиваем счётчик времени
        if self.pos[0][0] == a[0] and self.pos[0][1] == a[1] or self.time > 30:  # Если съели яблоко или прошло 30 ходов
            self.possible_possition.remove((-1, -1))  # Удаляем спецпозицию из списка
            a = random.choice(self.possible_possition)  # Случайная новая позиция яблока
            if self.time > 30:  # Если прошло 30 ходов без еды
                self.possible_possition.append((-1, -1))  # Возвращаем спецпозицию
            else:
                self.pos.append((-1, -1))  # Добавляем новый сегмент змейки
                s += t  # Увеличиваем счёт
            self.time = 0  # Сброс счётчика времени
            t = random.randint(1, 3)  # Новый тип фрукта
        return a, s, t  # Возвращаем новые данные: позицию яблока, счёт, тип фрукта

    def draw(self, window):
        # Отрисовка змейки на игровом окне
        for i in range(len(self.pos)):
            pygame.draw.rect(window, (0, 255, 0), (self.pos[i][0]*25, self.pos[i][1]*25, 25, 25))  # Рисуем каждый сегмент змейки
