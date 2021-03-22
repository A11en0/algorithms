def BubbleSort(items):
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                tmp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = tmp

    return items

if __name__ == '__main__':

    import random
    a = [random.randint(0, 10) for i in range(10)]
    print(BubbleSort(a))