#

def func(x):
    return x**2 - x + 2


def fibo_solve(a, b, sigma, func):
    c = 1.0 / sigma
    n = 1
    F = [1, 1]
    f = F[0] + F[1]
    while f < c:
        f = F[n] + F[n - 1] # 2
        F.append(f)
        n += 1

    k = 1
    x1 = a + (F[n - 2] / F[n])*(b - a)
    x2 = a + (F[n - 1] / F[n])*(b - a)

    f1 = func(x1)
    f2 = func(x2)

    while k < n - 2:
        print("[a, b] = [{:.3f}, {:.3f}]; x1 = {:.3f}; x2 = {:.3f}; f1 = {:.3f}; f2 = {:.3f}".format(a, b, x1, x2, f1, f2))
        if f1 < f2:
            b = x2; x2 = x1; f2 = f1
            x1 = a + (F[n - k - 2] / F[n - k])*(b - a)
            f1 = func(x1)
        else:
            a = x1; x1 = x2; f1 = f2
            x2 = a + (F[n - k - 1] / F[n - k])*(b - a)
            f2 = func(x2)

        k += 1



    if f1 < f2:
        b = x2; x2 = x1; f2 = f1
    else:
        a = x1

    x1 = x2 - 0.1*(b - a)
    # f1 = func(x1)

    # 对书上算法存在疑问？
    # if f1 < f2:
    #     x = (a + x2)*0.5
    # elif f1 == f2:
    #     x = (x1 + x2)*0.5
    # else:
    #     x = (x1 + b)*0.5

    x = (x1 + x2)*0.5

    return x, func(x)

x, y = fibo_solve(-1, 3, 0.08, func)
print("x = %.3f, y = %.3f" % (x, y))



