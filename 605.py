class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        i, j = 0, 1
        useful = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 1 and n == 0:
                return True
            elif flowerbed[0] == 0 and n == 1:
                return True
            elif flowerbed[0] == 0 and n == 0:
                return True
            elif flowerbed[0] == 1 and n == 1:
                return  False

        while(j < len(flowerbed)):
            if flowerbed[j] == 1:
                if flowerbed[0] == 0:
                    gap = j
                    useful += gap // 2
                else:
                    gap = j - i - 1
                    if gap % 2 == 0:
                        useful += gap / 2 - 1
                    else:
                        useful += gap // 2
                    i = j
            j += 1

        if flowerbed[-1] == 0:
            gap = len(flowerbed) - i - 1
            useful += gap // 2

        return useful >= n

s = Solution()
print(s.canPlaceFlowers([0], 1))
