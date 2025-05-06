n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
offers = [int(x) for x in input().split()]

data = []
for i in range(n):
    data.append((i + 1, a[i], b[i]))

data.sort(key=lambda x: (x[1] + x[2]), reverse=True)

for x in offers:
    i, j = 0, 1
    if x == 0:
        if data[i][1] == data[j][1]:
            while data[i][1] == data[j][1] and data[i][2] == data[j][2]:
                j += 1


