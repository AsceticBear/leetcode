'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        for i in range(s.len()):
            len = expandAroundCenter(s, i, i)
            if len > end - start:
                start = i - len / 2
                end = i + len / 2

        return s[start:end]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int：
        while(left > 0 && right < s.len() && s[left] == s[right]):
            left = left - 1
            right = right + 1
        
        return 


if __name__ == '__main__':
    s = Solution()

    # example 1
    input = "babad"
    output = "bab"
    assert s.longestPalindrome(input) == output 
    
    # example 2
    input = "cbbd"
    output = "bb"
    assert s.longestPalindrome(input) == output
