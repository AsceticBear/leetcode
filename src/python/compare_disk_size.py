# 1 T = 1000G
# 1 G = 1000M

import sys

def sortedDictValues(d): 
    items = d.items()
    items.sort() 
    return [(key, value) for key, value in items]

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    info = dict()
    origin = dict()
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        origin[i] = line;
        if line[-1] == 'T':
            info[i] = int(line[:-1]) * 1000 * 1000
        elif line[-1] == 'G':
            info[i] = int(line[:-1]) * 1000
        else:
            info[i] = int(line[:-1])
    
    items = sorted(info.items(), key = lambda x: x[1], reverse=False)
    
    for key, value in items:
        print(origin[key])

    

