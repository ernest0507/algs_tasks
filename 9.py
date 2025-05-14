n, m = [int(x) for x in input().split()]
cars = list(input())
l = 0
if m == 0:
    countm, count = 0, 0
    for car in cars:
        if car == 'B':
            count += 1
        else:
            count = 0
        countm = max(countm, count)
    print(countm)
    quit()



while l < n and cars[l] != 'B':
    l += 1

countm = 0
whites = 0
for r in range(l, n):
    if cars[r] == 'W':
        whites += 1
    if whites >= m > 0:
        if cars[r] == 'W':
            countm = max(countm, r - l - whites - 1)
        else:
            countm = max(countm, r - l - whites + 1)
        while cars[l + 1] != 'B':
            l += 1
            whites -= 1
        l += 1
if l < n:
    countm = max(countm, r - l - whites + 1)
print(countm)
