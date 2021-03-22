def fib0(n):
    if n <= 2: return 1
    return fib0(n - 1) + fib0(n - 2)

def fib1(n):
    if n < 1 :
        return 0

    memo = [0] * (n + 1)
    return helper(memo, n)
def helper(memo, n):

    if n <= 2: return 1

    if memo[n] != 0: return memo[n]

    memo[n] = helper(memo, n - 1) + helper(memo, n - 2)
    return memo[n]

def fib2(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n - 1]

# 状态压缩
def fib3(n):

    if n <= 2: return 1

    prev = 1
    curr = 1

    for i in range(2, n):
        sum = prev + curr
        prev = curr
        curr = sum

    return curr

# 矩阵快速幂
def fib4(n):
    pass

if __name__ == '__main__':

    import time
    n = 5
    s1 = time.time()
    # print(fib0(n))

    s2 = time.time()
    # print(fib1(n))

    # print(fib2(n))

    print(fib3(n))

