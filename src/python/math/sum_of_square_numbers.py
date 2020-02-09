'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

https://leetcode.com/problems/sum-of-square-numbers/
'''

'''
I. 暴力解决

public class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            for (long b = 0; b * b <= c; b++) {
                if (a * a + b * b == c)
                    return true;
            }
        }
        return false;
    }
}

II. 优化后的

public class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            double b = Math.sqrt(c - a * a);
            if (b == (int) b)
                return true;
        }
        return false;
    }
}
'''