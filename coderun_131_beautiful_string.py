k = int(input())
s = input()

i, j = 0, 1
mcount = 0
while j < len(s):
    if s[i] == s[j]:
        if k + i + 1 < len(s):
            mcount = max(mcount, k + 2)
        else:
            mcount = max(mcount, len(s) - i)
        j += 1
    elif j - i - 1 != k:
        j += 1
    else:
        i += 1

print(k + 1) if mcount == 0 else print(mcount)
