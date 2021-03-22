# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"

class Solution:
    def longestCommonPrefix(self, strs):
        ret = 0

        if len(strs) == 0:
            return ""

        for i in range(len(strs[0])):
            current = strs[0][:i+1]
            cnt = 0
            for j in range(len(strs)):
                if strs[j][:i+1] == current:
                    cnt += 1
                    continue
                else:
                    break                 
            if cnt == len(strs):
                ret = i + 1

        return strs[0][:ret]

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["a"]))