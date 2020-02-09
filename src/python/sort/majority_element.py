'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

https://leetcode.com/problems/majority-element/
'''

'''
I. 最粗鲁的方法，循环计数，比对，返回结果

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

II. Sort Array

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
'''