class Solution:
    def countPrimes(self, n: int) -> int:
        cnt = 0
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0:
                    # flag = False
                    break
            else:
                cnt += 1
            #
            # if flag == True:
            #     cnt += 1

        return cnt

    def shaifa(self, n):
        isPrim = [True]*n
        for i in range(2, int(n**0.5) + 1):
            if isPrim[i]:
                for j in range(i**2, n, i):
                    isPrim[j] = False

        cnt = 0
        for i in range(2, len(isPrim)):
            if isPrim[i]:
                cnt += 1

        return cnt

if __name__ == '__main__':
    S = Solution()
    print(S.shaifa(12))