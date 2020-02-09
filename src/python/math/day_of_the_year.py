'''
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

https://leetcode.com/problems/day-of-the-year/
'''

'''
class Solution:
    def dayOfYear(self, date: str) -> int:
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = map(int, date.split("-"))
        days = 0
        if y%400==0:
            month[1] = 29
        elif y%4 == 0 and y%100 != 0:
            month[1] = 29
        days += sum(month[0:m-1])
        return days+d
'''