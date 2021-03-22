class Solution:
    def summaryRanges(self, nums):
        i, j = 0, 1
        lists = []

        for n in range(len(nums)):
            if j > len(nums):
                break
            lists.append([])
            while (j < len(nums)) and (nums[j] - nums[i] == 1):
                lists[n].append(nums[i])
                i += 1
                j += 1
            lists[n].append(nums[i])
            i += 1
            j += 1

        ret = []
        for _ in lists:
            if len(_) == 1:
                current = str(_[0])
            else:
                current = str(_[0]) + "->" + str(_[-1])
            ret.append(current)

        return ret

s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))

