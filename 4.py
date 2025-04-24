n = 13
d = 2
k = 2

field = [['.' for _ in range(10)] for _ in range(10)]
row, col = 9, 0
direction = 'right'
for _ in range(10):
    if direction == 'right' and col + d < len(field[0]):
        field[row] = field[:col] + ['*'] * d + field[row][col + d:]
        col += d - 1
        direction = 'up'
        continue
    elif direction == 'up' and row - d < len(field):
        for _ in range(d):
            row -= 1
            field[row] = field[row][:col] + ['*'] + field[row][col + 1:]
        direction = 'left'
        continue
    else:
        d *= k

for i in range(10):
    print(field[i])
