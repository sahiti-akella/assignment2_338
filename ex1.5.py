import time
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def memo_func(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = memo_func(n-1, memo) + memo_func(n-2, memo)
    return memo[n]

numbers = range(36)
time_func = []
time_memo_func = []
for n in numbers:
    start_func = time.time()
    func(n)
    end_func = time.time()
    time_func.append(end_func - start_func)
    start_memo_func = time.time()
    memo_func(n)
    end_memo_func = time.time()
    time_memo_func.append(end_memo_func - start_memo_func)

plt.plot(numbers, time_func, label='func(Original)')
plt.plot(numbers, time_memo_func, label='memo_func(Optimized)')
plt.xlabel('n')
plt.ylabel('Time(s)')
plt.legend()
plt.show()
