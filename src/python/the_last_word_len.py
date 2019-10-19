import sys

for line in sys.stdin:
    splited_str = line.split();
    print(len(splited_str[-1]))