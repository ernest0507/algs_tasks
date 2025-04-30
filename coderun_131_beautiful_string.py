s = input()
k = int(input())

for i in range(len(s) - 1):
    j = len(s) - 1
    while i < j:
        if s[i] == s[j] and j - i - 1== k:
            print(j - i + 1)
            quit()
        else:
            j -= 1

print(k + 1)


