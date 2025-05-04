n, m1, m2 = 4, 1, 2
intervals = [(0, 4), (1, 5), (2, 6), (3, 4)]
intervals.sort()

count = 0
for i in range(n):
    l1, r1 = intervals[i]
    prevs = []
    for j in range(i + 1, n):
        l2, r2 = intervals[j]
        if max(l1, l2) < min(r1, r2) and m1 <= min(r1, r2) - max(l1, l2) <= m2:
            count += 1
            if len(prevs) > 0:
                count += j - i - 1
        prevs.append([l2, r2])


print(count)