# 进退法

def func(x):
    return x**2 - 2*x + 1


def advance_retreat(x0, delta, func):
    x1 = x0 + delta
    f0 = func(x0)
    f1 = func(x1)

    while True:
        if f1 <= f0:
            delta *= 2
            x2 = x1 + delta
            f2 = func(x2)
            if f1 <= f2:
                return (x0, x2)
            else:
                x0 = x1; x1 = x2
                f0 = f1; f1 = f2

        else:
            delta *= 2
            x2 = x0 - delta
            f2 = func(x2)
            if f0 <= f2:
                return (x2, x1)
            else:
                x1 = x0; x0 = x2
                f1 = f0; f0 = f2


if __name__=="__main__":
    from gold_solve import *
    ret = advance_retreat(-5, 0.001, func)
    print("查找结果区间[a, b]: [{:.3f}, {:.3f}]".format(ret[0], ret[1]))

    print("\n将得到的区间使用黄金分割法计算：")
    x, y = gold_solve(ret[0], ret[1], func)
    print("x = {:.3f}, y = {:.3f}".format(x, y))