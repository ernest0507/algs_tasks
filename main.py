s = 'z'
t = 'abcde'

i, j = 0, 0
flag = False
while i < len(s) and j < len(t) and s[i] == t[j]:
    flag = True
    i += 1
    j += 1

if flag:
    if j == len(t):
        print(s)
    else:
        print(s + t)
else:
    print(s + t[j:])
