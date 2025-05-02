n = int(input())
nums = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]

# Направления влево, вниз, вправо, вверх
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_index = 0
x, y = (2 * n + 1) // 2 - 1, (2 * n + 1) // 2 + 1
a = 1
steps = 2
k = 0
d = steps + k
flag = True
flag2 = True
while flag2:
    if flag:
        runs = 3
        flag = False
    else:
        runs = 2
    for _ in range(runs):
        dx, dy = directions[dir_index]
        for _ in range(d):
            x += dx
            y += dy
            nums[x][y] = a
            if x == 0 and y == 2 * n:
                flag2 = False
                break
            a += 1
        if not flag2:
            break
        dir_index = (dir_index + 1) % 4
    k += 1
    d = steps + k

res = []
for i in nums:
    res.append(' '.join(map(str, i)))

print(*res, sep='\n')
