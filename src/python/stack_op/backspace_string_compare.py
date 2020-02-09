'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

https://leetcode.com/problems/backspace-string-compare/
'''

'''
class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
'''