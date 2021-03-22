def LCS(X, Y):
    m = len(X)
    n = len(Y)

    c = [[0]*(n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]
            else:
                c[i][j] = c[i][j - 1]
    return c


def LCS_PRINT(X, Y, i, j, c):
    if i == 0 or j == 0:
        return

    if X[i - 1] == Y[j - 1]:
        LCS_PRINT(X, Y, i - 1, j - 1, c)
        print(X[i - 1])

    elif c[i - 1][j] >= c[i][j - 1]:
        LCS_PRINT(X, Y, i - 1, j, c)

    else:
        LCS_PRINT(X, Y, i, j - 1, c)


def LCS_PRINT_NEW(X, Y, i, j, c):
    ret = ""
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            ret += X[i - 1]
            i -= 1
            j -= 1

        elif c[i - 1][j] >= c[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return ret[::-1]


def LCS_PRINT_NEW_ALL(X, Y, i, j, c, lcs_string):

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string += X[i - 1]
            i -= 1
            j -= 1

        elif c[i - 1][j] > c[i][j - 1]:
            i -= 1

        elif c[i][j - 1] > c[i - 1][j]:
            j -= 1

        else:
            LCS_PRINT_NEW_ALL(X, Y, i - 1, j, c, lcs_string)
            LCS_PRINT_NEW_ALL(X, Y, i, j - 1, c, lcs_string)
            return

    ret.append(lcs_string[::-1])


if __name__ == '__main__':
    a = 'abcbdab'
    b = 'bdcaba'

    m = len(a)
    n = len(b)

    c = LCS(a, b)

    ret = []

    # result = LCS_PRINT_NEW(a, b, m, n, c)

    LCS_PRINT_NEW_ALL(a, b, m, n, c, "")

    print(ret)