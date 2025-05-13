# первое решение
# O (n * m)
# n = 6
# a = [3, 3, 3, 4, 4, 5]
# m, k = 7, 0
# indexes = [1, 2, 3, 4, 5, 6, 7]
# for ind in indexes:
#     cur_k = k
#     ind -= 1
#     while ind >= 1:
#         if (a[ind] < a[ind - 1]) or (cur_k == 0 and a[ind] == a[ind - 1]):
#             break
#         if a[ind] == a[ind - 1]:
#             cur_k -= 1
#         ind -= 1
#     print(ind + 1, end=' ')


# второе решение
n = 7
a = [1, 5, 7, 2, 10, 10, 6]
m, k = 7, 0
indexes = [1, 2, 3, 4, 5, 6, 7]
segments = []
cur_k = k
j = n - 1
for i in range(n - 1, 0, -1):
    if (a[i] == a[i - 1] and cur_k == 0) or (a[i] < a[i - 1]):
        cur_k = k
        segments.append([i + 1, j + 1])
        j = i - 1
    elif a[i] == a[i - 1]:
        cur_k -= 1

segments.append([1, j + 1])
print(segments)
