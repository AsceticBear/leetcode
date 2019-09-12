'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

https://leetcode.com/problems/sqrtx/
'''

'''
I. 牛顿迭代法

r = x
    while r*r > x:
        r = (r + x/r) / 2
    return r
'''