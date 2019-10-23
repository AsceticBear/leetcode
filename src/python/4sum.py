'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

https://leetcode.com/problems/4sum/
'''
from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    print('nums after sorted', nums)

    # Deal with extreme cases
    if target < nums[0] || target > nums[n-1]:
        return []
    
    n = nums.length
    l, r = 0, n - 1
    result = []

    if nums[l] + nums[r] < target:
        

    return [1]

def test_fourSum():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    assert fourSum(nums, target) == []


