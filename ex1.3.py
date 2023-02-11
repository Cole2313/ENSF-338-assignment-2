def func(n, fibnum = {}):
    if n == 0 or n == 1:
        return n
    for num in fibnum:
        if num == n:
            return fibnum[n]
    fibnum[n] = func(n-1) + func(n-2)
    return fibnum[n]

