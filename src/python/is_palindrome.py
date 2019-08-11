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
