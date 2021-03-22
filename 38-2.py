class Solution:
    def countAndSay(self, n):
        if n <= 1:
            return "1"

        prev = self.countAndSay(n-1)
        curr = ""
        start, end = 0, 0

        while end < len(prev):
            while end < len(prev) and prev[start] == prev[end]:
                end += 1
            curr += str(end - start) + prev[start]
            start = end

        return curr

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(10))