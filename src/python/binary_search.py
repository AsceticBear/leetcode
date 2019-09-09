'''
Binary Search

Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums. If target exists, then return its index, otherwise return -1.
'''

'''

1. 最简单的 list 索引

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1
```

2. 二分查找

要设置左右两个标记位来表示位置，当左边小于右边的时候，把中间位置的值和 target 进行比较：

* 如果等于 target， 返回该值;
* 如果大于 target， 右边的标记左移一位。
* 如果小于 target,  左边的标记右移一位。

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            else:
                if target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
        return -1
```

'''