class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0:
            x = -x
            flag = 1

        result = 0
        while(x != 0):
            res = x % 10
            result = result * 10 + res
            x = x // 10

        if result > 2**31 - 1 or  result < -2**31:
            return 0

        if flag == 1:
            return -result

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-4389))