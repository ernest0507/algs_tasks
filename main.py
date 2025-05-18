n = int(input())
boxes = [[int(x) for x in input().split()] for _ in range(n)] + [[]]

dct_ind = {}  # словарь для хранения текущего расположения шара
for i in range(n):
    dct_ind[boxes[i][0]] = dct_ind.get(boxes[i][0], []) + [i]
    dct_ind[boxes[i][1]] = dct_ind.get(boxes[i][1], []) + [i]

count = 0
sequences = []
for i in range(n):
    balloon1, balloon2 = boxes[i]
    if balloon1 != balloon2:
        if dct_ind[balloon1][0] != i:  # получаю индекс шара, которой нужно переложить
            ind = dct_ind[balloon1][0]
        else:
            ind = dct_ind[balloon1][1]

        # перекладываю второй шар в пустую коробку
        boxes[n].append(balloon2)
        sequences.append([i, n])
        count += 1

        # проверяем снизу или сверху находится необходимый шар
        # если сверху
        if boxes[ind][1] == balloon1:
            # просто перекидываем шар к своему цвету
            boxes[i] = [balloon1, balloon1]
            sequences.append([ind, i])
            count += 1
            boxes[n] = []
            # перекладываем второй шар на новое место
            boxes[ind][1] = balloon2
            sequences.append([n, ind])
            count += 1

            # переписываем переменные
            dct_ind[balloon1] = [i, i]
            if dct_ind[balloon2][0] == i:
                dct_ind[balloon2][0] = ind
            else:
                dct_ind[balloon2][1] = ind
        # если снизу
        else:
            boxes[n].append(boxes[ind][1])
            count += 1

            # соединяю два шара одного цвета вместе
            boxes[i] = [balloon1, balloon1]
            sequences.append([ind, i])
            count += 1

            # перекладываю два шара из запасной коробки в новую
            boxes[ind] = boxes[n]
            sequences.append([n, ind])
            sequences.append([n, ind])
            boxes[n] = []
            count += 2

            # переписываю индексы для шаров
            dct_ind[balloon1] = [i, i]

            if dct_ind[balloon2][0] == i:
                dct_ind[balloon2][0] = ind
            else:
                dct_ind[balloon2][1] = ind


print(count)
for s in sequences:
    print(*s)
