def quickSort(elem, lo, hi):
    if lo < hi:
        mi = partition(elem, lo ,hi)
        quickSort(elem, lo, mi - 1)
        quickSort(elem, mi + 1, hi)
    return elem

def partition(elem, lo, hi):
    pivot = elem[lo]
    while lo < hi:
        while lo < hi and elem[hi] > pivot: hi -= 1
        elem[lo] = elem[hi]
        while lo < hi and elem[lo] <= pivot: lo += 1
        elem[hi] = elem[lo]
    elem[lo] = pivot
    return lo

if __name__ == '__main__':
    import random, time
    a = [random.randint(0, 10) for i in range(10000)]
    start = time.time()
    ret = quickSort(a, 0, len(a) - 1)
    print(time.time() - start)
