N = int(input())
matr = [[int(x) for x in input().split()] for _ in range(N)]

ms1, ms2 = float('inf'), float('inf')
ind1, ind2, ind3 = 0, 0, 0
for i in range(N):
    s1, s2 = sorted(matr[i])[1:3]
    if s1 < ms1 and s2 < ms2:
        ms1 = s1
        ms2 = s2
        ind1 = i
        ind2 = matr[i].index(s1)
        ind3 = matr[i].index(s2)

print(ind1 + 1, ind2 + 1, ind3 + 1)

