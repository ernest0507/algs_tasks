n = int(input())
a = [int(x) for x in input().split()]

count = [0] * 5  # создаем массив для подсчета чисел по разрядам

for num in a:  # заполняем массив count
    count[len(str(num))] += 1

total = 1
for num in a:
    for i in range(1, 5):
        if count[i] != 0:
            total *= num * 10 ** len(str(num)) * count[i]
            total *= num * count[i]

print(total)
print(11 * 22 * 21 * 12)
