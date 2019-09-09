'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
'''

'''

class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans

思路： 大致分为两个模块：
1. 统计数组值出现的最多次数
2. 用 left 和 right 分别标记数组值第一次出现的位置和最后一次出现的位置。数组中所有的值都标记好之后，left - right + 1 就是该值的最大子字符串长度。

Note: 重点在于对数组内容进行重新整合。
'''