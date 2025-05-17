n = int(input())
boxes = [[int(x) for x in input().split()] for _ in range(n)] + [[]]

dct_ind = {}  # словарь для хранения текущего расположения шара
for i in range(n):
    dct_ind[boxes[i][0]] = dct_ind.get(boxes[i][0], []) + [i]
    dct_ind[boxes[i][1]] = dct_ind.get(boxes[i][1], []) + [i]
dct_ind[n] = []

for i in range(n):
    balloon1, balloon2 = boxes[i]
    if balloon1 != balloon2:
        boxes[n].append(balloon2)
        # случай, когда нужный шар сверху
        if dct_ind[balloon1][1] != i:
            if dct_ind[balloon2][0] == dct_ind[balloon1][0]: # проверяем какую позицию в boxes нужно переписывать
                boxes[dct_ind[balloon1][1]][1] = balloon2 # переписываем элемент в boxes
                dct_ind[balloon2][0] = dct_ind[balloon1][1] # переписываем индекс для balloon2
            else:
                boxes[dct_ind[balloon1][0]][1] = balloon2
                dct_ind[balloon2][1] = dct_ind[balloon1][1]
            boxes[i] = [balloon1, balloon1]
        else:
            ind = boxes[dct_ind[balloon1][1]][1]
            boxes[n].append()
            boxes[i] = [balloon1, balloon1]
            boxes[]
