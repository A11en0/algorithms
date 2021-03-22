class Solution:
    def romanToInt(self, s: str) -> int:
        vmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sp = {"IV": 4, "IX": 9, "XL": 40 , "XC": 90, "CD": 400, "CM": 900}

        ret = 0
        i = 0
        while i < len(s):
            next = i + 2
            if s[i:next] in sp:
                print(s[i:next])
                ret += sp.get(s[i:next])
                i += 2
                continue
            ret += vmap.get(s[i])
            i += 1

        return ret

if __name__ == '__main__':
    s = Solution()