from math import log
t = int(input())
data = [[int(x) for x in input().split()] for _ in range(t)]

for i in range(t):
    k, l1, r1, l2, r2 = data[i]
    count = 0
    if l1 > l2:
        l1, l2 = l2, l1
        r1, r2 = r2, r1
    for x in range(l1, r1 + 1):
        y = l2
        while y % x != 0:
            y += 1
        while l2 <= y <= r2:
            if log((y / x), k).is_integer():
                count += 1
            y += x

    print(count)
