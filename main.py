n, m, k, p = [int(x) for x in input().split()]
lst = [[x for x in input().split()] for _ in range(p)]
constraints = {}
for cons_type, num_student, row, col in lst:
    constraints[int(num_student)] = [cons_type, int(row), int(col)]
q = int(input())
commands = [[int(x) for x in input().split()[1:]] for _ in range(q)]

matr = [[0] * m for _ in range(n)]  # представление мест в аудитории в виде матрицы

occupied = {}  # для записи занятых мест
count = 0  # счетчик нарушений
for student, row, column in commands:
    if student in occupied:  # если ученик уже сидел на каком-то месте
        matr[occupied[student][0]][occupied[student][1]] = 0  # освобождаем место
        del occupied[student]
    if matr[row - 1][column - 1] == 0:  # если свободное, то сажаем
        matr[row - 1][column - 1] = 1
        occupied[student] = [row - 1, column - 1]  # записываем ученика в словарь
    else:  # если пытаемся усадить уже на занятое место
        count += 1
    if student in constraints:  # проверка на ограничения
        if constraints[student][0] == 'R':
            if not (constraints[student][1] <= row <= constraints[student][2]):
                count += 1
        else:
            if not (constraints[student][1] <= column <= constraints[student][2]):
                count += 1

print(k - q + count)
