bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1


def f(arr, c, k):
    a = ['x' if x <= c else '_' for x in arr]
    count, total_count = 0, 0
    for i in range(len(a)):
        if a[i] == 'x':
            count += 1
        else:
            total_count += count // k
            count = 0
    total_count += count // k
    return total_count


if m * k > len(bloomDay):
    print(-1)
    exit()

l, r = 0, max(bloomDay)
while l + 1 != r:
    c = (l + r) // 2
    if f(bloomDay, c, k) < m:
        l = c
    else:
        r = c
print(r)
