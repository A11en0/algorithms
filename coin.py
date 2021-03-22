def coinChange(coins, amount):
    if amount < 0:
        return -1

    if amount == 0:
        return 0

    ret = float("INF")
    for coin in coins:
        subproblem = coinChange(coins, amount - coin)
        if subproblem == -1: continue
        ret = min(ret, subproblem + 1)

    return ret if ret != float("INF") else -1

if __name__ == '__main__':
    ret = [coinChange([1, 3, 5], i) for i in range(30)]
    print(ret)