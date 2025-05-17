n = int(input())
boxes = [[int(x) for x in input().split()] for _ in range(n)] + [[]]

dct_ind = {}  # словарь для хранения текущего расположения шара
for i in range(n):
    dct_ind[boxes[i][0]] = dct_ind.get(boxes[i][0], []) + [i]
    dct_ind[boxes[i][1]] = dct_ind.get(boxes[i][1], []) + [i]
count = 0
for i in range(n):
    balloon1, balloon2 = boxes[i]
    if balloon1 != balloon2:
        boxes[n].append(balloon2)
        ind1 = dct_ind[balloon1][1]
        if boxes[ind1][1] == balloon1:
            boxes[i] = [balloon1, balloon1]
            boxes[ind1][1] = boxes[n][0]
            dct_ind[balloon1] = [i, i]
            boxes[n] = []
            if dct_ind[balloon2][1] == ind1:
                dct_ind[balloon2][1] = ind1
            else:
                dct_ind[balloon2][0] = ind1
            count += 3
        else:
            boxes[n].append(boxes[ind1][1])
            boxes[i] = [balloon1, balloon1]
            boxes[ind1] = boxes[n]
            boxes[n] = []
            if dct_ind[balloon2][0] == i:
                dct_ind[balloon2][0] = ind1
            else:
                dct_ind[balloon2][1] = ind1
            count += 4

print(boxes)
print(count)
