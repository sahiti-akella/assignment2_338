def memo_func(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = memo_func(n-1, memo) + memo_func(n-2, memo)
    return memo[n]

print(memo_func(1))