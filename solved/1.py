n = int(input())
a1, a2 = [], []
s1, s2 = 0, 0
for i in range(n):
    if i % 2 == 0:
        a1.append(int(input()))
    else:
        a2.append(int(input()))
s1, s2 = sum(a1), sum(a2)
if s1 == s2:
    print('Yes')
    quit()

if s1 < s2:
    a1, a2 = a2, a1
    s1, s2 = s2, s1
a1.sort()
a2.sort()
i, j = 0, 0
while i < len(a1) and j < len(a2):
    news1 = s1 - a1[i] + a2[j]
    news2 = s2 - a2[j] + a1[i]
    if news1 == news2:
        print('Yes')
        quit()
    if news1 < news2:
        j += 1
    else:
        i += 1
print('No')

