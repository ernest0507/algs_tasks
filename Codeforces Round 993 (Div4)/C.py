t = int(input())
data = [[int(x) for x in input().split()] for _ in range(t)]

for i in range(t):
    count = 0
    m, a, b, c = data[i]
    row1 = m
    row2 = m
    if row1 > a:
        count += a
        row1 -= a
    else:
        count += row1
        row1 = 0

    if row2 > b:
        count += b
        row2 -= b
    else:
        count += row2
        row2 = 0

    if row1 + row2 > c:
        count += c
    else:
        count += row1 + row2
    print(count)
