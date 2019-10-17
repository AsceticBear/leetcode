import sys
import re

num_regex = re.compile('[0-9]')
english_regex = re.compile('[a-zA-Z]')

def getEnglishCharCount(str):
    return len(english_regex.findall(str));

def getBlankCharCount(str):
    return str.count(' ');

def getNumberCharCount(str):
    return len(num_regex.findall(str));

def getOtherCharCount(str):
    return len(str) - getNumberCharCount(str) - getBlankCharCount(str) - getEnglishCharCount(str) - 1;

for line in sys.stdin:
    print(getEnglishCharCount(line))
    print(getBlankCharCount(line))
    print(getNumberCharCount(line))
    print(getOtherCharCount(line))



