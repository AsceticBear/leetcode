'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

https://leetcode.com/problems/add-digits/
'''

'''
I. Iteration

class Solution(object):
      def addDigits(self, num):
    """
    :type num: int
    :rtype: int
    """
    while(num >= 10):
        temp = 0
        while(num > 0):
            temp += num % 10
            num /= 10
        num = temp
    return num

II. Digit root

dr(n) = 1 + (n - 1) % 9

class Solution(object):
    def addDigits(self, num):
    """
    :type num: int
    :rtype: int
    """
    if num == 0 : return 0
    else:return (num - 1) % 9 + 1
'''