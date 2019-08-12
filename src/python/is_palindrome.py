import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

        
class TestCases(unittest.TestCase):
    def test_example1(self):
        # example 1
        s = Solution()
        input = 121
        self.assertTrue(s.isPalindrome(input))
        
    def test_example_2(self):
        # example 2
        s = Solution()
        input = -121
        self.assertFalse(s.isPalindrome(input)) 


if __name__ == "__main__":
    unittest.main()

'''
分析：

1. 第一种方式

将 int 类型的入参 a 转换为字符串 sa, 再对 sa 做字符串反转操作生成 reverse_sa, 比较 sa == reverse_sa.

2. 第二种方式

折半比较法，例如 `12321`， 把前边的 `12` 和后边的 `21` 通过对 10 进行模运算取出来，然后对比。

临界条件：

当前半部分小于等于后半部分的值时，就说明到中间了。
'''
