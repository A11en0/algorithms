# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


class Solution:
    def maxSubArray(self, nums):

        res = []

        for i in range(1, len(nums)):
            res.append(max(res[i - 1] + nums[i], nums[i]))


        # max_ = -2e+32
        #
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)+1):
        #         sum_ = sum(nums[i:j])
        #         if sum_ > max_:
        #             max_  = sum_
        #
        # return max_



if __name__ == '__main__':
    nums = [-1]
    s = Solution()
    print(s.maxSubArray(nums))