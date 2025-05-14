n = int(input()) # кол-во коробок
boxes = [[int(x) for x in input().split()] for _ in range(n)] + [[0, 0]]

boxes[-1] = [boxes[0][1], 0]
boxes[0][1] = 0
for i in range(n + 1):
    if boxes[i][1] == 0:
        find = boxes[i][0]
        for j in range(i + 1, n + 1):
            if boxes[j][1] == find:
                boxes[i][1] = find
                boxes[j][1] = 0
                break
            if boxes[j][1] == 0 and boxes[j][0] == find:
                boxes[i][1] = find
                boxes[j][0] = 0
                break



print(boxes)

