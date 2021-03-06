# 黄金分割搜索

def func(x):
    return x**2 - x + 2


def gold_solve(a, b, func):
    x1 = a + 0.382*(b - a)
    x2 = a + 0.618*(b - a)

    f1 = func(x1)
    f2 = func(x2)
    k = 1

    # 设置阈值 0.32
    while abs(b - a) > 0.32:
        print("第{}次迭代： [a, b] = [{:.3f}, {:.3f}]; x1 = {:.3f}; x2 = {:.3f}; f1 = {:.3f}; f2 = {:.3f}".
              format(k, a, b, x1, x2, f1, f2))
        if f1 < f2:
            b = x2
        elif f1 == f2:
            a = x1; b = x2
        else:
            a = x1

        x1 = a + 0.382 * (b - a)
        x2 = a + 0.618 * (b - a)
        f1 = func(x1)
        f2 = func(x2)
        k += 1

    x = (x1 + x2)*0.5
    y = func(x)
    return x, y

if __name__=="__main__":
    x, y = gold_solve(-1, 3, func)
    print("x = %.3f, y = %.3f" % (x, y))
