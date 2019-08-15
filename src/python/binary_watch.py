'''
Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
'''

# Add code here

'''
分析：

from collections import defaultdict

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        hours = defaultdict(list)
        mins = defaultdict(list)
        # count and store all hours by its '1'count
        for i in range(0, 12):
            binCount = bin(i)[2:].count('1')
            hours[binCount].append(i)
        
        # count and store all mins by its '1' count
        for j in range(0, 60):
            binCount = bin(j)[2:].count('1')
            mins[binCount].append(j)
            
        ans = []
        #print(hours)
        #print(mins)
        for i in range(0, num+1):   
            for hour in hours[i]:
                for minute in mins[num-i]:
                    ans.append(str(hour) + ":" + "{0:0>2}".format(minute))

        return ans
		```

先把 12 小时，用 4 位二进制表示出来，分别是：
0001 0010 0011 0100
0101 0110 0111 1000
1001 1010 1011 1100

再把 59 分钟， 用 6 位二进制表示出来，分别是：
～～～～～～～
～～～～～～～
～～～～～～～

统一 1 的数量，双层循环遍历， hours 和 minites, 统计 1 的数量，相加之和等于 number 即可。
'''