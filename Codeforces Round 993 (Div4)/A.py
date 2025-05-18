t = int(input())
nums = [int(input()) for _ in range(t)]

counts = []
for n in nums:
    count = 0
    for b in range(1, n):
        if 1 <= n - b <= 2 * n:
            count += 1
    counts.append(count)

print(*counts, sep='\n')
