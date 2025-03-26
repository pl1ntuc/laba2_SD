def josephus(n, m):
    """Возвращает номер последнего оставшегося человека."""
    res = 0
    for i in range(2, n + 1):
        res = (res + m) % i
    return res + 1


def find_starting_position(n, m, l):
    """Определяет начальную позицию, если известен последний оставшийся номер."""
    for start in range(1, n + 1):
        if josephus(n, m) == l:
            return start
    return -1  # В случае ошибки


N = 10
M = 3
L = josephus(N, M)
print(f"Последний оставшийся: {L}")

start_position = find_starting_position(N, M, L)
print(f"Начальная позиция: {start_position}")

author_info = "Автор: Полина Рубцова Алексеевна"
print(author_info)