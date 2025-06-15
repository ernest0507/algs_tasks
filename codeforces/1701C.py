for _ in range(int(input())): # входные данные
    n, m = [int(x) for x in input().split()] # входные данные
    nums = [int(x) for x in input().split()]# входные данные

    # подсчитываю кол-во задач для каждого рабочего
    cnt = [0] * (n + 1)
    for i in nums:
        cnt[i] += 1


    def f(T):
        global cnt
        count = 0
        for i in range(1, n + 1):
            count += (T - min(T, cnt[i])) // 2 + min(T, cnt[i])
        return count


    l, r = 0, 10
    while l + 1 != r:
        c = (l + r) // 2
        if f(c) < m:
            l = c
        else:
            r = c

    print(r)
