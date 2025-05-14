n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
nums.sort()


# O(n logn)
# ломает на тесте 5 5 5 5 5, k = 10
def solution1(n, k, nums):
    def bs(a, x, y):
        l, r = -1, len(a) - 1
        while l + 1 != r:
            c = (l + r) // 2
            if a[c] + x < y:
                l = c
            else:
                r = c
        return a[r]

    count = 0
    for num1 in nums[::-1]:
        num2 = bs(nums, num1, k)
        if num1 + num2 == k:
            count += 1

    return count // 2


# O(n)
# ломает на тесте 1 1 3 3 3 5, k = 6
def solution2(n, k, nums):
    count = 0
    i, j = 0, n - 1
    while i != j and j > 0 and i < n:
        cur_sum = nums[i] + nums[j]
        if cur_sum == k:
            count += 1
            j -= 1
        elif cur_sum < k:
            i += 1
        elif cur_sum > k:
            j -= 1

    return count


# from random import randint
# for _ in range(100):
#     n = randint(5, 10)
#     k = randint(1, 15)
#     nums = [randint(1, 20) for _ in range(n)]
#     assert solution1(n, k, nums) == solution2(n, k, nums), f'solution1 - {solution1(n, k, nums)} | solution2 - {solution2(n, k, nums)} | {k, sorted(nums)}'
# #
print(solution1(n, k, nums))
print(solution2(n, k, nums))

import itertools


def min_elements_to_remove(n, k, arr):
    min_remove = n  # Изначально предполагаем худший случай - выключить все элементы

    # Перебираем все возможные комбинации включения/выключения
    for mask in itertools.product([0, 1], repeat=n):
        # Количество выключенных элементов в текущей комбинации
        count_removed = mask.count(0)

        # Если уже хуже текущего минимума, пропускаем проверку
        if count_removed >= min_remove:
            continue

        valid = True  # Флаг, что текущая комбинация допустима

        # Проверяем все возможные пары включенных элементов
        for i in range(n):
            if not mask[i]:  # Если элемент выключен, пропускаем
                continue
            for j in range(i + 1, n):
                if not mask[j]:  # Если элемент выключен, пропускаем
                    continue
                # Проверяем запрещенную сумму
                if arr[i] + arr[j] == k:
                    valid = False
                    break  # Нашли запрещенную пару, дальше проверять бессмысленно
            if not valid:
                break  # Выходим из внешнего цикла, если нашли запрещенную пару

        # Если комбинация допустима и лучше текущего минимума
        if valid and count_removed < min_remove:
            min_remove = count_removed

    return min_remove


n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
print(min_elements_to_remove(n, k, nums))

