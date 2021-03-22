import numpy as np
def ZeroOneBag(N, W, vals, weight):
    cell = [[0]*(W + 1)]*(N + 1)
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if weight[i] <= j:
                cell[i][j] = max(cell[i - 1][j- weight[i]] + vals[i], cell[i - 1][j])
            else:
                cell[i][j] = cell[i - 1][j]
    return cell

def solve2(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalWeight)+1,dtype=np.int32)
    for i in range(1,totalLength+1):
        for j in range(totalWeight,0,-1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j],resArr[j-wlist[i]]+vlist[i])
    return resArr

# if __name__ == '__main__':
#     v = [0,60,100,120]
#     w = [0,10,20,30]
#     weight = 50
#     n = 3
#     result = solve2(v,w,weight,n)
#     print(result)

if __name__ == '__main__':
    # ret = ZeroOneBag(3, 4, [0, 1500, 3000, 2000], [0, 1, 4, 3])
    ret = solve2([0, 1500, 3000, 2000], [0, 1, 4, 3], 4, 3)
    print(ret)