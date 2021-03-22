

def insertSort(A):
    n = len(A)

    for j in range(1, n):
        i = j - 1
        key = A[j]
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1

        A[i + 1] = key

if __name__ == '__main__':
    A = [2, 8, 5, 3, 8, 12]
    insertSort(A)
    print(A)
