n = int(input())
a = [int(input()) for _ in range(n)]
even, odd = 0, 0
for i in range(n):
    if i % 2 == 0:
        even += a[i]
    else:
        odd += a[i]

if even != odd:
    for x in a:
        for y in a:
            delta = abs(x - y)
            if (even - delta == odd + delta) or (even + delta == odd - delta):
                print('Yes')
                exit()

print('No')
