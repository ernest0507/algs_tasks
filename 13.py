s = list(input())
j = 0
i = 0
while j < 3:
    if s[i] == 'cat'[j]:
        s[i] = 'CAT'[j]
        j += 1
    i += 1
print(''.join(s))
