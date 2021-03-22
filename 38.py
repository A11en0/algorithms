class Solution:
    def countAndSay(self, n):
        prev = "1"

        for i in range(1, n):
            start, end = 0, 0
            curr = ""

            while end < len(prev):
                while end < len(prev) and prev[start] == prev[end]:
                    end += 1

                curr += str(end - start) + prev[start]
                start = end
            prev = curr
        return prev

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(5))