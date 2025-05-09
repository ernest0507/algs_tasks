r1, s1, p1 = [int(x) for x in input().split()]
r2, s2, p2 = [int(x) for x in input().split()]

'''
идея реализации: 
чтобы минимизировать кол-во проигрышей, необходимо максимизировать ничью и выигрыши 
прогоняю все эти моменты в первом цикле

а на момент второго цикла, значения переменных такие, что достичь минимального или максимального значения 
уже нельзя, остается только подсчитать исходы каждой игры и при необходимости просуммировать кол-во проигрышей 
'''
for i in range(3):
    if i == 0:
        if r2 >= r1:
            r2 -= r1
            r1 = 0

            if r2 >= s1:
                r2 -= s1
                s1 = 0
            else:
                s1 -= r2
                r2 = 0
        else:
            r1 -= r2
            r2 = 0
    elif i == 1:
        if s2 >= s1:
            s2 -= s1
            s1 = 0

            if s2 >= p1:
                s2 -= p1
                p1 = 0
            else:
                p1 -= s2
                s2 = 0
        else:
            s1 -= s2
            s2 = 0
    else:
        if p2 >= p1:
            p2 -= p1
            p1 = 0

            if p2 >= r1:
                p2 -= r1
                r1 = 0
            else:
                r1 -= p2
                p2 = 0
        else:
            p1 -= p2
            p2 = 0

print(r1, s1, p1)
print(r2, s2, p2)

count = 0
for i in range(3):
    if i == 0:
        if 0 < r2 <= p1:
            count += r2
    elif i == 1:
        if 0 < s2 <= r1:
            count += s2
    else:
        if 0 < p2 <= s1:
            count += p2

print(count)
