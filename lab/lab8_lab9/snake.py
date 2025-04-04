# Импорт функций уровней из соответствующих модулей
from level1 import level1
from level2 import level2
from level3 import level3

# Инициализация переменной счёта значением 0
score = 0

# Последовательно выполняем каждую функцию уровня и обновляем счёт
score = level1(score)  # Выполнить уровень 1 и обновить счёт
score = level2(score)  # Выполнить уровень 2 и обновить счёт
score = level3(score)  # Выполнить уровень 3 и обновить счёт
