# time: O(2^n)
# space: O(n)
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# time: O(n)
# space: O(n)
def fib_memo(n, memo={}):
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib_memo(50))  # 12586269025
