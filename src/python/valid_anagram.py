'''
Given two strings s and t , write a function to determine if t is an anagram of s.

https://leetcode.com/problems/valid-anagram/
'''

'''
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
        return false;
    }
    char[] str1 = s.toCharArray();
    char[] str2 = t.toCharArray();
    Arrays.sort(str1);
    Arrays.sort(str2);
    return Arrays.equals(str1, str2);
}
'''