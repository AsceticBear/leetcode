import sys

for line in sys.stdin:
    splited_str = line.split();
    print(len(splited_str[-1]))

# class Solution(object):
#     def getLen(self, str):
#         splited_str = str.split();
#         # print(splited_str[-1])
#         return len(splited_str[-1])

# if __name__ == '__main__':
#     s = Solution();
#     str = 'XSUWHQ'
#     print(s.getLen(str))

import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)
    

