'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        for i in range(len(s)):
            print(f'==> i = {i}')
            l1 = self.expandAroundCenter(s, i, i)
            l2 = self.expandAroundCenter(s, i, i + 1)
            max_l =  l1 if l1 > l2 else l2
            if max_l > end - start:
                start = i - (max_l - 1) // 2
                end = i + max_l // 2
        
        print(f'start: {start} end: {end}')
        print(f'longestPalindrome： {s[start:end + 1]}')
        return s[start:end+1]
    
    def expandAroundCenter(self, s: str, l: int, r: int) -> int:
        while l > 0 and r < len(s) and s[l] == s[r]:
            l = l - 1
            r = r + 1

        print(f'expandAroundCenter: left: {l}, right: {r}, return: {r-l-1}')
        return r-l-1


if __name__ == '__main__':
    s = Solution()

    # example 1
    input = "babad"
    output1 = "bab" 
    output2 = "aba" 
    assert s.longestPalindrome(input) == output1 or s.longestPalindrome(input) == output2  
    
    # example 2
    input = "cbbd"
    output = "bb"
    assert s.longestPalindrome(input) == output
