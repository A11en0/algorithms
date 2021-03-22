class Solution:
    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        result = 0
        while (x != 0):
            res = x % 10
            result = result * 10 + res
            x = x // 10

        return temp == result

    def isPalindrome2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome2(-121))
