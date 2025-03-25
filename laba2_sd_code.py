def josephus(n, m):
    res = 0  # Начинаем с 0 для удобства (позиции с 0 в вычислениях)
    for i in range(2, n + 1):
        res = (res + m) % i
    return res + 1  # Переводим в 1-индексацию


def find_starting_position(n, m, l):
    for start in range(1, n + 1):
        if josephus(n, m) == l:
            return start
    return -1  # В случае ошибки


N = 10  # Количество людей
M = 3   # Счет до M
L = josephus(N, M)  # Находим последнего оставшегося
print(f"Последний оставшийся: {L}")

start_position = find_starting_position(N, M, L)
print(f"Начальная позиция: {start_position}")