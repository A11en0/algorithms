def binarySqrt(n, u):
    low, high = 0, n

    while low <= high:
        mid = (low + high) / 2
        sqrt = n / mid
        if(mid == sqrt):
            return mid
        elif mid < sqrt:
            low = mid + u
        else:
            high = mid - u
    return high

if __name__ == '__main__':
    ret = binarySqrt(4, 1e-10)
    print(ret)
