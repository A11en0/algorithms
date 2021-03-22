class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        left = ['(', '[', '{']
        right = [')', ']', '}']

        for _ in s:
            if _ in left:
                stack.append(_)
            elif _ in right:
                if stack == []:
                    return False
                if stack[-1] == left[right.index(_)]:
                    stack.pop()
                else:
                    return False

        if stack == []:
            return True

        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("]"))

