def solve():
    n, d, k = [int(x) for x in input().split()]

    # Направления: вправо, вверх, влево, вниз
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_index = 0  # Начинаем с направления вправо

    visited = set()
    x, y = 0, 0
    visited.add((x, y))
    remaining_moves = n

    current_d = d  # текущий шаг
    steps_in_direction = 0

    while remaining_moves > 0:
        dx, dy = directions[dir_index]
        for _ in range(current_d):
            if remaining_moves == 0:
                break
            x += dx
            y += dy
            visited.add((x, y))
            remaining_moves -= 1

        dir_index = (dir_index + 1) % 4  # циклический проход по массиву
        steps_in_direction += 1

        if steps_in_direction % 2 == 0:
            current_d *= k

    # Находим минимальные координаты для сдвига
    min_x = min(x for x, y in visited)
    min_y = min(y for x, y in visited)

    # Сдвигаем все координаты так, чтобы минимальные были (0, 0)
    shifted_visited = set()
    for (x, y) in visited:
        shifted_x = x - min_x
        shifted_y = y - min_y
        shifted_visited.add((shifted_x, shifted_y))

    # Находим размеры таблицы
    max_x = max(x for x, y in shifted_visited)
    max_y = max(y for x, y in shifted_visited)
    h = max_y + 1
    w = max_x + 1

    print(h, w)

    # Создаем таблицу и заполняем её
    for y_pos in range(max_y, -1, -1):
        row = []
        for x_pos in range(max_x + 1):
            if (x_pos, y_pos) in shifted_visited:
                row.append('*')
            else:
                row.append('.')
        print(''.join(row))


solve()
