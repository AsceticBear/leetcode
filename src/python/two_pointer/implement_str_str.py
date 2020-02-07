'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1


if __name__ == "__main__":
    s = Solution()

    assert s.strStr("hello", "ll"), 2
    assert s.strStr("aaaaa", "bba"), -1
    assert s.strStr("", "a"), -1
