def multiply(a, b):
    n = len(a)
    c = [[0]*len(b[1]) for i in range(n)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            c[i][j] = 0
            for k in range(len(a[1])):
                c[i][j] += a[i][k] * b[k][j]
    return c

if __name__ == '__main__':
    a = [
        [1, 2, 3], [3, 4, 1]
    ]

    b = [
        [1, 2], [3, 4], [2, 3]
    ]

    ret = multiply(a, b)
    print(ret)
